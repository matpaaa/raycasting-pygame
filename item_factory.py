from item import *

class ItemFactory:
    
    @staticmethod
    def vodka():
        return Item('VODKA', 'Vodka', 0.06, 'CONSUMABLE', './assets/game/items/vodka.png')
    
    @staticmethod
    def canned():
        return Item('CANNED', 'Conserve', 40, 'CONSUMABLE', './assets/game/items/canned.png')
    
    @staticmethod
    def gun():
        return Item('GUN', 'Fusil', 50, 'WEAPON', './assets/game/items/gun.png')
    
    @staticmethod
    def key(value: int):
        return Item('KEY', 'Clé', value, 'SECRET', './assets/game/items/key.png')
    
    @staticmethod
    def code(value: int):
        return Item('CODE', 'Morceau de code', value, 'SECRET', './assets/game/items/code.png')