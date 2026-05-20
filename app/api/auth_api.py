import requests
from app.api.api_config import *

class AuthApi:
    
    @staticmethod
    def login(data):
        res = session.post(f'{API_URL}api/login', json=data)
        return res
    
    @staticmethod
    def logout():
        res = session.post(f'{API_URL}api/logout')
        return res
    
    @staticmethod
    def register(data):
        res = requests.post(f'{API_URL}api/register', json=data)
        return res
    
    @staticmethod
    def forgot_password(data):
        res = requests.post(f'{API_URL}api/forgot-password', json=data)
        return res
    
    @staticmethod
    def reset_password(data):
        res = requests.post(f'{API_URL}api/reset-password', json=data)
        return res
    
    @staticmethod
    def verify_code(data):
        res = requests.post(f'{API_URL}api/verify-code', json=data)
        return res
    
    @staticmethod
    def delete_account():
        res = session.delete(f'{API_URL}api/delete/account')
        return res