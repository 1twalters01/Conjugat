from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import RomanceMain
import random

number = 15
lower = 1
upper = 100
numbers = sorted(random.sample(range(lower, upper), number))
objects =  RomanceMain.objects.filter(pk__in=numbers)
for object in objects:
    print(object.conjugation, object.pk)

class VerbRandomRetrieval(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        language = data['language']
        number = data['number']
        lower = 1
        upper = 100
        numbers = sorted(random.sample(range(lower, upper), number))
        objects =  RomanceMain.objects.filter(pk__in=numbers)
        for object in objects:
            print(object.conjugation, object.pk)



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
    