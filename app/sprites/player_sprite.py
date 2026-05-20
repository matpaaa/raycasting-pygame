from app.sprites.sprite import *

class PlayerSprite(Sprite):

    def __init__(self, x, y, id=None):
        super().__init__(x, y, './app/assets/game/pnj/default-pnj.png', id)
        
    def handle_move(self, pos_x: float, pos_y: float):
        print('handle_move', pos_x, pos_y)
        self._x = pos_x
        self._y = pos_y
        self.load()