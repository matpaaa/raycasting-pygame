from app.features.item import *
from app.constants.settings import *

class ItemFactory:
    
    @staticmethod
    def vodka():
        return Item('VODKA', 'Vodka', 0.04, 'CONSUMABLE', './app/assets/game/items/vodka.png')
    
    @staticmethod
    def canned():
        return Item('CANNED', 'Conserve', 40, 'CONSUMABLE', './app/assets/game/items/canned.png')
    
    @staticmethod
    def gun():
        return Item('GUN', 'Fusil', 50, 'WEAPON', './app/assets/game/items/gun.png')
    
    @staticmethod
    def ammo():
        return Item('AMMO', 'Munition', None, 'AMMO', './app/assets/game/items/ammo.png')
    
    @staticmethod
    def key():
        return Item('KEY', 'Clé', None, 'SECRET', './app/assets/game/items/key.png')
    
    @staticmethod
    def code(value: int):
        return Item('CODE', 'Morceau de code', value, 'SECRET', './app/assets/game/items/code.png')
    
    @staticmethod
    def battery():
        return Item('BATTERY', 'Battery', BATTERY_CAPACITY, 'ELECTRICITY', './app/assets/game/items/battery.png')