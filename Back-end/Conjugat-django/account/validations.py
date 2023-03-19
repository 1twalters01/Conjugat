from django.core.exceptions import ValidationError

def validate_username(data):
    username = data['username'].strip()
    if not username:
        raise ValidationError('No username provided')
    return True

def validate_uidb64(data):
    uidb64 = data['uidb64'].strip()
    if not uidb64:
        raise ValidationError('Invalid url type')
    return True

def validate_token(data):
    token = data['token'].strip()
    if not token:
        raise ValidationError('Invalid url type')
    return True

def validate_passwords(data):
    password = data['password'].strip()
    password2 = data['password2'].strip()
    if not password or not password2:
        raise ValidationError('Provide all fields')
    if password != password2:
         raise ValidationError('Passwords must match')
    return True