import pygame
from app.constants.assets import *
from app.ui.button import *
from app.constants.settings import *
import app._utils.global_var as global_var
from app.api.auth_api import *
from app.services.save_service import *
import threading
from app._utils.sounds import *
from app.ui.input import Input
from app.ui.text import Text
from app.ui.error_bubble import *
from app.constants.color import *

class SavesScreen:

    def __init__(self, screen):
        self.screen = screen
        self.modal_join_save = False
        self.disconnect_btn = Button(
            'DECONNEXION',
            SCREEN_WIDTH - ELEMENT_WIDTH_SMALL - 100,
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
        
        self.join_btn = Button(
            "Rejoindre",
            SCREEN_WIDTH-ELEMENT_WIDTH_SMALL-SCREEN_PADDING,
            SCREEN_HEIGHT-SCREEN_PADDING-ELEMENT_HEIGHT,
            ELEMENT_WIDTH_SMALL,
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

        self.font_title = Fonts.font_save_title
        self.font_info  = Fonts.font_save_info
        
        self.settings_pos_x = SCREEN_WIDTH-120-ELEMENT_WIDTH_SMALL-Assets.settings.get_width()
        self.settings_pos_y = 64
        
        self.settings_rect = pygame.Rect(
            self.settings_pos_x,
            self.settings_pos_y,
            Assets.settings.get_width(),
            Assets.settings.get_height()
        )
        
        self.input_code = Input(
            'ENTRER LE CODE',
            SCREEN_WIDTH/2 - ELEMENT_WIDTH_LARGE/2,
            348,
            ELEMENT_WIDTH_LARGE,
            ELEMENT_HEIGHT
        )
        
        self.btn_back = Button(
            'BACK',
            SCREEN_WIDTH/2 - GAP_BETWEEN_ELEMENT/2 - ELEMENT_WIDTH_SMALL,
            368 + ELEMENT_HEIGHT,
            ELEMENT_WIDTH_SMALL,
            ELEMENT_HEIGHT,
            'danger'
        )

        self.btn_confirm = Button(
            'VALIDER',
            SCREEN_WIDTH/2 + GAP_BETWEEN_ELEMENT/2,
            368 + ELEMENT_HEIGHT,
            ELEMENT_WIDTH_SMALL,
            ELEMENT_HEIGHT
        )
        
        self.title = Text(
            "Rejoindre une partie",
            'center',
            224,
            WHITE,
            'title'
        )

        self.subtitle = Text(
            "Entrer le code de la partie que vous souhaiter joindre",
            'center',
            270,
            TEXT_GRAY,
            'subtitle'
        )
        
        self.error_bubble = ErrorBubble(self.screen)

    def _load_saves(self):
        if len(self.saves) > 0 and global_var.save_store.saves is not None: return
        saves = global_var.save_store.saves
        self.saves = saves if saves else []
        max_index = len(self.saves)
        self.current_index = min(self.current_index, max_index)

    @property
    def _total_slots(self):
        return 1 + len(self.saves)

    @property
    def _is_new_game_selected(self):
        return self.current_index == 0

    @property
    def _selected_save(self):
        try:
            if self._is_new_game_selected:
                return None
            return self.saves[self.current_index - 1]
        except Exception as e:
            print(e)
    
    def create_save_async(self):
        global_var.navigate_page('loading')
        create_save()
        
    def load_save_async(self):
        global_var.navigate_page('loading')
        save = self._selected_save
        load_save(save['id_save'])
        
    def join_save_async(self):
        online_code = self.input_code.value
        
        if online_code:
            try:
                int_online_code = int(online_code)
                global_var.navigate_page('loading')
                join_save(int_online_code)
            except:
                self.error_bubble.set_content('Code invalide')

    def handle_event(self, event):
        self.error_bubble.handle_event(event)
        if self.modal_join_save:
            self.input_code.handle_event(event)
        
        if event.type != pygame.MOUSEBUTTONDOWN or event.button != 1:
            return
        
        if self.join_btn.is_clicked(event):
            self.modal_join_save = True
        
        if self.btn_back.is_clicked(event) and self.modal_join_save:
            self.modal_join_save = False
            
        if self.btn_confirm.is_clicked(event) and self.modal_join_save:
            self.btn_confirm.is_loading = True
            self.join_save_async()
            self.btn_confirm.is_loading = False
            
        if self.modal_join_save: return
        
        if self.settings_rect.collidepoint(event.pos):
            Sounds.click()
            global_var.navigate_page('settings')

        if self.arrow_left_rect.collidepoint(event.pos):
            Sounds.click()
            self.current_index = (self.current_index - 1) % self._total_slots

        elif self.arrow_right_rect.collidepoint(event.pos):
            Sounds.click()
            self.current_index = (self.current_index + 1) % self._total_slots
            
        elif self.create_save_btn.is_clicked(event):
            self.create_save_btn.is_loading = True
            Sounds.click()
            self.create_save_async()
            self.saves = []
            self.create_save_btn.is_loading = False
            
        elif self.delete_save_btn.is_clicked(event):
            self.delete_save_btn.is_loading = True
            if self._selected_save:
                Sounds.click()
                try:
                    delete_save(self._selected_save['id_save'])
                    self.saves = []
                except:
                    self.error_bubble.set_content("Erreur lors de la suppression d'une sauvegarde")
            self.delete_save_btn.is_loading = False

        elif self.start_game_rect.collidepoint(event.pos):
            Sounds.click()
            if self._is_new_game_selected:
                self.create_save_async()
                self.saves = []
            elif not self._selected_save['is_win'] and not self._selected_save['is_failed']: 
                self.load_save_async()
                self.saves = []

        elif self.disconnect_btn.is_clicked(event):
            self.disconnect_btn.is_loading = True
            res = AuthApi.logout()
            global_var.save_store.invalid_save_loaded()
            global_var.save_store.invalid_saves()
            global_var.user_store.invalid_maps()
            global_var.user_store.invalid_me()
            self.saves = []
            if res.status_code == 200:
                global_var.navigate_page('login')
            self.disconnect_btn.is_loading = False

    def draw(self):
        thread = threading.Thread(target=self._load_saves)
        thread.start()
        self.screen.fill((0, 0, 0))
        self.screen.blit(Assets.background, (0, 0))
        self.screen.blit(Assets.screen_title, (100, 64))
        self.screen.blit(Assets.settings, (SCREEN_WIDTH-120-ELEMENT_WIDTH_SMALL-Assets.settings.get_width(), 64))
        self.disconnect_btn.draw(self.screen)

        left_alpha  = 255 if self._total_slots > 1 else 80
        right_alpha = 255 if self._total_slots > 1 else 80
        arrow_left  = Assets.arrow_left.copy()
        arrow_right = Assets.arrow_right.copy()
        arrow_left.set_alpha(left_alpha)
        arrow_right.set_alpha(right_alpha)
        self.screen.blit(arrow_left,  (self.arrow_left_rect.x,  self.arrow_left_rect.y))
        self.screen.blit(arrow_right, (self.arrow_right_rect.x, self.arrow_right_rect.y))
        self.join_btn.draw(self.screen)
        
        self._draw_dots()
        self.create_save_btn.draw(self.screen)

        if self._is_new_game_selected:
            self.screen.blit(Assets.start_game, (self.start_game_x, self.start_game_y))
        elif self._selected_save:
            self._draw_save_card(self._selected_save)
            
        if self.modal_join_save:
            self.screen.blit(Assets.window, ((SCREEN_WIDTH - Assets.window.get_width()) / 2, (SCREEN_HEIGHT - Assets.window.get_height()) / 2))
            self.title.draw(self.screen)
            self.subtitle.draw(self.screen)
            self.btn_back.draw(self.screen)
            self.btn_confirm.draw(self.screen)
            self.input_code.draw(self.screen)
            
        self.error_bubble.draw()

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
        card_surf.fill(BUTTON_BACKGROUND)
        self.screen.blit(card_surf, (card_x, card_y))
        pygame.draw.rect(self.screen, WHITE, (card_x, card_y, card_w, card_h), 2, border_radius=8)

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

        title_surf = self.font_title.render(f'Sauvegarde #{save_id}', True, WHITE)
        self.screen.blit(title_surf, (card_x + padding, card_y + padding))
        
        minutes = duration // 60
        seconds = duration % 60

        infos = [
            (f'Durée : {minutes} min {seconds:02d} s', WHITE),
            (f'Créée : {created}', WHITE),
            (status, status_color),
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