from django.core.cache import cache
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import RomanceMain
import random

class VerbRandomRetrieval(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        language = data['language']
        number = data['number']
        lower = 1
        upper = 100
        numbers = sorted(random.sample(range(lower, upper), number))
        objects =  RomanceMain.objects.filter(rank__in=numbers, conjugation__base__language__language__in=language)
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
        return Response(data=formated_json_list, status=status.HTTP_200_OK)



class VerbTest(APIView):
    permission_classes = (permissions.AllowAny,)
    # authentication_classes = (SessionAuthentication,)
    def post(self, request):
        data = request.data

        IDs = data['results']['IDs']
        Answers = data['results']['answers']
        IDs = [int(elem) for elem in IDs]

        objects = RomanceMain.objects.filter(pk__in=IDs)
        for index, object in enumerate(objects):
            print(object.conjugation, Answers[index])
            if (str(object.conjugation) == Answers[index]):
                print(f'Yeah buddy: {object.conjugation}')
            else:
                print (f'nah retard: {object.conjugation}')
        return Response(status=status.HTTP_200_OK)
