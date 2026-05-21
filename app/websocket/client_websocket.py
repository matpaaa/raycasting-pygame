import websockets, json
from app.sprites.player_sprite import *
from app.features.user import *
from app.features.item import *
from app.sprites.object_sprite import *
from app.sprites.player_sprite import *

class ClientWebsocket:
    
    def __init__(self, players: list[PlayerSprite], id_save: int, id_player: int, map_config):
        self.players = players
        self.ws = None
        self.id_save = id_save
        self.id_player = id_player
        self.map_config = map_config
        
    async def send_data(self, data):
        if self.ws is None: return
        await self.ws.send(json.dumps(data))
        
    def get_player(self, id_player: int):
        for player in self.players:
            if player.id == id_player:
                return player
        
    def handle_move(self, data):
        id_player = data['id_player']
        if id_player == self.id_player: return
        
        pos_x = data['pos_x']
        pos_y = data['pos_y']
        
        if id_player is None or pos_x is None or pos_y is None:
            print("Donnée incorrecte impossible de faire bouger le player")
            return
        
        player = self.get_player(id_player)
        player.handle_move(pos_x,pos_y)
        
    def handle_drop_item(self, data):
        id_player = data['id_player']
        if id_player == self.id_player: return
        
        pos_x = data['pos_x']
        pos_y = data['pos_y']
        item = data['item']
        value = float(item['value']) if item['value'] is not None else None
        itemClass = Item(item['id_item'], item['name'], value, item['id_item_type'], item['image'])
        self.map_config.add_item_to_sprite(pos_x, pos_y, itemClass)
        
    def handle_join_player(self, data):
        id_player = data['id_player']
        if id_player == self.id_player: return
        
        pos_x = data['pos_x']
        pos_y = data['pos_y']
        id_player = data['id_player']
        
        player = PlayerSprite(pos_x, pos_y, id_player)
        self.players.append(player)
        
    def handle_rcv(self, data_rcv):
        type = data_rcv['type']
        if type is None: return
        
        print(data_rcv)
        
        if type == 'move':
            self.handle_move(data_rcv)
        elif type == 'drop_item':
            self.handle_drop_item(data_rcv)
        elif type == 'join':
            self.handle_join_player(data_rcv)
        
    async def connect(self):
        async with websockets.connect(f"ws://localhost:8000/ws/save/{self.id_save}/") as ws:
            self.ws = ws
            
            while True:
                data_rcv = json.loads(await self.ws.recv())
                self.handle_rcv(data_rcv)

    async def move(self, user: User):
        data = {
            'pos_x': user.pos_x,
            'pos_y': user.pos_y,
            'id_player': user.id_player
        }
        await self.send_data(data)