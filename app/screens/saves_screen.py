import pygame
from app.constants.assets import *
from app.ui.button import *
from app.constants.settings import *
import app._utils.global_var as global_var
from app.api.auth_api import *
from app.services.save_service import *
import threading
from app._utils.sounds import *

class SavesScreen:

    def __init__(self, screen):
        self.screen = screen
        self.disconnect_btn = Button(
            'DECONNEXION',
            SCREEN_WIDTH - ELEMENT_WIDTH_SMALL - SCREEN_PADDING,
            64,
            ELEMENT_WIDTH_SMALL,
            ELEMENT_HEIGHT,
            'danger'
        )
        
        self.delete_save_btn = Button(
            'Supprimer',
            SCREEN_WIDTH//2-ELEMENT_WIDTH_SMALL//2,
            SCREEN_HEIGHT // 2 + SCREEN_PADDING + ELEMENT_HEIGHT,
            ELEMENT_WIDTH_SMALL,
            ELEMENT_HEIGHT,
            'danger'
        )
        
        self.create_save_btn = Button(
            "Créer une partie",
            SCREEN_WIDTH//2-ELEMENT_WIDTH_LARGE//2,
            SCREEN_HEIGHT-SCREEN_PADDING-ELEMENT_HEIGHT,
            ELEMENT_WIDTH_LARGE,
            ELEMENT_HEIGHT,
        )

        self.arrow_left_rect = pygame.Rect(
            23,
            SCREEN_HEIGHT // 2 - Assets.arrow_left.get_height() // 2,
            Assets.arrow_left.get_width(),
            Assets.arrow_left.get_height()
        )
        self.arrow_right_rect = pygame.Rect(
            SCREEN_WIDTH - 23 - Assets.arrow_right.get_width(),
            SCREEN_HEIGHT // 2 - Assets.arrow_right.get_height() // 2,
            Assets.arrow_right.get_width(),
            Assets.arrow_right.get_height()
        )

        self.start_game_x = SCREEN_WIDTH // 2 - Assets.start_game.get_width() // 2
        self.start_game_y = SCREEN_HEIGHT // 2 - Assets.start_game.get_height() // 2
        self.start_game_rect = pygame.Rect(
            self.start_game_x,
            self.start_game_y,
            Assets.start_game.get_width(),
            Assets.start_game.get_height()
        )

        self.current_index = 0
        self.saves = []

        self.font_title = pygame.font.SysFont(None, 36)
        self.font_info  = pygame.font.SysFont(None, 26)

    # ------------------------------------------------------------------
    # Chargement des saves
    # ------------------------------------------------------------------

    def _load_saves(self):
        if len(self.saves) > 0: return
        saves = global_var.save_store.saves
        self.saves = saves if saves else []
        max_index = len(self.saves)
        self.current_index = min(self.current_index, max_index)

    # ------------------------------------------------------------------
    # Propriétés de commodité
    # ------------------------------------------------------------------

    @property
    def _total_slots(self):
        return 1 + len(self.saves)

    @property
    def _is_new_game_selected(self):
        return self.current_index == 0

    @property
    def _selected_save(self):
        if self._is_new_game_selected:
            return None
        return self.saves[self.current_index - 1]
    
    def create_save_async(self):
        global_var.navigatePage('loading')
        thread = threading.Thread(target=create_save)
        thread.start()
        
    def load_save_async(self):
        global_var.navigatePage('loading')
        save = self._selected_save
        thread = threading.Thread(target=load_save, args=(save['id_save'],))
        thread.start()
    # ------------------------------------------------------------------
    # Événements
    # ------------------------------------------------------------------

    def handle_event(self, event):
        if event.type != pygame.MOUSEBUTTONDOWN or event.button != 1:
            return

        if self.arrow_left_rect.collidepoint(event.pos):
            self.current_index = (self.current_index - 1) % self._total_slots

        elif self.arrow_right_rect.collidepoint(event.pos):
            self.current_index = (self.current_index + 1) % self._total_slots
            
        elif self.create_save_btn.is_clicked(event):
            Sounds.click()
            self.create_save_async()
            
        elif self.delete_save_btn.is_clicked(event):
            if self._selected_save:
                Sounds.click()
                delete_save(self._selected_save['id_save'])
                self.saves = []

        elif self.start_game_rect.collidepoint(event.pos):
            Sounds.click()
            if self._is_new_game_selected:
                self.create_save_async()
            else:   
                self.load_save_async()

        # Bouton déconnexion
        elif self.disconnect_btn.is_clicked(event):
            res = AuthApi.logout()
            if res.status_code == 200:
                global_var.navigatePage('login')

    # ------------------------------------------------------------------
    # Rendu
    # ------------------------------------------------------------------

    def draw(self):
        self._load_saves()
        self.screen.fill((0, 0, 0))
        self.screen.blit(Assets.background, (0, 0))
        self.screen.blit(Assets.screen_title, (100, 64))
        self.disconnect_btn.draw(self.screen)

        left_alpha  = 255 if self._total_slots > 1 else 80
        right_alpha = 255 if self._total_slots > 1 else 80
        arrow_left  = Assets.arrow_left.copy()
        arrow_right = Assets.arrow_right.copy()
        arrow_left.set_alpha(left_alpha)
        arrow_right.set_alpha(right_alpha)
        self.screen.blit(arrow_left,  (self.arrow_left_rect.x,  self.arrow_left_rect.y))
        self.screen.blit(arrow_right, (self.arrow_right_rect.x, self.arrow_right_rect.y))

        self._draw_dots()
        self.create_save_btn.draw(self.screen)

        if self._is_new_game_selected:
            self.screen.blit(Assets.start_game, (self.start_game_x, self.start_game_y))
        else:
            self._draw_save_card(self._selected_save)

    def _draw_dots(self):
        dot_radius = 6
        spacing    = 20
        total_w    = self._total_slots * spacing
        start_x    = SCREEN_WIDTH // 2 - total_w // 2
        y          = SCREEN_HEIGHT // 2 + Assets.start_game.get_height() // 2 + 30

        for i in range(self._total_slots):
            color = (255, 255, 255) if i == self.current_index else (100, 100, 100)
            pygame.draw.circle(self.screen, color, (start_x + i * spacing, y), dot_radius)

    def _draw_save_card(self, save):
        card_w, card_h = 320, 180
        card_x = SCREEN_WIDTH  // 2 - card_w // 2
        card_y = SCREEN_HEIGHT // 2 - card_h // 2 - 40

        card_surf = pygame.Surface((card_w, card_h), pygame.SRCALPHA)
        card_surf.fill((0, 0, 0, 160))
        self.screen.blit(card_surf, (card_x, card_y))
        pygame.draw.rect(self.screen, (200, 200, 100), (card_x, card_y, card_w, card_h), 2, border_radius=8)

        def _get(key):
            return save[key] if isinstance(save, dict) else getattr(save, key, '?')

        save_id  = _get('id_save')
        duration = _get('duration')
        is_win   = _get('is_win')
        is_fail  = _get('is_failed')
        created  = str(_get('created_at'))[:10]

        if is_win:
            status, status_color = 'Victoire', (100, 255, 100)
        elif is_fail:
            status, status_color = 'Échec',    (255, 80,  80)
        else:
            status, status_color = 'En cours', (255, 200, 50)

        padding = 16
        line_h  = 30

        title_surf = self.font_title.render(f'Sauvegarde #{save_id}', True, (255, 255, 255))
        self.screen.blit(title_surf, (card_x + padding, card_y + padding))

        infos = [
            (f'Durée : {duration}s',  (200, 200, 200)),
            (f'Créée : {created}',    (200, 200, 200)),
            (status,                   status_color),
        ]
        for i, (text, color) in enumerate(infos):
            surf = self.font_info.render(text, True, color)
            self.screen.blit(surf, (card_x + padding, card_y + padding + 36 + i * line_h))

        slot_surf = self.font_info.render(
            f'{self.current_index}/{len(self.saves)}', True, (160, 160, 160)
        )
        self.screen.blit(slot_surf, (
            card_x + card_w - slot_surf.get_width() - padding,
            card_y + padding
        ))
        self.delete_save_btn.draw(self.screen)