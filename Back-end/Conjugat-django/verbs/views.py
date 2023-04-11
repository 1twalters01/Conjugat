from django.core.cache import cache
from .models import RomanceMain
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
import random, string

class VerbRandomRetrieval(APIView):
    permission_classes = (permissions.AllowAny,)
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
        TestID = 3333 # placeholder
        # Try random x digit alphanumeric string. Repeat if it is in the the cache. If failed 3 consecutive times then increase the number of digits by one. Store the size of this digit in cache as it is a singular number for all users of the site
        # count = 0
        # while True:
        #     TestID = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(length))
        #     if cache.get(TestID) == None:
        #         break
        #     count += 1
        #     if count == 3:
        #       count = 0
        #       # set length to be length += 1

        Test_json = {
            'TestID': TestID,
            'Test': formated_json_list
        }
        cache.set(key=TestID, value=formated_json_list)
        return Response(data=Test_json, status=status.HTTP_200_OK)



class VerbTest(APIView):
    permission_classes = (permissions.AllowAny,)
    # authentication_classes = (SessionAuthentication,)
    def post(self, request):
        data = request.data

        TestID = data['results']['TestID']
        IDs = [int(elem) for elem in data['results']['IDs']]
        Answers = data['results']['answers']
        print(TestID)
        print(IDs)
        print(Answers)

        for index, item in enumerate(Answers):
            print(index, item, IDs[index])
        objects = RomanceMain.objects.filter(pk__in=IDs)
        for index, object in enumerate(objects):
            print(object.conjugation, Answers[index])
            if (str(object.conjugation) == Answers[index]):
                print(f'Correct answer: {object.conjugation}')
            else:
                print (f'Incorrect answer: {object.conjugation}')
        return Response(status=status.HTTP_200_OK)
