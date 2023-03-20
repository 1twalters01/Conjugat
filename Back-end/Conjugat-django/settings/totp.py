import base64
import hashlib
import hmac
import math
import time
# pip install qrcode[pil] if you want to create the qrcode in python
# import qrcode
import secrets
          
def create_key_of_length(key_length=20):
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$^&*(-_=+)'
    key = ''.join(secrets.choice(chars) for i in range(key_length)).encode('ascii')
    return key
          
def generate_totp(key, length_of_OTP=6, step_in_seconds=30):
    t = math.floor(time.time() // step_in_seconds)
    hmac_object = hmac.new(key, t.to_bytes(length=8, byteorder="big"), hashlib.sha1)
    hmac_sha1 = hmac_object.hexdigest()
    offset = int(hmac_sha1[-1], 16)
    binary = int(hmac_sha1[(offset * 2):((offset * 2) + 8)], 16) & 0x7fffffff
    totp = str(binary)[-length_of_OTP:]
    return totp
          
def generate_QR_string_and_code(key, email, length_of_OTP=6, step_in_seconds=30):
    site = 'Conjugat'
    token = base64.b32encode(key)
    qr_string = "otpauth://totp/"+site+":"+email+"?secret=" + token.decode("utf-8") +"&issuer="+site+"&algorithm=SHA1&digits="+str(length_of_OTP)+"&period="+str(step_in_seconds)
    # qr_code = qrcode.make(qr_string)
    return qr_string#, qr_code

# https://pythoncircle.com/post/731/implementing-2fa-in-python-django-using-time-based-one-time-password-totp/