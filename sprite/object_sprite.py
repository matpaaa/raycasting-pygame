from sprite.sprite import *
from item import *

class ObjectSprite(Sprite):

    def __init__(self, x, y, item: Item):
        super().__init__(x, y, item.image)
        self.item = item
        self.is_added = False

    def handle_interaction(self, user):
        if self.is_added is False:
            self.is_added = True
            
            self.item.add_item_inventory()
            user.add_item(self.item)