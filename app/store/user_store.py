from app.api.user_api import *
from app.store.store import InvalidStoreOptions

class UserStore:
    me = None
    maps = None
    
    def hydrate(self):
        self.hydrate_me()
        self.hydrate_maps()
        
    def invalid_me(self, options: InvalidStoreOptions):
        self.me = None
        if options.refetch:
            self.hydrate_me()
            
    def invalid_maps(self, options: InvalidStoreOptions):
        self.maps = None
        if options.refetch:
            self.hydrate_maps()
    
    def hydrate_me(self):
        if self.me is None:
            self.me = UserApi.me()
        
    def hydrate_maps(self):
        if self.maps is None:
            self.maps = UserApi.get_maps()