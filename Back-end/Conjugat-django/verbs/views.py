from django.core.cache import cache
from .models import RomanceMain
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
import random, string
from testFunctionality.models import TestIdDigits

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

        cache.set(key=TestID, value=numbers, timeout=(1*60))
        return Response(data=Test_json, status=status.HTTP_200_OK)



class VerbTest(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data

        TestID = data['results']['TestID']
        IDs = [int(elem) for elem in data['results']['IDs']]
        Submitted = data['results']['answers']
        Answers = cache.get(key=int(TestID))

        results = []
        result = None
        objects = RomanceMain.objects.filter(pk__in=Answers)
        for object in objects:
            print(IDs, object.pk)
            if object.pk in IDs:
                SubmittedIndex = IDs.index(object.pk)
                if (str(object.conjugation) == Submitted[SubmittedIndex]):
                    result = True
                    print(f'Correct answer: {object.conjugation}')
                else:
                    result = False
                    print (f'Incorrect answer: {Submitted[SubmittedIndex]} instead of {object.conjugation}')
            else:
                result = None
                print(f'Not found {object.conjugation, object.pk}')
            
            if len(results) == 0:
                formated_json = {
                    'Language': object.subject.language.language,
                    'Base': object.conjugation.base.base,
                    'Tense': object.tense.tense,
                    'IDs': [object.pk],
                    'Subjects': [object.subject.subject],
                    'Auxiliaries': [object.auxiliary.auxiliary],
                    'Verbs': [object.conjugation.conjugation],
                    'Result': [result]
                }
                results.append(formated_json)
            else:
                if object.tense.tense == results[-1]['Tense'] and object.conjugation.base.base == results[-1]['Base']:
                    results[-1]['IDs'].append(object.pk)
                    results[-1]['Subjects'].append(object.subject.subject)
                    results[-1]['Auxiliaries'].append(object.auxiliary.auxiliary)
                    results[-1]['Verbs'].append(object.conjugation.conjugation)
                    results[-1]['Result'].append(result)
                else:
                    results.append({
                        'Language': object.subject.language.language,
                        'Base': object.conjugation.base.base,
                        'Tense': object.tense.tense,
                        'IDs': [object.pk],
                        'Subjects': [object.subject.subject],
                        'Auxiliaries': [object.auxiliary.auxiliary],
                        'Verbs': [object.conjugation.conjugation],
                        'Result': [result]
                    })
        return Response(data=results, status=status.HTTP_200_OK)
