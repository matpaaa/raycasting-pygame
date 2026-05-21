import asyncio

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
from app.sprites.player_sprite import *
from app.websocket.client_websocket import *

class Game:
    
    players: List[PlayerSprite] = []
    
    def __init__(self, screen: Surface):
        self.screen = screen

        self.client_ws = None
        self.session_start = None
        self.save_loaded = None
        self.map_config = None
        self.sprite_interact = None
        self.event = None
        self.pygame_actions = None

        self.btn_back_menu = Button('RETOUR AU MENU', SCREEN_WIDTH//2 - ELEMENT_WIDTH_LARGE//2, SCREEN_HEIGHT - 150, ELEMENT_WIDTH_LARGE, ELEMENT_HEIGHT)
        self.dead_sound = None
        self.game_menu = False
        
        self.menu_puzzle = False
        self.current_puzzle_index = 0
        
        self.is_failed = False
        self.is_win = False
        
        self.is_failed_req = False
        self.is_win_req = False
        
        self.players = []
        self.online_code = None

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
            350 + ELEMENT_HEIGHT,
            ELEMENT_WIDTH_SMALL,
            ELEMENT_HEIGHT,
            'danger'
        )
        
        self.btn_active_online = Button(
            'Activer le monde en ligne',
            SCREEN_WIDTH/2 - ELEMENT_WIDTH_LARGE//2,
            320,
            ELEMENT_WIDTH_LARGE,
            ELEMENT_HEIGHT,
        )

        self.btn_save = Button(
            'VALIDER',
            SCREEN_WIDTH/2 + GAP_BETWEEN_ELEMENT/2,
            350 + ELEMENT_HEIGHT,
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
        
    def failed_req(self):
        if not self.is_failed_req:
            self.is_failed_req = True
            game_failed(self.save_loaded['id_save'])
            
    def win_req(self):
        if not self.is_win_req:
            self.is_win_req = True
            game_win(self.save_loaded['id_save'])
            
    def active_online(self):
        res = SaveApi.active_online({
            'id_player': self.user.id_player,
            'id_save': self.save_loaded['id_save']
        })
        self.online_code = res['online_code']
        
    def navigate_error(self):
        self.unload_save()
        global_var.navigate_page('error')
        
    def load_save(self):
        try:
            if self.map_config is not None: return
            
            save_loaded = global_var.save_store.save_loaded
            me = global_var.user_store.me
            
            self.session_start = pygame.time.get_ticks()
            
            self.current_player = next((player for player in save_loaded['players'] if player['id_account'] == me['id_account']), None)
            if self.current_player is None:
                global_var.navigate_page('saves')
                return
            
            other_players = [
                player for player in save_loaded['players']
                if player['id_player'] != self.current_player['id_player']
            ]
            
            for player in other_players:
                player_pos_x = float(player['pos_x'])
                player_pos_y = float(player['pos_y'])
                id_player = int(player['id_player'])
                self.players.append(PlayerSprite(player_pos_x, player_pos_y, id_player))
                
            self.online_code = save_loaded['online_code']
                    
            sprites = save_loaded['sprite_items'] + save_loaded['sprite_enemies'] + save_loaded['sprite_doors'] + [sprite for sprite in MAP_SPRITES_MOCKED if isinstance(sprite, HumanSprite)] + self.players
            for sprite in sprites:
                sprite.load()
                
            self.map_config = MapConfig(MAP_MOCKED, sprites, MAP_TEXTURES_MOCKED, save_loaded['id_save'])
            self.map_config.load_textures()
            
            user_items = []
            for item in save_loaded['items_secret']:
                user_items.append(Item(item['id_item'], item['name'], item['value'], item['id_item_type'], item['image']))
                
            for item in self.current_player['items']:
                user_items.append(Item(item['id_item'], item['name'], item['value'], item['id_item_type'], item['image']))
            
            pos_x = float(self.current_player['pos_x']) or DEFAULT_USER_POS_X
            pos_y = float(self.current_player['pos_y']) or DEFAULT_USER_POS_Y
            health = int(self.current_player['health'])
            energy = int(self.current_player['energy'])
            id_player = int(self.current_player['id_player'])
            rotation = self.current_player['rotation'] or DEFAULT_USER_ROT
            
            self.user = User(pos_x, pos_y, rotation, health, energy, id_player, self.map_config)
            self.user.set_items(user_items)
            
            self.client_ws = ClientWebsocket(self.players, save_loaded['id_save'], self.current_player['id_player'], self.map_config, self.user)
            threading.Thread(
                target=lambda: asyncio.run(self.client_ws.connect())
            ).start()
            
            self.health = Health(self.user, self.screen)
            self.battery = Battery(self.screen, self.user)
            self.inventory = Inventory(self.user, self.screen)
            self.ray_casting = RayCasting(self.screen, self.user, self.map_config)
            self.minimap = Minimap(self.screen, self.user, self.map_config)
            self.pygame_actions = PygameActions(self.user, self.screen, self.map_config, self.client_ws)
            self.interaction = Interaction(self.screen, self.user)
            
            self.save_loaded = save_loaded
            
            if self.save_loaded['is_failed']:
                self.is_failed = True
                self.failed_req()
                
            if self.save_loaded['is_win']:
                self.is_win = True
                self.win_req()
        except Exception as e:
            print(e)
            self.navigate_error()
        
    def unload_save(self):
        self.map_config = None
        self.session_start = None
        self.client_ws = None
        self.online_code = None
        
        self.user = None
        self.health = None
        self.battery = None
        self.inventory = None
        self.ray_casting = None
        self.minimap = None
        self.pygame_actions = None
        self.interaction = None
        
        self.is_failed = False
        self.is_failed_req = False
        self.is_win = False
        self.is_win_req = False
        self.players = []

    def handle_event(self, event: Event):
        try:
            if self.pygame_actions is None: return
            
            self.event = event
            if not self.is_win and not self.is_failed:
                self.pygame_actions.one_actions(self.sprite_interact, self.event)
            
            if self.game_menu:
                if self.btn_active_online.is_clicked(event) and self.current_player['is_owner']:
                    self.active_online()

                if self.btn_back_menu.is_clicked(event) or self.btn_back.is_clicked(event):
                    Sounds.click()
                    global_var.navigate_page('saves')
                    self.game_menu = False

                if self.btn_save.is_clicked(event):
                    self.btn_save.is_loading = True
                    Sounds.click()
                    self.save_user_async()
                    global_var.save_store.invalid_saves({'refetch': True})
                    self.game_menu = False
                    self.btn_save.is_loading = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                if self.game_menu:
                    self.game_menu = False
                else:
                    self.game_menu = True
                
            if not self.game_menu:
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
        except Exception as e:
            print(e)
            self.navigate_error()

    def draw(self):
        try:
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
            
            elapsed_seconds = (pygame.time.get_ticks() - self.session_start) // 1000
            remaining = GAME_DURATION - self.save_loaded['duration'] - elapsed_seconds
            
            if remaining <= 0:
                self.is_failed = True
                self.failed_req()
            
            remaining = max(0, remaining)

            minutes = remaining // 60
            seconds = remaining % 60

            timer_surf = Fonts.font_title.render(f'{minutes} min {seconds:02d} s', True, TEXT_GRAY)
            self.screen.blit(timer_surf, (SCREEN_WIDTH//2-timer_surf.get_width()//2, 50))

            if not self.user.is_dead and not self.user.has_win and not self.game_menu:
                self.pygame_actions.actions(self.sprite_interact, self.event)

            if self.is_failed:
                if self.dead_sound is None:
                    self.dead_sound = Sounds.dead()
                overlay = pygame.Surface((self.screen.get_width(), self.screen.get_height()), pygame.SRCALPHA)
                overlay.fill((255, 56, 60, 255*0.3))
                self.screen.blit(overlay, (0, 0))
                self.screen.blit(Assets.dead_screen, (SCREEN_WIDTH//2 - Assets.dead_screen.get_width()//2, SCREEN_HEIGHT//2 - Assets.dead_screen.get_height()//2))
                self.btn_back_menu.draw(self.screen)
                
            if self.is_win:
                overlay = pygame.Surface((self.screen.get_width(), self.screen.get_height()), pygame.SRCALPHA)
                overlay.fill((52, 199, 89, 255*0.3))
                self.screen.blit(overlay, (0, 0))
                self.screen.blit(Assets.win_screen, (SCREEN_WIDTH//2 - Assets.win_screen.get_width()//2, SCREEN_HEIGHT//2 - Assets.win_screen.get_height()//2))
                self.btn_back_menu.draw(self.screen)
                

            if self.user.is_dead:
                self.is_failed = True
                self.failed_req()
                
            if self.user.has_win:
                self.is_win = True
                self.win_req()

            if self.game_menu:
                self.screen.blit(Assets.window_small, ((SCREEN_WIDTH - Assets.window_small.get_width())//2, (SCREEN_HEIGHT - Assets.window_small.get_height())//2))
                self.title.draw(self.screen)
                
                if self.current_player['is_owner']:
                    if self.online_code:
                        self.online_code_title = Text(
                            str(self.online_code),
                            'center',
                            320,
                            WHITE,
                            'title'
                        )
                        self.online_code_title.draw(self.screen)
                    else:
                        self.btn_active_online.draw(self.screen)
                    
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
        except Exception as e:
            print(e)
            self.navigate_error()