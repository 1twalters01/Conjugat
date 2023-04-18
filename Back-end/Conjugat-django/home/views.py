from django.core.cache import cache
from verbs.models import RomanceTestResult, RomanceTestResult_by_user_and_language, RomanceTestResult_by_user_and_date
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime, timedelta
from knox.models import AuthToken


class homeView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request):
        # pk = request.user.id
        # RomanceTestResult_by_user_and_date.objects.filter(pk=pk).delete()
        # RomanceTestResult_by_user_and_language.objects.filter(pk=pk).delete()
        
        # tests = RomanceTestResult_by_user_and_date.objects.filter(pk=request.user.id)
        # tests = tests.filter(EndDateTime__gte=(datetime.today() - timedelta(days=7)))
        # for test in tests:
        #     print(test.testID)
        
        # print(tests.testID)
        return Response(status=status.HTTP_200_OK)
    
class authTokenValidator(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        Authorization = request.headers['Authorization']
        token = Authorization.split('Token ')[1]
        valid = None

        knox_objects = AuthToken.objects.filter(token_key__startswith=token[:8])
        knox_users = [knox_object.user for knox_object in knox_objects]

        if request.user in knox_users:
            valid = True
        else:
            valid = False

        return Response(data=valid, status=status.HTTP_200_OK)