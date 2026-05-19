from app.api.api_config import *

class GameApi:
    
    @staticmethod
    def drop_item(data):
        return session.put(f'{API_URL}api/drop/item', json=data)

    @staticmethod
    def recover_item(data):
        return session.post(f'{API_URL}api/recover/item', json=data)
    
    @staticmethod
    def open_door(data):
        return session.post(f'{API_URL}api/door/open', json=data)
    
    @staticmethod
    def puzzle_finish(data):
        return session.post(f'{API_URL}api/puzzle/finish', json=data)