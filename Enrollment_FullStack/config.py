import os

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or b'\x05\xb9\x01\xeaKy\xd4\xea{P\xbe\\\xb9\x1fn!'

    MONGODB_SETTINGS = { 'db': 'UTA_Enrollment'}

    