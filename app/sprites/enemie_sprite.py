from app.sprites.sprite import *

class EnemieSprite(Sprite):

    def __init__(self, x, y, image, pv, damage: int, id=None):
        super().__init__(x, y, image, id)

        self.pv = pv
        self.damage = damage
        
        if self.pv <= 0:
            self.dead()

    def attack(self, user):
        user.damage(self.damage)
        
    def dead(self):
        self.pv = 0
        super().set_image('./app/assets/game/pnj/zombie-dead-pnj.png')
        
    def receive_damage(self, dmg):
        if self.pv - dmg <= 0:
            self.pv = 0
            self.dead()
        else:
            self.pv -= dmg

    @property
    def is_dead(self):
        return self.pv == 0