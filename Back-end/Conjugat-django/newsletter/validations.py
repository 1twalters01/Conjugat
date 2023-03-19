from django.core.exceptions import ValidationError

def validate_email(data):
    email = data['email'].strip()
    if not email:
        raise ValidationError('No email provided')
    return True

def validate_first_name(data):
    first_name = data['first_name'].strip()
    if not first_name:
        raise ValidationError('No first name provided')
    return True