from cryptography.fernet import Fernet
from django.conf import settings


key = settings.ENCRYPTION_KEY

def encrypt(token):
    f = Fernet(key)
    token = token.encode('ascii')
    token = f.encrypt(token).decode('ascii')
    token = token.lstrip("b'").rstrip("'")
    token = token.replace("=", "%")
    return token

def decrypt(token):
    f = Fernet(key)
    token = token.replace("%", "=")
    token = token.encode('ascii')
    token = f.decrypt(token).decode('ascii')
    return token