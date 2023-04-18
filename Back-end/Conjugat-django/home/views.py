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

        testIDs = cache.get(key=request.user.username)
        tests = [cache.get(testID) for testID in testIDs]
        tests = sorted(tests, key=lambda x: x['EndDateTime'])
        data = []
        for test in tests:
            date = test['EndDateTime'].date()
            incorrect_count = test['status'].count(False)
            correct_count = test['status'].count(True)

            if len(data) == 0:
                formated_json = {
                    'Date': [date],
                    'Incorrect': [incorrect_count],
                    'Correct': [correct_count],
                }
                data.append(formated_json)

            else:
                if date == data[-1]['Date'][0]:
                    data[-1]['Incorrect'].append(incorrect_count)
                    data[-1]['Correct'].append(correct_count)
                else:
                    formated_json = {
                        'Date': [date],
                        'Incorrect': [incorrect_count],
                        'Correct': [correct_count],
                    }
                    data.append(formated_json)

        return Response(data=data, status=status.HTTP_200_OK)
    
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