from app.api.api_config import *

class UserApi:
    
    @staticmethod
    def me():
        res = session.get(f'{API_URL}api/me')
        return res.json()
    
    @staticmethod
    def get_maps():
        res = session.get(f'{API_URL}api/maps')
        return res.json()
    
    @staticmethod
    def delete_account(data):
        return session.delete(f'{API_URL}api/account', json=data)