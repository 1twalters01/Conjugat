from django.core.exceptions import ValidationError

def validate_email(data):
    email = data['email'].strip()
    if not email:
        raise ValidationError('No email provided')
    return True

def validate_username(data):
    username = data['username'].strip()
    if not username:
        raise ValidationError('No username provided')
    return True

def validate_password(data):
    password = data['password'].strip()
    if not password:
        raise ValidationError('No password provided')
    return True

def validate_new_passwords(data):
    newPassword1 = data['newPassword1'].strip()
    newPassword2 = data['newPassword2'].strip()
    if not newPassword1 or not newPassword2:
        raise ValidationError('Provide all fields')
    if newPassword1 != newPassword2:
         raise ValidationError('Passwords must match')
    return True

def validate_first_name(data):
    first_name = data['first_name'].strip()
    if not first_name:
        raise ValidationError('No first name provided')
    return True

def validate_choice(data):
    choice = data['choice'].strip()
    if not choice:
        raise ValidationError('No theme provided')
    return True