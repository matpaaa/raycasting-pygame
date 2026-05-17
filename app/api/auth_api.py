import requests
from app.api.api_config import *

class AuthApi:
    
    @staticmethod
    def login(data):
        res = requests.post(f'{API_URL}api/login', json=data)
        return res
    
    @staticmethod
    def logout():
        res = requests.post(f'{API_URL}api/logout')
        return res
    
    @staticmethod
    def register(data):
        res = requests.post(f'{API_URL}api/register', json=data)
        return res
    
    @staticmethod
    def verify_code(data):
        res = requests.post(f'{API_URL}api/verify-code', json=data)
        return res