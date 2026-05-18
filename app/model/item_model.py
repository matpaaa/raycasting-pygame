import time

class ItemModel:
    id_item: str
    value: float
    name: str
    id_item_type: str
    
class ItemSecretModel(ItemModel):
    id_item_secret_possessed: int
    created_at: time
    
class PlayerItemModel(ItemModel):
    id_item_possessed: int
    created_at: time