from rest_framework import status

def validate_return_urls(data):
    success_url = data['success_url'].strip()
    cancel_url = data['cancel_url'].strip()
    if not success_url or not cancel_url:
        error = 'Provide all urls'
        return False, error, status.HTTP_400_BAD_REQUEST
    return True, 'valid'

def validate_customer_id(data):
    customer_id = data['customer_id'].strip()
    if not customer_id:
        error = 'Provide all urls'
        return False, error, status.HTTP_400_BAD_REQUEST
    return True, 'valid'

def validate_subscriber_id(data):
    subscriber_id = data['subscriber_id'].strip()
    if not subscriber_id:
        error = 'Provide all urls'
        return False, error, status.HTTP_400_BAD_REQUEST
    return True, 'valid'

def validate_charge_url(data):
    charge_url = data['charge_url'].strip()
    if not charge_url:
        error = 'Provide all urls'
        return False, error, status.HTTP_400_BAD_REQUEST
    return True, 'valid'