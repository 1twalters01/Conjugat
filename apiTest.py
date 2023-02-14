import requests

def registerViewTest(username, email, password, password2):
    h = ""
    d = {"username":username, "email":email, "password":password, "password2":password2}
    url = "http://conjugat.io:8000/account/register/"
    r = requests.put(url, headers=h, data=d).json()
    return r

def getRoutesTest(token):
    h = {"Authorization":"Token " + token}
    d = ""
    url = "http://conjugat.io:8000/account/"
    r = requests.get(url, headers=h, data=d).json()
    return r

def loginViewTest(username):
    h = ""
    d = {"username":username}
    url = "http://conjugat.io:8000/account/login/"
    r = requests.post(url, headers=h, data=d).json()
    return r

def loginPasswordViewTest(username, password, totp):
    h = ""
    d = {"username":username, "password":password, "totp":totp}
    url = "http://conjugat.io:8000/account/login/password/"
    r = requests.post(url, headers=h, data=d).json()
    return r

def logoutViewTest(token):
    h = {"Authorization":"Token " + token}
    d = ""
    url = "http://conjugat.io:8000/account/logout/"
    r = requests.get(url, headers=h, data=d).json()
    return r




# get_access = loginViewTest("admin", "admin")
# print(get_access)
# print(getRoutesTest(get_access['token']))
# print(logoutViewTest(get_access['token']))

print(registerViewTest("test", "tw2165582@gmail.com", "adf fdadf fd", "adf fdadf fd"))