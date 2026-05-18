import requests
from app.api.api_config import *

class OnlineApi:
    
    @staticmethod
    def active_online(data):
        return requests.post(f'{API_URL}api/save/online', json=data)
    
    @staticmethod
    def join_save(data):
        return requests.post(f'{API_URL}api/save/join', json=data)