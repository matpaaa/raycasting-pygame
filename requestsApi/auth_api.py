import requests
from requestsApi.api_config import *

class AuthApi:
    
    @staticmethod
    def login(data):
        res = requests.post(f'{API_URL}api/login', json=data)
        return res
    
    @staticmethod
    def register(data):
        res = requests.post(f'{API_URL}api/register', json=data)
        return res
    
    @staticmethod
    def register_verify_code(data):
        res = requests.post(f'{API_URL}api/register-verify-code', json=data)
        return res