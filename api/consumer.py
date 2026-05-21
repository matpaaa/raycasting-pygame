from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ConsumerWebsocket(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.id_save = self.scope["url_route"]["kwargs"]["id_save"]
        self.group_name = f"save_{self.id_save}"
        
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        
        await self.accept()
        
    async def receive(self, text_data):
        data = json.loads(text_data)
        
        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "move",
                "pos_x": data["pos_x"],
                "pos_y": data["pos_y"],
                "id_player": data["id_player"]
            }
        )

    async def move(self, event):
        await self.send(text_data=json.dumps({
            "type": "move",
            "pos_x": event["pos_x"],
            "pos_y": event["pos_y"],
            "id_player": event["id_player"]
        }))
        
    async def join(self, event):
        await self.send(text_data=json.dumps({
            "type": "join",
            "pos_x": event["pos_x"],
            "pos_y": event["pos_y"],
            "id_player": event["id_player"]
        }))
        
    async def drop_item(self, event):
        await self.send(text_data=json.dumps({
            "type": "join",
            "pos_x": event["pos_x"],
            "pos_y": event["pos_y"],
            "item": event["item"]
        }))