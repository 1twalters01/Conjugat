from django.core.cache import cache
from verbs.models import RomanceTestResult, RomanceTestResult_by_user_and_language, RomanceTestResult_by_user_and_date
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from knox.models import AuthToken
from operator import itemgetter
from datetime import datetime, timedelta
# Have not refactored this code in any way yet

class homeView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request):
        # Get tests ordered by date in ascending order
        testIDs = cache.get(key=request.user.username)
        if testIDs:
            tests = [cache.get(testID) for testID in testIDs]
        else: tests=None
        if tests:
            tests = sorted(tests, key=lambda x: x['EndDateTime'])
        
        # Get the dates
        dates = [(datetime.now().date() - timedelta(days=i)) for i in range(6, -1, -1)]

        # Create the initial data
        data = [{'id':i, 'Date': dates[i], 'Correct':None, 'Incorrect':None} for i in range(7)]

        if tests:
            id = 0
            for test in tests:
                date = test['EndDateTime'].date()
                incorrect_count = test['status'].count(False)
                correct_count = test['status'].count(True)

                while data[id]['Date'] < date:
                    id += 1
                if data[id]['Correct'] == None:
                    data[id]['Correct'] = correct_count
                else:
                    data[id]['Correct'] = int(data[id]['Correct']) + int(correct_count)
                
                if data[id]['Incorrect'] == None:
                    data[id]['Incorrect'] = incorrect_count
                else:
                    data[id]['Incorrect'] = int(data[id]['Incorrect']) + int(incorrect_count)
                
        for id, elem in enumerate(data):
            if elem['Correct'] == None:
                elem['Correct'] = 0
            if elem['Incorrect'] == None:
                elem['Incorrect'] = 0

        return Response(data=data, status=status.HTTP_200_OK)

class homeModalView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def obtain_tests_and_testIDs(self, username, date):
        # Obtain tests and test IDs filtered to the date specified
        RAWTestIDs = cache.get(key=username)
        if RAWTestIDs:
            RAWTests = [(cache.get(RAWTestIDs), RAWTestIDs) for RAWTestIDs in RAWTestIDs]
        else:
            RAWTests=None

        tests, testIDs = [], []
        if RAWTests:
            for RAWtest in RAWTests:
                if str(RAWtest[0]['EndDateTime'].date()) == date:
                    tests.append(RAWtest[0])
                    testIDs.append(RAWtest[1])
        return tests, testIDs
    
    def post(self, request):
        data = request.data
        date = data['date']
        tests, testIDs = self.obtain_tests_and_testIDs(request.user.username, date)

        class Results:
            def __init__(self):
                self.TestID =  ''
                self.Test = [{
                    'Language': [],
                    'Base': [],
                    'Tense': [],
                    'IDs':  [],
                    'Ranks': [],
                    'Subjects': [],
                    'Auxiliaries': [],
                    'Conjugations': [],
                    'Answers': [],
                    'Status': [],
                }]

        results = []
        for i in range(len(tests)):
            results.append(Results())

        for i, test in enumerate(tests):
            results[i].TestID = str(testIDs[i])
            for index, item in enumerate(test['status']):
                if len(results[i].Test[0]['IDs']) == 0:
                    formated_json = {
                        'Language': test['languages'][index],
                        'Base': test['bases'][index],
                        'Tense':test['tenses'][index],
                        'IDs': [test['pks'][index]],
                        'Ranks':[test['ranks'][index]],
                        'Subjects':[test['subjects'][index]],
                        'Auxiliaries':[test['auxiliaries'][index]],
                        'Conjugations':[test['conjugations'][index]],
                        'Answers':[test['answers'][index]],
                        'Status': [item]
                    }
                    results[i].Test[0] = formated_json
                else:
                    if test['tenses'][index] == results[i].Test[-1]['Tense'] and test['bases'][index] == results[i].Test[-1]['Base']:
                        results[i].Test[-1]['IDs'].append(test['pks'][index])
                        results[i].Test[-1]['Ranks'].append(test['ranks'][index])
                        results[i].Test[-1]['Subjects'].append(test['subjects'][index])
                        results[i].Test[-1]['Auxiliaries'].append(test['auxiliaries'][index])
                        results[i].Test[-1]['Conjugations'].append(test['conjugations'][index])
                        results[i].Test[-1]['Answers'].append(test['answers'][index])
                        results[i].Test[-1]['Status'].append(item)
                    else:
                        results[i].Test.append({
                            'Language': test['languages'][index],
                            'Base': test['bases'][index],
                            'Tense':test['tenses'][index],
                            'IDs': [test['pks'][index]],
                            'Ranks':[test['ranks'][index]],
                            'Subjects':[test['subjects'][index]],
                            'Auxiliaries':[test['auxiliaries'][index]],
                            'Conjugations':[test['conjugations'][index]],
                            'Answers':[test['answers'][index]],
                            'Status': [item]
                        })

        for i in range(len(results)):
            results[i] = results[i].__dict__

        return Response(data=results, status=status.HTTP_200_OK)





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