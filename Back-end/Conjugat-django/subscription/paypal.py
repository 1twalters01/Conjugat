from django.conf import settings
import requests

def get_access_token():
    client_id = settings.PAYPAL_CLIENT_ID
    secret_id = settings.PAYPAL_SECRET_KEY
    user = (client_id, secret_id)

    url = 'https://api-m.sandbox.paypal.com/v1/oauth2/token'
    header = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {'grant_type': 'client_credentials'}
    
    request = requests.post(url, auth=user, headers=header, data=data).json()
    return request['access_token']


def show_sub_details(subscription_id):
    url = 'https://api-m.sandbox.paypal.com/v1/billing/subscriptions/' + subscription_id
    header = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + get_access_token()
    }

    request = requests.get(url, headers=header).json()
    return request


def cancel_sub(subscription_id):
    url = 'https://api-m.sandbox.paypal.com/v1/billing/subscriptions/' + subscription_id + '/cancel'
    header = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + get_access_token()
    }
    data = {'reason': 'Not satisfied with the service'}

    request = requests.post(url, headers=header, data=data).json()
    print(request)


def suspend_sub(subscription_id, reason='Not satisfied with the service'):
    url = 'https://api-m.sandbox.paypal.com/v1/billing/subscriptions/' + subscription_id + '/suspend'
    header = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + get_access_token()
    }
    data = {'reason': reason}

    try:
        request = requests.post(url, headers=header, data=data).json()
    except:
        request = None
    if request:
        return {"success": True}
    return {"success": False}


def activate_sub(subscription_id, reason='Not satisfied with the service'): 
    url = 'https://api-m.sandbox.paypal.com/v1/billing/subscriptions/' + subscription_id + '/activate'
    header = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + get_access_token()
    }
    data = {'reason': reason}

    try:
        request = requests.post(url, headers=header, data=data).json()
    except:
        request = None
    if request:
        return {"success": True}
    return {"success": False}



#subscription_id = 'I-W0F4P2H7MDNJ'
#print(show_sub_details(subscription_id))
#suspend_sub(get_access_token(), subscription_id)
#cancel_sub(subscription_id)
#activate_sub(get_access_token(), subscription_id)
