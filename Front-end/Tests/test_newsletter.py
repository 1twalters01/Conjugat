import unittest
from http_methods import HTTP_methods
from newsletter_urls import urls

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

    def test_subscribeView(self):
        # GET
        self.assertEqual(HTTP_methods.get(urls['subscribeView']).json()['detail'], 'Authentication credentials were not provided.')
        self.assertEqual(HTTP_methods.get(urls['subscribeView'], headers={'Authorization':'Token fake0a2d09694c835ec37d15a115a7141c791417'}).json()['detail'], 'Invalid token.')
        self.assertEqual(HTTP_methods.get(urls['subscribeView'], headers={'Authorization':'Token 35290a2d09694c835ec37d15a115a7141c791417'}).json()['email'], '1twalters01@gmail.com')
        # POST
        self.assertEqual(HTTP_methods.post(urls['subscribeView']).json()['detail'], 'Authentication credentials were not provided.')
        self.assertEqual(HTTP_methods.post(urls['subscribeView'], headers={'Authorization':'Token fake0a2d09694c835ec37d15a115a7141c791417'}).json()['detail'], 'Invalid token.')
        self.assertEqual(HTTP_methods.post(urls['unsubscribeView'], headers={'Authorization':'Token 35290a2d09694c835ec37d15a115a7141c791417'}).json()['error'], 'No email provided')
        self.assertEqual(HTTP_methods.post(urls['unsubscribeView'], headers={'Authorization':'Token 35290a2d09694c835ec37d15a115a7141c791417'}, data={'email':'1twalters01@gmail.com'}).json()['error'], 'No first name provided')
        self.assertEqual(HTTP_methods.post(urls['unsubscribeView'], headers={'Authorization':'Token 35290a2d09694c835ec37d15a115a7141c791417'}, data={'email':'1twalters01@gmail.com', 'first_name':'Tyler'}).json()['error'], 'Email already on list')
        self.assertEqual(HTTP_methods.post(urls['unsubscribeView'], headers={'Authorization':'Token 35290a2d09694c835ec37d15a115a7141c791417'}, data={'email':'twalters1234579@gmail.com', 'first_name':'Tyler'}).json()['success'], 'Successfully subscribed to the newsletter')
        # Disallowed methods
        self.assertEqual(str(HTTP_methods.head(urls['subscribeView'])), '<Response [405]>')
        self.assertEqual(str(HTTP_methods.put(urls['subscribeView'])), '<Response [405]>')
        self.assertEqual(str(HTTP_methods.delete(urls['subscribeView'])), '<Response [405]>')
        self.assertEqual(str(HTTP_methods.options(urls['subscribeView'])), '<Response [200]>')
        self.assertEqual(str(HTTP_methods.patch(urls['subscribeView'])), '<Response [405]>')


    def test_unsubscribeView(self):
        self.assertEqual(HTTP_methods.post(urls['unsubscribeView']).json()['detail'], 'Authentication credentials were not provided.')
        self.assertEqual(HTTP_methods.post(urls['unsubscribeView'], headers={'Authorization':'Token fake0a2d09694c835ec37d15a115a7141c791417'}).json()['detail'], 'Invalid token.')
        self.assertEqual(HTTP_methods.post(urls['unsubscribeView'], headers={'Authorization':'Token 35290a2d09694c835ec37d15a115a7141c791417'}).json()['error'], 'No email provided')
        self.assertEqual(HTTP_methods.post(urls['unsubscribeView'], headers={'Authorization':'Token 35290a2d09694c835ec37d15a115a7141c791417'}, data={'email': 'invalidEmail@gmail.com'}).json(), 'invalid email')
        self.assertEqual(HTTP_methods.post(urls['unsubscribeView'], headers={'Authorization':'Token 35290a2d09694c835ec37d15a115a7141c791417'}, data={'email': '1twalters01@gmail.com'}).json(), 'Successfully unsubscribed from the newsletter')
        # Disallowed methods
        self.assertEqual(str(HTTP_methods.head(urls['unsubscribeView'])), '<Response [405]>')
        self.assertEqual(str(HTTP_methods.get(urls['unsubscribeView'])), '<Response [405]>')
        self.assertEqual(str(HTTP_methods.put(urls['unsubscribeView'])), '<Response [405]>')
        self.assertEqual(str(HTTP_methods.delete(urls['unsubscribeView'])), '<Response [405]>')
        self.assertEqual(str(HTTP_methods.options(urls['unsubscribeView'])), '<Response [200]>')
        self.assertEqual(str(HTTP_methods.patch(urls['unsubscribeView'])), '<Response [405]>')

if __name__ == '__main__':
    unittest.main()