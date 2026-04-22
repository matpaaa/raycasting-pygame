from sprite.sprite import *

class EnemieSprite(Sprite):

    def __init__(self, x, y, image, pv, damage: int):
        super().__init__(x, y, image)

        self.pv = pv
        self.damage = damage

    def attack(self, user):
        user.damage(self.damage)

    def receive_damage(self, dmg):
        if self.pv - dmg <= 0:
            self.pv = 0
            super().set_image('./assets/game/pnj/zombie-dead-pnj.png')
        else:
            self.pv -= dmg

    @property
    def is_dead(self):
        return self.pv == 0