from sprite.sprite import *
from item import *
from user import *

class ObjectSprite(Sprite):

    def __init__(self, x, y, item: Item):
        super().__init__(x, y, item.image)
        self.item = item
        self.is_added = False

    def handle_interaction(self, user: User):
        if self.is_added is False:
            self.is_added = True
            user.add_item(self.item)