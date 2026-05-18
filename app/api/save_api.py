import requests
from app.api.api_config import *

class SaveApi:
    
    @staticmethod
    def save_player(data):
        return requests.put(f'{API_URL}api/player/save', json=data)
    
    @staticmethod
    def delete_save(data):
        return requests.delete(f'{API_URL}api/save', json=data)
    
    @staticmethod
    def create_save(data):
        return requests.post(f'{API_URL}api/create/save', json=data)
    
    @staticmethod
    def get_saves():
        res = requests.get(f'{API_URL}api/saves')
        return res.json()
    
    @staticmethod
    def get_save(save_id: int):
        res = requests.get(f'{API_URL}api/saves/{save_id}')
        return res.json()