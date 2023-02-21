import unittest
from http_methods import HTTP_methods
from settings_urls import urls

class TestAccountApi(unittest.TestCase):
    # def test_getRoutes(self):
    #     self.assertEqual(str(HTTP_methods.get(urls['getRoutes'])), '<Response [200]>')
    #     self.assertEqual(str(HTTP_methods.get(urls['getRoutes'], headers = {"test":"test"})), '<Response [200]>')
    #     self.assertEqual(str(HTTP_methods.get(urls['getRoutes'], data = {"data":"data"})), '<Response [200]>')
    #     self.assertEqual(str(HTTP_methods.get(urls['getRoutes'], headers = {"test":"test"}, data = {"":""})), '<Response [200]>')
    #     # Disallowed methods
    #     self.assertEqual(str(HTTP_methods.head(urls['getRoutes'])), '<Response [405]>')
    #     self.assertEqual(str(HTTP_methods.post(urls['getRoutes'])), '<Response [405]>')
    #     self.assertEqual(str(HTTP_methods.put(urls['getRoutes'])), '<Response [405]>')
    #     self.assertEqual(str(HTTP_methods.delete(urls['getRoutes'])), '<Response [405]>')
    #     self.assertEqual(str(HTTP_methods.options(urls['getRoutes'])), '<Response [200]>')
    #     self.assertEqual(str(HTTP_methods.patch(urls['getRoutes'])), '<Response [405]>')

    # def changeEmailView(self):
        # self.assertEqual(HTTP_methods.post(urls['changeEmailView']).json()['detail'], 'Authentication credentials were not provided.')
        # self.assertEqual(HTTP_methods.post(urls['changeEmailView'], headers={'Authorization':'Token 01d40d2d327d682d8cbf73772d5078486f91874c'}).json()['error'], 'No email provided')
        # self.assertEqual(HTTP_methods.post(urls['changeEmailView'], headers={'Authorization':'Token 01d40d2d327d682d8cbf73772d5078486f91874c'}, data={'email':'twalters1234579@gmail.com'}).json()['error'], 'No password provided')
        # self.assertEqual(HTTP_methods.post(urls['changeEmailView'], headers={'Authorization':'Token 01d40d2d327d682d8cbf73772d5078486f91874c'}, data={'email':'twalters1234579@gmail.com', 'password':'aaa'}).json()['error'], 'Incorrect password')
        # self.assertEqual(HTTP_methods.post(urls['changeEmailView'], headers={'Authorization':'Token 01d40d2d327d682d8cbf73772d5078486f91874c'}, data={'email':'conjugat465@gmail.com', 'password':'adf fdadf fd'}).json()['error'], 'Email is already in use')
        # self.assertEqual(HTTP_methods.post(urls['changeEmailView'], headers={'Authorization':'Token 01d40d2d327d682d8cbf73772d5078486f91874c'}, data={'email':'1twalters01@gmail.com', 'password':'adf fdadf fd'}).json()['success'], 'Email changed successfully')
        # Disallowed methods
        # self.assertEqual(str(HTTP_methods.head(urls['getRoutes'])), '<Response [405]>')
        # self.assertEqual(str(HTTP_methods.post(urls['getRoutes'])), '<Response [405]>')
        # self.assertEqual(str(HTTP_methods.put(urls['getRoutes'])), '<Response [405]>')
        # self.assertEqual(str(HTTP_methods.delete(urls['getRoutes'])), '<Response [405]>')
        # self.assertEqual(str(HTTP_methods.options(urls['getRoutes'])), '<Response [200]>')
        # self.assertEqual(str(HTTP_methods.patch(urls['getRoutes'])), '<Response [405]>')

    def test_loginUsernameView(self):
        # self.assertEqual(HTTP_methods.post(urls['changeEmailView']).json()['detail'], 'Authentication credentials were not provided.')
        # self.assertEqual(HTTP_methods.post(urls['changeEmailView'], headers={'Authorization':'Token 01d40d2d327d682d8cbf73772d5078486f91874c'}).json()['error'], 'No email provided')
        # self.assertEqual(HTTP_methods.post(urls['changeEmailView'], headers={'Authorization':'Token 01d40d2d327d682d8cbf73772d5078486f91874c'}, data={'email':'twalters1234579@gmail.com'}).json()['error'], 'No password provided')
        # self.assertEqual(HTTP_methods.post(urls['changeEmailView'], headers={'Authorization':'Token 01d40d2d327d682d8cbf73772d5078486f91874c'}, data={'email':'twalters1234579@gmail.com', 'password':'aaa'}).json()['error'], 'Incorrect password')
        # self.assertEqual(HTTP_methods.post(urls['changeEmailView'], headers={'Authorization':'Token 01d40d2d327d682d8cbf73772d5078486f91874c'}, data={'email':'conjugat465@gmail.com', 'password':'adf fdadf fd'}).json()['error'], 'Email is already in use')
        # self.assertEqual(HTTP_methods.post(urls['changeEmailView'], headers={'Authorization':'Token 01d40d2d327d682d8cbf73772d5078486f91874c'}, data={'email':'1twalters01@gmail.com', 'password':'adf fdadf fd'}).json()['success'], 'Email changed successfully')
        # Disallowed methods
        self.assertEqual(str(HTTP_methods.head(urls['getRoutes'])), '<Response [405]>')
        self.assertEqual(str(HTTP_methods.post(urls['getRoutes'])), '<Response [405]>')
        self.assertEqual(str(HTTP_methods.put(urls['getRoutes'])), '<Response [405]>')
        self.assertEqual(str(HTTP_methods.delete(urls['getRoutes'])), '<Response [405]>')
        self.assertEqual(str(HTTP_methods.options(urls['getRoutes'])), '<Response [200]>')
        self.assertEqual(str(HTTP_methods.patch(urls['getRoutes'])), '<Response [405]>')


if __name__ == '__main__':
    unittest.main()