import requests
from app.api.api_config import *

class UserApi:
    
    @staticmethod
    def me():
        res = requests.get(f'{API_URL}api/me')
        return res.json()
    
    @staticmethod
    def get_maps():
        res = requests.get(f'{API_URL}api/maps')
        return res.json()
    
    @staticmethod
    def delete_account(data):
        return requests.delete(f'{API_URL}api/account', json=data)