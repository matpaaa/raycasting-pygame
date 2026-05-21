import websockets, json
from app.sprites.player_sprite import *
from app.features.user import *

class ClientWebsocket:
    
    def __init__(self, players: list[PlayerSprite], id_save: int, id_player: int):
        self.players = players
        self.ws = None
        self.id_save = id_save
        self.id_player = id_player
        
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
        
    def handle_rcv(self, data_rcv):
        type = data_rcv['type']
        if type is None: return
        
        if type == 'move':
            self.handle_move(data_rcv)
        
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