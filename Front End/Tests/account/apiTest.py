import requests

def getRoutesTest(token, headers=None, data=None):
    url = "http://conjugat.io:8000/account/"
    r = requests.get(url, headers, data).json()
    return r

# def loginViewTest(username, password):
#     h = ""
#     d = {"username":username, "password":password}
#     url = "http://conjugat.io:8000/account/login/"
#     r = requests.post(url, headers=h, data=d).json()
#     return r

# def logoutViewTest(token):
#     h = {"Authorization":"Token " + token}
#     d = ""
#     url = "http://conjugat.io:8000/account/logout/"
#     r = requests.get(url, headers=h, data=d).json()
#     return r

# def registerViewTest(username, email, password, password2):
#     h = ""
#     d = {"username":username, "email":email, "password":password, "password2":password2}
#     url = "http://conjugat.io:8000/account/register/"
#     r = requests.put(url, headers=h, data=d).json()
#     return r


# get_access = loginViewTest("admin", "admin")
# print(get_access)
# print(getRoutesTest(get_access['token']))
# print(logoutViewTest(get_access['token']))

# print(registerViewTest("test", "tw2165582@gmail.com", "adf fdadf fd", "adf fdadf fd"))