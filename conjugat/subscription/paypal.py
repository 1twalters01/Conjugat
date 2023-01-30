from django.conf import settings
import requests

client_id = settings.PAYPAL_CLIENT_ID
secret_id = settings.PAYPAL_SECRET_KEY

def get_access_token():
    d = {'grant_type':'client_credentials'}
    h = {'Content-Type':'application/x-www-form-urlencoded'}
    u = {client_id:secret_id}
    url = 'https://api-m.sandbox.paypal.com/v1/oauth2/token'
    r = requests.post(url, auth=(client_id, secret_id), headers=h, data=d).json()
    return r['access_token']


def show_sub_details(subscription_id):
    access_token = get_access_token()
    bearer_token = 'Bearer ' + access_token
    h = {'Content-Type':'application/json',
    'Authorization':bearer_token}
    url = 'https://api-m.sandbox.paypal.com/v1/billing/subscriptions/' + subscription_id
    r = requests.get(url, headers=h).json()
    return r


def cancel_sub(subscription_id):
    access_token = get_access_token()
    bearer_token = 'Bearer ' + access_token
    h = {'Content-Type':'application/json',
    'Authorization':bearer_token}
    d = {'reason':'Not satisfied with the service'}
    url = 'https://api-m.sandbox.paypal.com/v1/billing/subscriptions/' + subscription_id + '/cancel'
    r = requests.post(url, headers=h).json()
    print(r)

def suspend_sub(subscription_id):
    access_token = get_access_token()
    bearer_token = 'Bearer ' + access_token
    h = {'Content-Type':'application/json',
    'Authorization':bearer_token}
    d = {'reason':'Not satisfied with the service'}
    url = 'https://api-m.sandbox.paypal.com/v1/billing/subscriptions/' + subscription_id + '/suspend'
    try:
        r = requests.post(url, headers=h).json()
    except:
        r = None


def activate_sub(subscription_id):
    access_token = get_access_token()
    bearer_token = 'Bearer ' + access_token
    h = {'Content-Type':'application/json',
    'Authorization':bearer_token}
    d = {'reason':'Not satisfied with the service'}
    url = 'https://api-m.sandbox.paypal.com/v1/billing/subscriptions/' + subscription_id + '/activate'
    try:
        r = requests.post(url, headers=h).json()
    except:
        r = None



#subscription_id = 'I-W0F4P2H7MDNJ'
#print(show_sub_details(subscription_id))
#suspend_sub(get_access_token(), subscription_id)
#cancel_sub(subscription_id)
#activate_sub(get_access_token(), subscription_id)