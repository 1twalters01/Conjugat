import unittest
from http_methods import HTTP_methods
from account_urls import urls

class TestAccountApi(unittest.TestCase):

    def test_getRoutes(self):
        self.assertEqual(str(HTTP_methods.get(urls['getRoutes'])), '<Response [200]>')
        self.assertEqual(str(HTTP_methods.get(urls['getRoutes'], headers = {"test":"test"})), '<Response [200]>')
        self.assertEqual(str(HTTP_methods.get(urls['getRoutes'], data = {"data":"data"})), '<Response [200]>')
        self.assertEqual(str(HTTP_methods.get(urls['getRoutes'], headers = {"test":"test"}, data = {"":""})), '<Response [200]>')
         #Disallowed methods
        self.assertEqual(str(HTTP_methods.head(urls['getRoutes'])), '<Response [405]>')
        self.assertEqual(str(HTTP_methods.post(urls['getRoutes'])), '<Response [405]>')
        self.assertEqual(str(HTTP_methods.put(urls['getRoutes'])), '<Response [405]>')
        self.assertEqual(str(HTTP_methods.delete(urls['getRoutes'])), '<Response [405]>')
        self.assertEqual(str(HTTP_methods.options(urls['getRoutes'])), '<Response [200]>')
        self.assertEqual(str(HTTP_methods.patch(urls['getRoutes'])), '<Response [405]>')

    def test_loginUsernameView(self):
        self.assertEqual(HTTP_methods.post(urls['loginUsernameView']).json()['error'], 'No username was entered')
        self.assertEqual(str(HTTP_methods.post(urls['loginUsernameView'], data={"username":"lgyhglh"})), '<Response [400]>')
        self.assertEqual(HTTP_methods.post(urls['loginUsernameView'], data={"username":"lgyhglh"}).json()['error'], 'Username is not recognised')
        self.assertEqual(str(HTTP_methods.post(urls['loginUsernameView'], data={"username":"unverified"})), '<Response [400]>')
        self.assertEqual(HTTP_methods.post(urls['loginUsernameView'], data={"username":"unverified"}).json()['error'], 'User is not activated')
        self.assertEqual(HTTP_methods.post(urls['loginUsernameView'], headers={"a":"b"}, data={"username":"unverified"}).json()['error'], 'User is not activated')
        self.assertEqual(HTTP_methods.post(urls['loginUsernameView'], data={"username":"admin"}).json(), {'username': 'admin', 'uid': 2, 'confirmed': None})
        self.assertEqual(HTTP_methods.post(urls['loginUsernameView'], data={"username":"1twalters01@gmail.com"}).json(), {'username': 'admin', 'uid': 2, 'confirmed': None})
         #Disallowed methods
        self.assertEqual(str(HTTP_methods.get(urls['loginUsernameView'])), '<Response [405]>')
        self.assertEqual(str(HTTP_methods.head(urls['loginUsernameView'])), '<Response [405]>')
        self.assertEqual(str(HTTP_methods.put(urls['loginUsernameView'])), '<Response [405]>')
        self.assertEqual(str(HTTP_methods.delete(urls['loginUsernameView'])), '<Response [405]>')
        self.assertEqual(str(HTTP_methods.options(urls['loginUsernameView'])), '<Response [200]>')
        self.assertEqual(str(HTTP_methods.patch(urls['loginUsernameView'])), '<Response [405]>')


    def test_loginPasswordVieww(self):
        self.assertEqual(str(HTTP_methods.post(urls['loginPasswordView']).json()['error']), 'No username provided')
        self.assertEqual(str(HTTP_methods.post(urls['loginPasswordView'], data={'username': 'admin', 'uid': 'admin'}).json()['error']), 'User id must be an integer')
        self.assertEqual(str(HTTP_methods.post(urls['loginPasswordView'], data={'username': 'admin', 'uid': 2}).json()['error']), 'No password provided')
        self.assertEqual(str(HTTP_methods.post(urls['loginPasswordView'], data={'username': 'admin', 'uid': 2, 'password':'wrong password'}).json()['error']), 'No totp status provided')
        self.assertEqual(str(HTTP_methods.post(urls['loginPasswordView'], data={'username': 'admin', 'uid': 2, 'password':'wrong password', 'confirmed':'something'}).json()['error']), 'totp status must be a boolean')
        self.assertEqual(str(HTTP_methods.post(urls['loginPasswordView'], data={'username': 'admin', 'uid': 2, 'password':'admin', 'confirmed':True}).json()['error']), 'The totp is incorrect')
        self.assertEqual(str(HTTP_methods.post(urls['loginPasswordView'], data={'username': 'admin','uid': 3, 'password':'admin', 'confirmed':True}).json()['error']), 'uid is not found')
        self.assertEqual(str(HTTP_methods.post(urls['loginPasswordView'], data={'username': 'admin','uid': 2, 'password':'admin', 'confirmed':True, 'totp': '8799942'}).json()['error']), 'The totp is incorrect')
        self.assertEqual(str(HTTP_methods.post(urls['loginPasswordView'], data={'username': 'admin','uid': 2, 'password':'admin', 'confirmed':True, 'totp': '491484'}).json().keys()), "dict_keys(['token'])")
        #Disallowed methods
        self.assertEqual(str(HTTP_methods.get(urls['loginPasswordView'])), '<Response [405]>')
        self.assertEqual(str(HTTP_methods.head(urls['loginPasswordView'])), '<Response [405]>')
        self.assertEqual(str(HTTP_methods.put(urls['loginPasswordView'])), '<Response [405]>')
        self.assertEqual(str(HTTP_methods.delete(urls['loginPasswordView'])), '<Response [405]>')
        self.assertEqual(str(HTTP_methods.options(urls['loginPasswordView'])), '<Response [200]>')
        self.assertEqual(str(HTTP_methods.patch(urls['loginPasswordView'])), '<Response [405]>')

    def test_logoutView(self):
        self.assertEqual(str(HTTP_methods.post(urls['logoutView']).json()['detail']), 'Authentication credentials were not provided.')
        self.assertEqual(str(HTTP_methods.post(urls['logoutView'], headers={'Authorization':'Token f3aa8f2f2bc993069d0ca86f8f4bc50287d69ee7'}).json()['detail']), 'Invalid token.')
        self.assertEqual(str(HTTP_methods.post(urls['logoutView'], headers={'Authorization':'Token c3aa8f2f2bc993069d0ca86f8f4bc50287d69ee7'})), '<Response [200]>')
        self.assertEqual(str(HTTP_methods.get(urls['logoutView'])), '<Response [405]>')
        self.assertEqual(str(HTTP_methods.head(urls['logoutView'])), '<Response [405]>')
        self.assertEqual(str(HTTP_methods.put(urls['logoutView'])), '<Response [405]>')
        self.assertEqual(str(HTTP_methods.delete(urls['logoutView'])), '<Response [405]>')
        self.assertEqual(str(HTTP_methods.options(urls['logoutView'])), '<Response [200]>')
        self.assertEqual(str(HTTP_methods.patch(urls['logoutView'])), '<Response [405]>')

    # def test_registerView(self):
    #     self.assertEqual(str(HTTP_methods.get(urls['registerView'])), '<Response [405]>')
    #     self.assertEqual(str(HTTP_methods.head(urls['registerView'])), '<Response [405]>')
    #     self.assertEqual(str(HTTP_methods.post(urls['registerView'])), '<Response [405]>')
    #     self.assertEqual(str(HTTP_methods.put(urls['registerView'])), '<Response [405]>')
    #     self.assertEqual(str(HTTP_methods.delete(urls['registerView'])), '<Response [405]>')
    #     self.assertEqual(str(HTTP_methods.options(urls['registerView'])), '<Response [200]>')
    #     self.assertEqual(str(HTTP_methods.patch(urls['registerView'])), '<Response [405]>')

    # def test_activateView(self):
    #     self.assertEqual(str(HTTP_methods.get(urls['activateView'])), '<Response [405]>')
    #     self.assertEqual(str(HTTP_methods.head(urls['activateView'])), '<Response [405]>')
    #     self.assertEqual(str(HTTP_methods.post(urls['activateView'])), '<Response [405]>')
    #     self.assertEqual(str(HTTP_methods.put(urls['activateView'])), '<Response [405]>')
    #     self.assertEqual(str(HTTP_methods.delete(urls['activateView'])), '<Response [405]>')
    #     self.assertEqual(str(HTTP_methods.options(urls['activateView'])), '<Response [200]>')
    #     self.assertEqual(str(HTTP_methods.patch(urls['activateView'])), '<Response [405]>')

    # def test_passwordResetView(self):
    #     self.assertEqual(str(HTTP_methods.get(urls['passwordResetView'])), '<Response [405]>')
    #     self.assertEqual(str(HTTP_methods.head(urls['passwordResetView'])), '<Response [405]>')
    #     self.assertEqual(str(HTTP_methods.post(urls['passwordResetView'])), '<Response [405]>')
    #     self.assertEqual(str(HTTP_methods.put(urls['passwordResetView'])), '<Response [405]>')
    #     self.assertEqual(str(HTTP_methods.delete(urls['passwordResetView'])), '<Response [405]>')
    #     self.assertEqual(str(HTTP_methods.options(urls['passwordResetView'])), '<Response [200]>')
    #     self.assertEqual(str(HTTP_methods.patch(urls['passwordResetView'])), '<Response [405]>')

    # def test_passwordResetConfirmView(self):
    #     self.assertEqual(str(HTTP_methods.get(urls['passwordResetConfirmView'])), '<Response [405]>')
    #     self.assertEqual(str(HTTP_methods.head(urls['passwordResetConfirmView'])), '<Response [405]>')
    #     self.assertEqual(str(HTTP_methods.post(urls['passwordResetConfirmView'])), '<Response [405]>')
    #     self.assertEqual(str(HTTP_methods.put(urls['passwordResetConfirmView'])), '<Response [405]>')
    #     self.assertEqual(str(HTTP_methods.delete(urls['passwordResetConfirmView'])), '<Response [405]>')
    #     self.assertEqual(str(HTTP_methods.options(urls['passwordResetConfirmView'])), '<Response [200]>')
    #     self.assertEqual(str(HTTP_methods.patch(urls['passwordResetConfirmView'])), '<Response [405]>')

if __name__ == '__main__':
    unittest.main()