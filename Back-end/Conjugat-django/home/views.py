from django.core.cache import cache
from verbs.models import RomanceTestResult, RomanceTestResult_by_user_and_language, RomanceTestResult_by_user_and_date
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from knox.models import AuthToken
from operator import itemgetter
# Have not refactored this code in any way yet

class homeView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request):
        # RomanceTestResult_by_user_and_date.objects.filter(pk=request.user.id).delete()
        # RomanceTestResult_by_user_and_language.objects.filter(pk='English', user=request.user.id).delete()

        testIDs = cache.get(key=request.user.username)
        if testIDs:
            tests = [cache.get(testID) for testID in testIDs]
        else: tests=None
        if tests:
            tests = sorted(tests, key=lambda x: x['EndDateTime'])
        
        data = []
        if tests:
            for index, test in enumerate(tests):
                date = test['EndDateTime'].date()
                date = str(date)
                print(date)
                incorrect_count = test['status'].count(False)
                correct_count = test['status'].count(True)

                if len(data) == 0:
                    formated_json = {
                        'id': index+1,
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
                            'id': index+1,
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