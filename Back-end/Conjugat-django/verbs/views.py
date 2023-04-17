from django.core.cache import cache
from .models import RomanceMain, RomanceTestResult, RomanceTestResult_by_user_and_language, RomanceTestResult_by_user_and_date
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
import random, string
from testFunctionality.models import TestIdDigits

import uuid
from datetime import datetime, timedelta

class VerbRandomRetrieval(APIView):
    permission_classes = (permissions.AllowAny,)
    def generate_TestID(self):
        count = 0
        digits = TestIdDigits.objects.get()
        while True:
            TestID = ''.join(random.choice(string.digits) for _ in range(digits.digits))
            if cache.get(TestID) == None:
                return TestID
            count += 1
            if count == 3:
              count = 0
              digits.digits = digits.digits + 1
              digits.save()

    def post(self, request):
        data = request.data
        language = data['language']
        number = data['number']
        lower = 1
        upper = 100
        numbers = sorted(random.sample(range(lower, upper), number))
        objects =  RomanceMain.objects.filter(rank__in=numbers, conjugation__base__language__language__in=language).order_by('pk')
        formated_json_list = []
        for object in objects:
            if len(formated_json_list) == 0:
                formated_json = {
                    'Language': object.subject.language.language,
                    'Base': object.conjugation.base.base,
                    'Tense': object.tense.tense,
                    'IDs': [object.pk],
                    'Subjects': [object.subject.subject],
                    'Auxiliaries': [object.auxiliary.auxiliary],
                    'Verbs': [object.conjugation.conjugation]
                }
                formated_json_list.append(formated_json)
            else:
                if object.tense.tense == formated_json_list[-1]['Tense'] and object.conjugation.base.base == formated_json_list[-1]['Base']:
                    formated_json_list[-1]['IDs'].append(object.pk)
                    formated_json_list[-1]['Subjects'].append(object.subject.subject)
                    formated_json_list[-1]['Auxiliaries'].append(object.auxiliary.auxiliary)
                    formated_json_list[-1]['Verbs'].append(object.conjugation.conjugation)
                else:
                    formated_json_list.append({
                        'Language': object.subject.language.language,
                        'Base': object.conjugation.base.base,
                        'Tense': object.tense.tense,
                        'IDs': [object.pk],
                        'Subjects': [object.subject.subject],
                        'Auxiliaries': [object.auxiliary.auxiliary],
                        'Verbs': [object.conjugation.conjugation]
                    })

        random.shuffle(formated_json_list)
        TestID = self.generate_TestID()
        
        Test_json = {
            'TestID': TestID,
            'Test': formated_json_list
        }

        cache.set(key=TestID, value=numbers, timeout=(30*60))
        return Response(data=Test_json, status=status.HTTP_200_OK)



class VerbTest(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request):
        # Get data from the post request
        data = request.data
        tempTestID = data['results']['TestID']
        IDs = [int(elem) for elem in data['results']['IDs']]
        Submitted = data['results']['answers']
        object_pks = cache.get(key=int(tempTestID))
        StartDateTime = datetime.now()
        EndDateTime = datetime.now()+timedelta(minutes=5)
       
        # Initialise key variables
        while True:
            TestID = uuid.uuid4() # Generate permanent TestID
            try:
                ValidateUUID = RomanceTestResult.objects.get(pk=TestID)
            except:
                ValidateUUID = None
            if not ValidateUUID:
                break
        
        try:
            objects = RomanceMain.objects.filter(pk__in=object_pks) # Get list of conjugations tested
        except:
            objects = None
        if not objects:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        #Create blank lists for relevant properties
        languages = []
        ranks = []
        tenses = []
        bases = []
        subjects = []
        auxiliaries = []
        verbs = []
        answersList = []
        statusList = []

        # Fill in blank lists by looping through objects
        for object in objects:
            languages.append(object.subject.language.language)
            ranks.append(object.pk)
            tenses.append(object.tense.tense)
            bases.append(object.conjugation.base.base)
            subjects.append(object.subject.subject)
            auxiliaries.append(object.auxiliary.auxiliary)
            verbs.append(object.conjugation.conjugation)

            if object.pk in IDs: # Filled in answers
                SubmittedIndex = IDs.index(object.pk)
                if (str(object.conjugation) == Submitted[SubmittedIndex]): # Correctly answered
                    answersList.append(Submitted[SubmittedIndex])
                    statusList.append(True)
                    # print (f'Correct answer: {object.conjugation}')

                else: # Incorrect answered
                    answersList.append(Submitted[SubmittedIndex])
                    statusList.append(False)
                    # print (f'Incorrect answer: {Submitted[SubmittedIndex]} instead of {object.conjugation}')

            else: # Left blank
                statusList.append(False)
                answersList.append('')
                # print(f'Not answered: {object.conjugation, object.pk}')

        # Save to redis cache
        # part 1 - save user and test ids
        timeoutTime = 10*24*3600 # Safety factor of 3 days so chronjob has time to clean up
        currentUserTestValues = cache.get(key=request.user.username)
        if currentUserTestValues == None:
            currentUserTestValues = []
        currentUserTestValues.append(TestID)
        cache.set(key = request.user.username, value=currentUserTestValues, timeout=timeoutTime)

        # part 2 - save test id results
        timeoutTime = 7*24*3600 # Tests last 7 days in cache
        cache.set(key=TestID, timeout=timeoutTime, value=({
            'rank':ranks,
            'language':languages,
            'StartDateTime':StartDateTime,
            'EndDateTime':EndDateTime,
            'answers':answersList,
            'status':statusList
        }))

        # Save to cassandra database
        TestResult = RomanceTestResult(
            testID=TestID,
            user = request.user.id,
            StartDateTime = StartDateTime,
            EndDateTime = EndDateTime,
            ranks = ranks,
            languages = languages,
            answers = answersList,
            status = statusList,
        )

        for language in languages:
            TestResultByLanguage = RomanceTestResult_by_user_and_language(
                testID=TestID,
                user = request.user.id,
                language = language,
            )

        TestResultByDate = RomanceTestResult_by_user_and_date(
            testID=TestID,
            user = request.user.id,
            EndDateTime = EndDateTime
        )

        print(cache.get(key=TestID))

        TestResult.save()
        TestResultByLanguage.save()
        TestResultByDate.save()

        # Delete the temporary testID data once it has been saved
        cache.delete(key=tempTestID)

        return Response(data=TestID, status=status.HTTP_200_OK)