from django.core.cache import cache
from verbs.models import RomanceTestResult, RomanceTestResult_by_user_and_language, RomanceTestResult_by_user_and_date
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime, timedelta

class homeView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        # pk = request.user.id
        # RomanceTestResult_by_user_and_date.objects.filter(pk=pk).delete()
        # RomanceTestResult_by_user_and_language.objects.filter(pk=pk).delete()
        
        # tests = RomanceTestResult_by_user_and_date.objects.filter(pk=request.user.id)
        tests = RomanceTestResult_by_user_and_date.objects.filter(pk=78)
        tests = tests.filter(EndDateTime__gte=(datetime.today() - timedelta(days=7)))
        for test in tests:
            print(test.testID)
        
        # print(tests.testID)
        return Response(status=status.HTTP_200_OK)
    
# class homeAltView(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#     def get(self, request):
#         tests = RomanceTestResult_by_user_and_date.objects.filter(EndDateTime__gte=(datetime.today() - timedelta(days=7)))
#         print(tests)
#         tests.objects.filter(user=request.user.id)
#         print(tests.testID)
#         return Response(status=status.HTTP_200_OK)