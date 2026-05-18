from app.model.save_model import *
from app.api.save_api import *
from app.store.store import InvalidStoreOptions

class SaveStore:
    save_loaded: None | SaveLoadedModel
    saves: None | SaveHomeModel
    
    def invalid_saves(self, options: InvalidStoreOptions):
        self.saves = None
        if options.refetch:
            self.hydrate_saves()
            
    def invalid_save_loaded(self, options: InvalidStoreOptions):
        self.save_loaded = None
        if options.refetch:
            self.hydrate_save_loaded()
    
    def hydrate_saves(self):
        if self.saves is None:
            self.saves = SaveApi.get_saves()
            
    def hydrate_save_loaded(self, save_id: int):
        if self.save_loaded is None:
            self.save_loaded = SaveApi.get_save(save_id)