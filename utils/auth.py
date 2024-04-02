import hashlib
import jwt
import string
import random
from jwt.exceptions import DecodeError
import smtplib
import asyncio
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime, timedelta

from config import *

class Auth():
    @staticmethod
    async def authPassword(password: str):
        if len(password) < 8:
            return True, "Password must be at least 8 characters"
        if len(password) > 18:
            return True, "Password must be at most 18 characters"
        if not any(char.isdigit() for char in password):
            return True, "Password must contain at least 1 number"
        if not any(char.isupper() for char in password):
            return True, "Password must contain at least 1 uppercase letter"
        if not any(char.islower() for char in password):
            return True, "Password must contain at least 1 lowercase letter"
        if not any(char in ".!@#$%^&*()_+-=" for char in password):
            return True, "Password must contain at least 1 special character"
        return False, None

    @staticmethod
    async def hash_password(password: str):
        hashed_password = hashlib.sha256(password.encode('utf-8') + SALT.encode('utf-8')).hexdigest()
        return hashed_password
    
    @staticmethod
    async def check_password(password: str, hashed_password: str):
        test_hashed_password = hashlib.sha256(password.encode('utf-8') + SALT.encode('utf-8')).hexdigest()
        return test_hashed_password == hashed_password
    
    @staticmethod
    def create_access_token(data: dict):
        expire = datetime.utcnow() + timedelta(hours=24)
        to_encode = data.copy()
        to_encode.update({'exp': expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm='HS256')
        return encoded_jwt

    @staticmethod
    def decode_access_token(token: str):
        try:
            decoded_jwt = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            return decoded_jwt
        except DecodeError:
            return None
        
    @staticmethod
    async def key(username: str, email: str):
        k = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(20))
        return hashlib.sha256((username + email).encode('utf-8') + k.encode('utf-8')).hexdigest()[:24]

    