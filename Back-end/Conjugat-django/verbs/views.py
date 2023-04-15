from django.core.cache import cache
from .models import RomanceMain, RomanceTestResult, RomanceTestResult_by_user_and_language, RomanceTestResult_by_user_and_date
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
import random, string
from testFunctionality.models import TestIdDigits

import uuid
from cassandra.cqlengine import columns
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
    def format_duration(self, delta):
        hours, remainder = divmod(delta.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        duration_string = 'P[0000]-[00]-[00]-T0{}:0{}:0{}'.format(hours, minutes, seconds)
        if delta.days > 0:
            duration_string = '{}d{}h{}m{}s'.format(delta.days, duration_string[1:])
        return duration_string
    
    def post(self, request):
        data = request.data

        TestID = data['results']['TestID']
        IDs = [int(elem) for elem in data['results']['IDs']]
        Submitted = data['results']['answers']
        Answers = cache.get(key=int(TestID))

        results = []
        result = None
        objects = RomanceMain.objects.filter(pk__in=Answers)
        
        languageList = []
        rankList = []
        answersList = []
        statusList = []

        for object in objects:
            rankList.append(object.pk)
            if object.subject.language.language not in languageList:
                languageList.append(object.subject.language.language)

            if object.pk in IDs:
                SubmittedIndex = IDs.index(object.pk)
                if (str(object.conjugation) == Submitted[SubmittedIndex]):
                    result = True
                    statusList.append(True)
                    answer = Submitted[SubmittedIndex]
                    answersList.append(Submitted[SubmittedIndex])
                    # print(f'Correct answer: {object.conjugation}')
                else:
                    result = False
                    statusList.append(False)
                    answer = Submitted[SubmittedIndex]
                    answersList.append(Submitted[SubmittedIndex])
                    # print (f'Incorrect answer: {Submitted[SubmittedIndex]} instead of {object.conjugation}')
            else:
                result = None
                statusList.append(False)
                answer = ''
                answersList.append('')
                # print(f'Not found {object.conjugation, object.pk}')
            
            if len(results) == 0:
                formated_json = {
                    'Language': object.subject.language.language,
                    'Base': object.conjugation.base.base,
                    'Tense': object.tense.tense,
                    'IDs': [object.pk],
                    'Subjects': [object.subject.subject],
                    'Auxiliaries': [object.auxiliary.auxiliary],
                    'Verbs': [object.conjugation.conjugation],
                    'Answers': [answer],
                    'Results': [result]
                }
                results.append(formated_json)
            else:
                if object.tense.tense == results[-1]['Tense'] and object.conjugation.base.base == results[-1]['Base']:
                    results[-1]['IDs'].append(object.pk)
                    results[-1]['Subjects'].append(object.subject.subject)
                    results[-1]['Auxiliaries'].append(object.auxiliary.auxiliary)
                    results[-1]['Verbs'].append(object.conjugation.conjugation)
                    results[-1]['Answers'].append(answer)
                    results[-1]['Results'].append(result)
                else:
                    results.append({
                        'Language': object.subject.language.language,
                        'Base': object.conjugation.base.base,
                        'Tense': object.tense.tense,
                        'IDs': [object.pk],
                        'Subjects': [object.subject.subject],
                        'Auxiliaries': [object.auxiliary.auxiliary],
                        'Verbs': [object.conjugation.conjugation],
                        'Answers': [answer],
                        'Results': [result]
                    })

        
        # TestID = uuid.uuid4().hex
        TestID = uuid.uuid4()

        print(TestID, type(TestID))
        StartDateTime = datetime.now()
        EndDateTime = datetime.now()+timedelta(minutes=5)

        # Save to cassandra database
        TestResult = RomanceTestResult(
            testID=TestID,
            user = request.user.id,
            StartDateTime = StartDateTime,
            EndDateTime = EndDateTime,
            rank = rankList,
            language = languageList,
            answers = answersList,
            status = statusList,
        )
        for language in languageList:
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

        TestResult.save()
        TestResultByLanguage.save()
        TestResultByDate.save()

        return Response(data=results, status=status.HTTP_200_OK)
