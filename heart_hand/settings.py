DATABASE_URI = ''
SECRET_KEY = ''
SECURITY_PASSWORD_HASH = ''
SECURITY_PASSWORD_SALT = ''
SECURITY_REGISTERABLE = ''

try:
   from heart_hand.dev_settings import *
except ImportError:
   pass