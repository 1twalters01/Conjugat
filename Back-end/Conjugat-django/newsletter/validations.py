from rest_framework import status

def validate_email(data):
    email = data['email'].strip()
    if not email:
        error = 'No email provided'
        return False, error, status.HTTP_400_BAD_REQUEST
    return True, 'valid'

def validate_first_name(data):
    first_name = data['first_name'].strip()
    if not first_name:
        error = 'No first name provided'
        return False, error, status.HTTP_400_BAD_REQUEST
    return True, 'valid'