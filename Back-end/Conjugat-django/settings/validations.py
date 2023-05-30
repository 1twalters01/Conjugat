from rest_framework import status

def validate_email(data):
    email = data['email'].strip()
    if not email:
        error = 'No email provided'
        return False, error, status.HTTP_400_BAD_REQUEST
    return True, 'valid'

def validate_username(data):
    username = data['username'].strip()
    if not username:
        error = 'No username provided'
        return False, error, status.HTTP_400_BAD_REQUEST
    return True, 'valid'

def validate_password(data):
    password = data['password'].strip()
    if not password:
        error = 'No password provided'
        return False, error, status.HTTP_400_BAD_REQUEST
    return True, 'valid'

def validate_totp(data, length_of_OTP):
    totp = data['totp'].strip()
    if not totp:
        error = 'No totp provided'
        return False, error, status.HTTP_400_BAD_REQUEST
    if totp.isnumeric() == False:
        error = 'totp must only contain numbers'
        return False, error, status.HTTP_400_BAD_REQUEST
    if len(totp) != length_of_OTP:
        error = 'totp must be ' + str(length_of_OTP) + ' characters long'
        return False, error, status.HTTP_400_BAD_REQUEST
    return True, 'valid'

def validate_new_passwords(data):
    newPassword1 = data['newPassword1'].strip()
    newPassword2 = data['newPassword2'].strip()
    if not newPassword1 or not newPassword2:
        error = 'Provide all fields'
        return False, error, status.HTTP_400_BAD_REQUEST
    if newPassword1 != newPassword2:
        error = 'Passwords must match'
        return False, error, status.HTTP_400_BAD_REQUEST
    return True, 'valid'

def validate_first_name(data):
    first_name = data['first_name'].strip()
    if not first_name:
        error = 'No first name provided'
        return False, error, status.HTTP_400_BAD_REQUEST
    return True, 'valid'

def validate_choice(data):
    choice = data['choice'].strip()
    if not choice:
        error = 'No value provided'
        return False, error, status.HTTP_400_BAD_REQUEST
    return True, 'valid'

def validate_header_font(data):
    choice = data['headerFont'].strip()
    if not choice:
        error = 'No value provided'
        return False, error, status.HTTP_400_BAD_REQUEST
    return True, 'valid'

def validate_body_font(data):
    choice = data['bodyFont'].strip()
    if not choice:
        error = 'No value provided'
        return False, error, status.HTTP_400_BAD_REQUEST
    return True, 'valid'

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