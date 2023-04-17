from django.core.cache import cache
from verbs.models import RomanceTestResult, RomanceTestResult_by_user_and_language, RomanceTestResult_by_user_and_date
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime, timedelta

class homeView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        # RomanceTestResult_by_user_and_date.objects.filter(pk=request.user.id).delete()
        # RomanceTestResult_by_user_and_language.objects.filter(pk=request.user.id).delete()
        tests = RomanceTestResult_by_user_and_date.objects.get(pk=request.user.id)
        print(tests)
        tests.objects.filter(EndDateTime__gte=(datetime.today() - timedelta(days=7)))
        print(tests.testID)
        return Response(status=status.HTTP_200_OK)
    
# class homeAltView(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#     def get(self, request):
#         tests = RomanceTestResult_by_user_and_date.objects.filter(EndDateTime__gte=(datetime.today() - timedelta(days=7)))
#         print(tests)
#         tests.objects.filter(user=request.user.id)
#         print(tests.testID)
#         return Response(status=status.HTTP_200_OK)