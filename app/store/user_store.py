from app.api.user_api import *
from app.store.store import InvalidStoreOptions
from app.model.me_model import *
from app.model.map_model import *

class UserStore:
    me = None | MeModel
    maps = None | MapModel
    
    def __init__(self):
        self.me = None
        self.maps = None
    
    def hydrate(self):
        self.hydrate_me()
        self.hydrate_maps()
        
    def invalid_me(self, options=None):
        if options is None:
            options = {"refetch": None}
            
        self.saves = None
            
        if options.get("refetch"):
            self.hydrate_me()
            
    def invalid_maps(self, options=None):
        if options is None:
            options = {"refetch": None}
            
        self.saves = None
            
        if options.get("refetch"):
            self.hydrate_maps()
    
    def hydrate_me(self):
        if self.me is None:
            self.me = UserApi.me()
        
    def hydrate_maps(self):
        if self.maps is None:
            self.maps = UserApi.get_maps()