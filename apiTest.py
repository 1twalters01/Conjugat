import requests

def getRoutesTest(token):
    # token = "e93ef372be1e80dc1fece644c554742bf3437954"
    # auth = "Token " + token
    h = {"Authorization":"Token " + token}
    d = ""
    url = "http://conjugat.io:8000/account/"
    r = requests.get(url, headers=h, data=d).json()
    return r

def loginViewTest():
    h = ""
    d = {"username":"admin", "password":"admin"}
    url = "http://conjugat.io:8000/account/login/"
    r = requests.post(url, headers=h, data=d).json()
    return r

def logoutViewTest(token):
    h = {"Authorization":"Token " + token}
    d = ""
    url = "http://conjugat.io:8000/account/logout/"
    r = requests.get(url, headers=h, data=d).json()
    return r



get_access = loginViewTest()
print(get_access)
print(getRoutesTest(get_access['token']))
print(logoutViewTest(get_access['token']))