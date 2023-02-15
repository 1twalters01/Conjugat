import requests
from account_urls import urls

class HTTP_methods():
    def get(url, headers=None, data=None):
        return requests.get(url, headers=headers, data=data)
    def head(url, headers=None, data=None):
        return requests.head(url, headers=headers, data=data)
    def post(url, headers=None, data=None):
        return requests.post(url, headers=headers, data=data)
    def put(url, headers=None, data=None):
        return requests.put(url, headers=headers, data=data)
    def delete(url, headers=None, data=None):
        return requests.delete(url, headers=headers, data=data)
    def options(url, headers=None, data=None):
        return requests.options(url, headers=headers, data=data)
    def patch(url, headers=None, data=None):
        return requests.patch(url, headers=headers, data=data)

print(HTTP_methods.post(urls['loginView'], data={"username":"lgyhglh"}).json())