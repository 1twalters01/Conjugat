import unittest
from http_methods import HTTP_methods
from account_urls import urls

class TestAccountApi(unittest.TestCase):

    def test_getRoutes(self):
        self.assertEqual(str(HTTP_methods.get(urls['getRoutes'])), '<Response [200]>')
        self.assertEqual(str(HTTP_methods.get(urls['getRoutes'], headers = {"test":"test"})), '<Response [200]>')
        self.assertEqual(str(HTTP_methods.get(urls['getRoutes'], data = {"data":"data"})), '<Response [200]>')
        self.assertEqual(str(HTTP_methods.get(urls['getRoutes'], headers = {"test":"test"}, data = {"":""})), '<Response [200]>')
        self.assertEqual(str(HTTP_methods.head(urls['getRoutes'])), '<Response [405]>')
        self.assertEqual(str(HTTP_methods.post(urls['getRoutes'])), '<Response [405]>')
        self.assertEqual(str(HTTP_methods.put(urls['getRoutes'])), '<Response [405]>')
        self.assertEqual(str(HTTP_methods.delete(urls['getRoutes'])), '<Response [405]>')
        self.assertEqual(str(HTTP_methods.options(urls['getRoutes'])), '<Response [200]>')
        self.assertEqual(str(HTTP_methods.patch(urls['getRoutes'])), '<Response [405]>')

    def test_loginView(self):
        self.assertEqual(HTTP_methods.post(urls['loginView']).json()['error'], 'No username was entered')
        self.assertEqual(HTTP_methods.post(urls['loginView'], data={"username":"lgyhglh"}).json()['error'], 'Username is not recognised')
        self.assertEqual(HTTP_methods.post(urls['loginView'], data={"username":"Inauthentic"}).json()['error'], 'User is not activated')

        # self.assertEqual(str(HTTP_methods.get(urls['loginView'])), '<Response [405]>')
        # self.assertEqual(str(HTTP_methods.head(urls['loginView'])), '<Response [405]>')
        # self.assertEqual(str(HTTP_methods.put(urls['loginView'])), '<Response [405]>')
        # self.assertEqual(str(HTTP_methods.delete(urls['loginView'])), '<Response [405]>')
        # self.assertEqual(str(HTTP_methods.options(urls['loginView'])), '<Response [200]>')
        # self.assertEqual(str(HTTP_methods.patch(urls['loginView'])), '<Response [405]>')


    # def test_loginPasswordVieww(self):
    #     self.assertEqual(str(HTTP_methods.get(urls['loginPasswordView'])), '<Response [405]>')
    #     self.assertEqual(str(HTTP_methods.head(urls['loginPasswordView'])), '<Response [405]>')
    #     self.assertEqual(str(HTTP_methods.post(urls['loginPasswordView'])), '<Response [405]>')
    #     self.assertEqual(str(HTTP_methods.put(urls['loginPasswordView'])), '<Response [405]>')
    #     self.assertEqual(str(HTTP_methods.delete(urls['loginPasswordView'])), '<Response [405]>')
    #     self.assertEqual(str(HTTP_methods.options(urls['loginPasswordView'])), '<Response [200]>')
    #     self.assertEqual(str(HTTP_methods.patch(urls['loginPasswordView'])), '<Response [405]>')

    # def test_logoutView(self):
    #     self.assertEqual(str(HTTP_methods.get(urls['logoutView'])), '<Response [405]>')
    #     self.assertEqual(str(HTTP_methods.head(urls['logoutView'])), '<Response [405]>')
    #     self.assertEqual(str(HTTP_methods.post(urls['logoutView'])), '<Response [405]>')
    #     self.assertEqual(str(HTTP_methods.put(urls['logoutView'])), '<Response [405]>')
    #     self.assertEqual(str(HTTP_methods.delete(urls['logoutView'])), '<Response [405]>')
    #     self.assertEqual(str(HTTP_methods.options(urls['logoutView'])), '<Response [200]>')
    #     self.assertEqual(str(HTTP_methods.patch(urls['logoutView'])), '<Response [405]>')

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