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

    # def test_changeEmailView(self):
    #     self.assertEqual(HTTP_methods.post(urls['changeEmailView']).json()['detail'], 'Authentication credentials were not provided.')
        # self.assertEqual(HTTP_methods.post(urls['changeEmailView'], headers={'Authorization':'Token 01d40d2d327d682d8cbf73772d5078486f91874c'}).json()['error'], 'No email provided')
        # self.assertEqual(HTTP_methods.post(urls['changeEmailView'], headers={'Authorization':'Token 01d40d2d327d682d8cbf73772d5078486f91874c'}, data={'email':'twalters1234579@gmail.com'}).json()['error'], 'No password provided')
        # self.assertEqual(HTTP_methods.post(urls['changeEmailView'], headers={'Authorization':'Token 01d40d2d327d682d8cbf73772d5078486f91874c'}, data={'email':'twalters1234579@gmail.com', 'password':'aaa'}).json()['error'], 'Incorrect password')
        # self.assertEqual(HTTP_methods.post(urls['changeEmailView'], headers={'Authorization':'Token 01d40d2d327d682d8cbf73772d5078486f91874c'}, data={'email':'conjugat465@gmail.com', 'password':'adf fdadf fd'}).json()['error'], 'Email is already in use')
        # self.assertEqual(HTTP_methods.post(urls['changeEmailView'], headers={'Authorization':'Token 01d40d2d327d682d8cbf73772d5078486f91874c'}, data={'email':'1twalters01@gmail.com', 'password':'adf fdadf fd'}).json()['success'], 'Email changed successfully')
        # Disallowed methods
        # self.assertEqual(str(HTTP_methods.head(urls['changeEmailView'])), '<Response [405]>')
        # self.assertEqual(str(HTTP_methods.get(urls['changeEmailView'])), '<Response [405]>')
        # self.assertEqual(str(HTTP_methods.put(urls['changeEmailView'])), '<Response [405]>')
        # self.assertEqual(str(HTTP_methods.delete(urls['changeEmailView'])), '<Response [405]>')
        # self.assertEqual(str(HTTP_methods.options(urls['changeEmailView'])), '<Response [200]>')
        # self.assertEqual(str(HTTP_methods.patch(urls['changeEmailView'])), '<Response [405]>')

    # def test_changePasswordView(self):
    #     self.assertEqual(HTTP_methods.post(urls['changePasswordView']).json()['detail'], 'Authentication credentials were not provided.')
    #     self.assertEqual(HTTP_methods.post(urls['changePasswordView'], headers={'Authorization':'Token 35290a2d09694c835ec37d15a115a7141c791417'}).json()['error'], 'No password provided')
    #     self.assertEqual(HTTP_methods.post(urls['changePasswordView'], headers={'Authorization':'Token 35290a2d09694c835ec37d15a115a7141c791417'}, data={'password':'adf fdadf fd'}).json()['error'], 'No new password provided')
    #     self.assertEqual(HTTP_methods.post(urls['changePasswordView'], headers={'Authorization':'Token 35290a2d09694c835ec37d15a115a7141c791417'}, data={'password':'adf fdadf fd', 'newPassword1':'qhwjekrlt;'}).json()['error'], 'No verification password provided')
    #     self.assertEqual(HTTP_methods.post(urls['changePasswordView'], headers={'Authorization':'Token 35290a2d09694c835ec37d15a115a7141c791417'}, data={'password':'wrongPassword', 'newPassword1':'qhwjekrlt;','newPassword2':'qhwjekrlt;'}).json()['error'], 'Incorrect password')
    #     self.assertEqual(HTTP_methods.post(urls['changePasswordView'], headers={'Authorization':'Token 35290a2d09694c835ec37d15a115a7141c791417'}, data={'password':'adf fdadf fd', 'newPassword1':'qhwjekrlt;','newPassword2':'not matching'}).json()['error'], 'Passwords do not match')
    #     self.assertEqual(HTTP_methods.post(urls['changePasswordView'], headers={'Authorization':'Token 35290a2d09694c835ec37d15a115a7141c791417'}, data={'password':'admin', 'newPassword1':'adf fdadf fd','newPassword2':'adf fdadf fd'}).json()['success'], 'Password was changed successfully')
    #     # Disallowed methods
    #     self.assertEqual(str(HTTP_methods.head(urls['changePasswordView'], headers={'Authorization':'Token 01d40d2d327d682d8cbf73772d5078486f91874c'})), '<Response [405]>')
    #     self.assertEqual(str(HTTP_methods.get(urls['changePasswordView'], headers={'Authorization':'Token 01d40d2d327d682d8cbf73772d5078486f91874c'})), '<Response [405]>')
    #     self.assertEqual(str(HTTP_methods.put(urls['changePasswordView'], headers={'Authorization':'Token 01d40d2d327d682d8cbf73772d5078486f91874c'})), '<Response [405]>')
    #     self.assertEqual(str(HTTP_methods.delete(urls['changePasswordView'], headers={'Authorization':'Token 01d40d2d327d682d8cbf73772d5078486f91874c'})), '<Response [405]>')
    #     self.assertEqual(str(HTTP_methods.options(urls['changePasswordView'], headers={'Authorization':'Token 01d40d2d327d682d8cbf73772d5078486f91874c'})), '<Response [200]>')
    #     self.assertEqual(str(HTTP_methods.patch(urls['changePasswordView'], headers={'Authorization':'Token 01d40d2d327d682d8cbf73772d5078486f91874c'})), '<Response [405]>')

    # def test_changeUsernameView(self):
    #     self.assertEqual(HTTP_methods.post(urls['changeUsernameView']).json()['detail'], 'Authentication credentials were not provided.')
    #     self.assertEqual(HTTP_methods.post(urls['changeUsernameView'], headers={'Authorization':'Token 01d40d2d327d682d8cbf73772d5078486f91874c'}).json()['error'], 'No username provided')
    #     self.assertEqual(HTTP_methods.post(urls['changeUsernameView'], headers={'Authorization':'Token 01d40d2d327d682d8cbf73772d5078486f91874c'}, data={'username':'newname'}).json()['error'], 'No password provided')
    #     self.assertEqual(HTTP_methods.post(urls['changeUsernameView'], headers={'Authorization':'Token 01d40d2d327d682d8cbf73772d5078486f91874c'}, data={'username':'newname', 'password':'aaa'}).json()['error'], 'Incorrect password')
    #     self.assertEqual(HTTP_methods.post(urls['changeUsernameView'], headers={'Authorization':'Token 01d40d2d327d682d8cbf73772d5078486f91874c'}, data={'username':'No2FA', 'password':'adf fdadf fd'}).json()['error'], 'Username is already in use')
    #     self.assertEqual(HTTP_methods.post(urls['changeUsernameView'], headers={'Authorization':'Token 01d40d2d327d682d8cbf73772d5078486f91874c'}, data={'username':'admin', 'password':'adf fdadf fd'}).json()['success'], 'Username changed successfully')
    #     # Disallowed methods
    #     self.assertEqual(str(HTTP_methods.head(urls['changeUsernameView'], headers={'Authorization':'Token 01d40d2d327d682d8cbf73772d5078486f91874c'})), '<Response [405]>')
    #     self.assertEqual(str(HTTP_methods.get(urls['changeUsernameView'], headers={'Authorization':'Token 01d40d2d327d682d8cbf73772d5078486f91874c'})), '<Response [405]>')
    #     self.assertEqual(str(HTTP_methods.put(urls['changeUsernameView'], headers={'Authorization':'Token 01d40d2d327d682d8cbf73772d5078486f91874c'})), '<Response [405]>')
    #     self.assertEqual(str(HTTP_methods.delete(urls['changeUsernameView'], headers={'Authorization':'Token 01d40d2d327d682d8cbf73772d5078486f91874c'})), '<Response [405]>')
    #     self.assertEqual(str(HTTP_methods.options(urls['changeUsernameView'], headers={'Authorization':'Token 01d40d2d327d682d8cbf73772d5078486f91874c'})), '<Response [200]>')
    #     self.assertEqual(str(HTTP_methods.patch(urls['changeUsernameView'], headers={'Authorization':'Token 01d40d2d327d682d8cbf73772d5078486f91874c'})), '<Response [405]>')

    def test_resetAccountView(self):
        pass

    def test_closeAccountView(self):
        pass

    def test_premiumView(self):
        pass

    # def test_themesView(self):
    #     self.assertEqual(HTTP_methods.post(urls['themesView']).json()['detail'], 'Authentication credentials were not provided.')
    #     self.assertEqual(HTTP_methods.post(urls['themesView'], headers={'Authorization':'Token 35290a2d09694c835ec37d15a115a7141c791417'}).json()['error'], 'No theme provided')
    #     self.assertEqual(HTTP_methods.post(urls['themesView'], headers={'Authorization':'Token 35290a2d09694c835ec37d15a115a7141c791417'}, data={'choice':'bird'}).json()['error'], 'Invalid option')
    #     self.assertEqual(HTTP_methods.post(urls['themesView'], headers={'Authorization':'Token 35290a2d09694c835ec37d15a115a7141c791417'}, data={'choice':'Light'}).json()['success'], 'Theme changed successfully')
    #     # Disallowed methods
    #     self.assertEqual(str(HTTP_methods.head(urls['themesView'], headers={'Authorization':'Token 35290a2d09694c835ec37d15a115a7141c791417'})), '<Response [405]>')
    #     self.assertEqual(str(HTTP_methods.get(urls['themesView'], headers={'Authorization':'Token 35290a2d09694c835ec37d15a115a7141c791417'})), '<Response [405]>')
    #     self.assertEqual(str(HTTP_methods.put(urls['themesView'], headers={'Authorization':'Token 35290a2d09694c835ec37d15a115a7141c791417'})), '<Response [405]>')
    #     self.assertEqual(str(HTTP_methods.delete(urls['themesView'], headers={'Authorization':'Token 35290a2d09694c835ec37d15a115a7141c791417'})), '<Response [405]>')
    #     self.assertEqual(str(HTTP_methods.options(urls['themesView'], headers={'Authorization':'Token 35290a2d09694c835ec37d15a115a7141c791417'})), '<Response [200]>')
    #     self.assertEqual(str(HTTP_methods.patch(urls['themesView'], headers={'Authorization':'Token 35290a2d09694c835ec37d15a115a7141c791417'})), '<Response [405]>')

    def twoFactorAuthView(self):
        pass

if __name__ == '__main__':
    unittest.main()