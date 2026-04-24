

# Doc API

### GET /api/me
```
{
    id_account: int
    name: str
    created_at: time
    email: str
    is_verified: bool
}
```

### GET /api/maps
```
[
    {
        id_map: int
        name: str
        created_at: time
    }
]
```

### GET /api/saves
```
[
    {
        id_save: int
        created_at: time
        updated_at: time
        duration: int
        id_map: int
        is_win: bool
        is_failed: bool
        players: [
            {
                id_player: int
                health: int
                energy: int
                pos_x: float
                pos_y: float
                created_at: time
                name: str
                is_owner: bool
            }
        ]
    }
]
```

### GET /api/save/[id_save]
```
{
    id_save: int
    created_at: time
    updated_at: time
    duration: int
    id_map: int
    is_win: bool
    is_failed: bool
    players: [
        {
            id_player: int
            health: int
            energy: int
            pos_x: float
            pos_y: float
            created_at: time
            name: str
            is_owner: bool
            items: [
                {
                    id_item_possessed: time
                    created_at: time
                    id_item: str
                    value: float
                    name: str
                    id_item_type: str
                }
            ]
        }
    ]
    items_secret: [
        {
            id_item_secret_possessed: int
            created_at: time
            id_item: str
            value: float
            name: str
            id_item_type: str
        }
    ]
    finish: [
        {
            id_save: int
            id_puzzle: int
            created_at: time
        }
    ]
    puzzles: [
        {
            id_puzzle: int
            title: string
            content: string
            item: None | {
                id_item: str
                value: float
                name: str
                id_item_type: str
            }
        }
    ]
    open: [
        {
            id_save: int
            id_sprite: int
            created_at: time
        }
    ]
    sprite_doors: [
        {
            id_sprite: int
            id_sprite_door_type: str
            pos_x: float
            pos_y: float
            image: str
        }
    ]
    sprite_items: [
        {
            id_sprite: int
            pos_x: float
            pos_y: float
            image: str
            created_at: time
            id_item: str
            value: float
            name: str
            id_item_type: str
        }
    ]
    sprite_enemies: [
        {
            id_sprite: int
            pos_x: float
            pos_y: float
            image: str
            created_at: time
            health: int
            damage: int
        }
    ]
}
```