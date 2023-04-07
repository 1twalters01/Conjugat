from django.shortcuts import render, redirect
from .forms import HomeForm, SingleTestForm
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import RomanceMain

# Create your views here.


class VerbTest(APIView):
    permission_classes = (permissions.AllowAny,)
    # authentication_classes = (SessionAuthentication,)
    def post(self, request):
        data = request.data

        print(data['results'])
        IDs = data['results']['IDs']
        Answers = data['results']['answers']
        IDs = [int(elem) for elem in IDs]

        objects = RomanceMain.objects.filter(pk__in=IDs)
        print(objects.count())
        for index, object in enumerate(objects):
            print(object.conjugation, Answers[index])
            if (str(object.conjugation) == Answers[index]):
                print(f'Yeah buddy: {object.conjugation}')
            else:
                print (f'nah retard: {object.conjugation}')
        
        return Response(status=status.HTTP_200_OK)
    