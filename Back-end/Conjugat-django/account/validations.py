from rest_framework import status

def validate_username(data):
    username = data['username'].strip()
    if not username:
        error = 'No username provided'
        return False, error, status.HTTP_400_BAD_REQUEST
    return True, 'valid'

def validate_email(data):
    email = data['email'].strip()
    if not email:
        error = 'No email provided'
        return False, error, status.HTTP_400_BAD_REQUEST
    return True, 'valid'

def validate_password(data):
    password = data['password'].strip()
    if not password:
        error = 'No password provided'
        return False, error, status.HTTP_400_BAD_REQUEST
    return True, 'valid'

def validate_passwords(data):
    password = data['password'].strip()
    password2 = data['password2'].strip()
    if not password or not password2:
        error = 'No password provided'
        return False, error, status.HTTP_400_BAD_REQUEST
    if password != password2:
        error = 'Passwords must match'
        return False, error, status.HTTP_400_BAD_REQUEST
    return True, 'valid'

def validate_uidb64(data):
    uidb64 = data['uidb64'].strip()
    if not uidb64:
        error = 'Invalid url type'
        return False, error, status.HTTP_400_BAD_REQUEST
    return True, 'valid'

def validate_token(data):
    token = data['token'].strip()
    if not token:
        error = 'Invalid url type'
        return False, error, status.HTTP_400_BAD_REQUEST
    return True, 'valid'

def validate_domain(data):
    domain = data['domain'].strip()
    if not domain:
        error = 'Invalid url'
        return False, error, status.HTTP_400_BAD_REQUEST
    return True, 'valid'