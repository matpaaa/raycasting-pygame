from constants.fonts import *
from settings import *

class Text:

    _positions = ('center')

    def __init__(self, text, x, y, color, font):
        self.text = text
        self.y = y
        self.color = color
        self.font = font

        self._fonts = {
            'title': Fonts.font_title,
            'subtitle': Fonts.font_subtitle,
            'btn': Fonts.font_btn,
        }

        if isinstance(x, str):
            if x in self._positions:
                self.x = x
            else:
                Exception('Postion value is invalid')
        else:
            self.x = x

        self.text_surf = self._fonts[font].render(self.text, True, color)

    def draw(self, surface):
        if isinstance(self.x, str):
            surface.blit(self.text_surf, (SCREEN_WIDTH/2 - self.text_surf.get_width()/2, self.y))
        else:
            surface.blit(self.text_surf, (self.x, self.y))
