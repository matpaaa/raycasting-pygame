from app.api.api_config import *

class SaveApi:
    
    @staticmethod
    def save_player(data):
        return session.post(f'{API_URL}api/player/save', json=data)
    
    @staticmethod
    def delete_save(data):
        return session.delete(f'{API_URL}api/delete/save', json=data)
    
    @staticmethod
    def create_save(data):
        return session.post(f'{API_URL}api/create/save', json=data)
    
    @staticmethod
    def get_saves():
        res = session.get(f'{API_URL}api/saves')
        return res.json()
    
    @staticmethod
    def get_save(save_id: int):
        res = session.get(f'{API_URL}api/save/{save_id}')
        return res.json()
    
    @staticmethod
    def active_online(data):
        res = session.post(f'{API_URL}api/save/online', json=data)
        return res.json()
    
    @staticmethod
    def join_save(data):
        return session.post(f'{API_URL}api/save/join', json=data)