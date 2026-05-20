from app.core.pygame_actions import PygameActions
from app.core.ray_casting import RayCasting
from app.features.minimap import Minimap
from app.constants.settings import DEFAULT_USER_POS_X, DEFAULT_USER_POS_Y, DEFAULT_USER_ROT, FPS, SCREEN_BACKGROUND, SCREEN_HEIGHT, SCREEN_WIDTH
from app.features.user import User
from app.features.health import *
from app.features.inventory import *
from app.sprites.human_sprite import *
from app.core.interaction import *
from pygame.event import Event
from app.features.map_config import *
from app.mock.map_mocked import *
from pygame import Surface
from app.ui.button import *
from app.ui.text import *
import app._utils.global_var as global_var
from app.features.battery import *
from app.services.save_service import *
import threading
from app._utils.wrap_text import *

class Game:
    
    def __init__(self, screen: Surface):
        self.screen = screen

        self.save_loaded = None
        self.map_config = None
        self.sprite_interact = None
        self.event = None

        self.btn_back_menu = Button('RETOUR AU MENU', SCREEN_WIDTH//2 - ELEMENT_WIDTH_LARGE//2, SCREEN_HEIGHT - 150, ELEMENT_WIDTH_LARGE, ELEMENT_HEIGHT)
        self.dead_sound = None
        self.game_menu = False
        
        self.menu_puzzle = False
        self.current_puzzle_index = 0

        self.title = Text(
            "SAUVEGARDER LA PARTIE",
            'center',
            275,
            WHITE,
            'title'
        )

        self.btn_back = Button(
            'QUITTER',
            SCREEN_WIDTH/2 - GAP_BETWEEN_ELEMENT/2 - ELEMENT_WIDTH_SMALL,
            325 + ELEMENT_HEIGHT,
            ELEMENT_WIDTH_SMALL,
            ELEMENT_HEIGHT,
            'danger'
        )

        self.btn_save = Button(
            'VALIDER',
            SCREEN_WIDTH/2 + GAP_BETWEEN_ELEMENT/2,
            325 + ELEMENT_HEIGHT,
            ELEMENT_WIDTH_SMALL,
            ELEMENT_HEIGHT
        )
        
        self.arrow_left_x = (SCREEN_WIDTH - Assets.window.get_width())//2 + 32
        self.arrow_left_y = SCREEN_HEIGHT//2-Assets.arrow_left.get_height()//2
        
        self.arrow_right_x = SCREEN_WIDTH - (SCREEN_WIDTH - Assets.window.get_width())//2 - 32 - Assets.arrow_left.get_width()
        self.arrow_right_y = SCREEN_HEIGHT//2-Assets.arrow_right.get_height()//2
        
    def save_user_async(self):
        thread = threading.Thread(target=save_user, args=(self.user,self.map_config.id_save,))
        thread.start()
        
    def load_save(self):
        if self.map_config is not None: return
        
        save_loaded = global_var.save_store.save_loaded
        me = global_var.user_store.me
                
        sprites = save_loaded['sprite_items'] + save_loaded['sprite_enemies'] + save_loaded['sprite_doors'] + [sprite for sprite in MAP_SPRITES_MOCKED if isinstance(sprite, HumanSprite)]
        for sprite in sprites:
            sprite.load()
            
        self.map_config = MapConfig(MAP_MOCKED, sprites, MAP_TEXTURES_MOCKED, save_loaded['id_save'])
        self.map_config.load_textures()
                                
        current_player = next((player for player in save_loaded['players'] if player['id_account'] == me['id_account']), None)
        if current_player is None:
            global_var.navigatePage('saves')
            return
        
        user_items = []
        for item in save_loaded['items_secret']:
            user_items.append(Item(item['id_item'], item['name'], item['value'], item['id_item_type'], item['image']))
            
        for item in current_player['items']:
            user_items.append(Item(item['id_item'], item['name'], item['value'], item['id_item_type'], item['image']))
        
        pos_x = float(current_player['pos_x']) or DEFAULT_USER_POS_X
        pos_y = float(current_player['pos_y']) or DEFAULT_USER_POS_Y
        rotation = current_player['rotation'] or DEFAULT_USER_ROT
        
        self.user = User(pos_x, pos_y, rotation, self.map_config)
        self.user.set_items(user_items)
        
        self.health = Health(self.user, self.screen)
        self.battery = Battery(self.screen, self.user)
        self.inventory = Inventory(self.user, self.screen)
        self.ray_casting = RayCasting(self.screen, self.user, self.map_config)
        self.minimap = Minimap(self.screen, self.user, self.map_config)
        self.pygame_actions = PygameActions(self.user, self.screen, self.map_config)
        self.interaction = Interaction(self.screen, self.user)
        
        self.save_loaded = save_loaded
        
    def unload_save(self):
        self.map_config = None
        
        self.user = None
        self.health = None
        self.battery = None
        self.inventory = None
        self.ray_casting = None
        self.minimap = None
        self.pygame_actions = None
        self.interaction = None

    def handle_event(self, event: Event):
        if self.pygame_actions is None: return
        
        self.event = event
        self.pygame_actions.one_actions(self.sprite_interact, self.event)

        if self.btn_back_menu.is_clicked(event) or self.btn_back.is_clicked(event):
            Sounds.click()
            global_var.navigatePage('saves')
            self.game_menu = False

        if self.btn_save.is_clicked(event):
            Sounds.click()
            self.save_user_async()
            global_var.save_store.invalid_saves({'refetch': True})
            self.game_menu = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            if self.game_menu:
                self.game_menu = False
            else:
                self.game_menu = True
                
        if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
            if self.menu_puzzle:
                self.menu_puzzle = False
            else:
                self.menu_puzzle = True
        
        if self.menu_puzzle and self.save_loaded:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and self.current_puzzle_index > 0:
                Sounds.click()
                self.current_puzzle_index = self.current_puzzle_index - 1

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and self.current_puzzle_index < len(self.save_loaded['puzzles'])-1:
                Sounds.click()
                self.current_puzzle_index = self.current_puzzle_index + 1

    def draw(self):
        if self.map_config is None: return
        
        self.screen.fill(SCREEN_BACKGROUND)
        self.ray_casting.launch_fucking_rays(self.user)
        self.ray_casting.draw_sprites(self.user)
        self.ray_casting.draw_darkness()
        
        self.user.handle_effect()
        self.user.draw_item_select(self.screen)
        self.minimap.draw()
        self.health.draw()
        self.battery.draw()
        self.sprite_interact = self.interaction.handle_interaction()
        self.inventory.draw()

        if not self.user.is_dead and not self.user.has_win and not self.game_menu:
            self.pygame_actions.actions(self.sprite_interact, self.event)

        if self.user.is_dead:
            if self.dead_sound is None:
                self.dead_sound = Sounds.dead()
            overlay = pygame.Surface((self.screen.get_width(), self.screen.get_height()), pygame.SRCALPHA)
            overlay.fill((255, 56, 60, 255*0.3))
            self.screen.blit(overlay, (0, 0))
            self.screen.blit(Assets.dead_screen, (SCREEN_WIDTH//2 - Assets.dead_screen.get_width()//2, SCREEN_HEIGHT//2 - Assets.dead_screen.get_height()//2))
            self.btn_back_menu.draw(self.screen)
        elif self.user.has_win:
            overlay = pygame.Surface((self.screen.get_width(), self.screen.get_height()), pygame.SRCALPHA)
            overlay.fill((52, 199, 89, 255*0.3))
            self.screen.blit(overlay, (0, 0))
            self.screen.blit(Assets.win_screen, (SCREEN_WIDTH//2 - Assets.win_screen.get_width()//2, SCREEN_HEIGHT//2 - Assets.win_screen.get_height()//2))
            self.btn_back_menu.draw(self.screen)

        if self.game_menu:
            self.screen.blit(Assets.window_small, ((SCREEN_WIDTH - Assets.window_small.get_width())//2, (SCREEN_HEIGHT - Assets.window_small.get_height())//2))
            self.title.draw(self.screen)
            self.btn_back.draw(self.screen)
            self.btn_save.draw(self.screen)
            
        puzzles = self.save_loaded['puzzles']
        if self.menu_puzzle and puzzles:
            self.screen.blit(Assets.window, ((SCREEN_WIDTH - Assets.window.get_width())//2, (SCREEN_HEIGHT - Assets.window.get_height())//2))
            
            puzzle = puzzles[self.current_puzzle_index]
            finish = [i for i in self.save_loaded['finish'] if i['id_puzzle'] == puzzle['id_puzzle']]
            title_surf = Fonts.font_title.render(puzzle['title'], True, WHITE)
            title_rect = title_surf.get_rect(center=(SCREEN_WIDTH // 2, 170))
            self.screen.blit(title_surf, title_rect)

            status_text = "Terminé" if finish else "Pas terminé"
            status_color = WHITE if finish else DANGER

            status_surf = Fonts.font_title.render(status_text, True, status_color)
            status_rect = status_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT-((SCREEN_HEIGHT-Assets.window.get_height())//2) - 32))
            self.screen.blit(status_surf, status_rect)

            lines = wrap_text(puzzle['content'], Fonts.font_puzzle_content, 500)

            y = 250
            for line in lines:
                content_surf = Fonts.font_puzzle_content.render(line, True, TEXT_GRAY)
                content_rect = content_surf.get_rect(center=(SCREEN_WIDTH // 2, y))
                self.screen.blit(content_surf, content_rect)
                y += content_surf.get_height() + 5
            
            if self.current_puzzle_index > 0:
                arrow_left  = Assets.arrow_left.copy()
                self.screen.blit(arrow_left,  (self.arrow_left_x, self.arrow_left_y))
            if self.current_puzzle_index < len(puzzles)-1:
                arrow_right = Assets.arrow_right.copy()
                self.screen.blit(arrow_right, (self.arrow_right_x, self.arrow_right_y))