

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
Récupère toutes les saves pour les affichers dans le menu
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
Charge toutes les données de la partie
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


### GET /api/logout
Supprimer le token de l'utilisateur pour les déconnecter

### POST /api/login
```
BODY
{
    credential: str
    password: str
}
```

### POST /api/register
```
BODY
{
    username: str
    email: str
    password: str
}
```

### POST /api/verify-code
Vérifie le code envoyé par email lors de la création d'un compte
```
BODY
{
    email: str
    code: str
}
```

### DELETE /api/account
Supprime le compte

### DELETE /api/save
Supprimer une sauvegarde
```
BODY
{
    id_save: int
}
```

### PUT /api/player/save
Sauvegarde du joueur utilisateur de la personne
```
BODY
{
    id_save: int
    health: int
    energy: int
    pos_x: float
    pos_y: float
    rotation: int
}
```

### POST /api/puzzle/finish
Finie une énigme et donne à tous les utilisateurs l'item en récompense
```
BODY
{
    id_save: int
    id_puzzle: int
}
```

### POST /api/door/open
Si le type de la porte ouverte est KEY alors il faut vérifier si les utilisateurs ont assez de clé et faire -1 clé
```
BODY
{
    id_save: int
    id_sprite: int
}
```

### POST /api/recover/item
```
BODY
{
    id_sprite: int
    id_save: int
    id_item: int
}
```

### DELETE /api/drop/item
Supprime l'item de l'inventaire de l'utilisateur et créer un sprite_item à l'emplacement de l'utilisateur
```
BODY
{
    id_save: int
    id_item: int
    pos_x: float
    pos_y: float
}
```

### POST /api/create/save
Lors ce que l'utilisateur créer une partie il va envoyé toutes les données des sprite_item & sprite_enemie présent dans ces fichiers au serveur
```
BODY
{
    sprite_enemies: [
        {
            health: int
            damage: int
            pos_x: float
            pos_y: float
            image: str
        }
    ]
    sprite_items: [
        {
            id_item: str
            pos_x: float
            pos_y: float
            image: str
        }
    ]
}
```

### POST /api/save/online
Le joueur qui a créer la partie peut activer le mode online, cela génère un code et le met dans "online_code" dans la table SAVE
```
BODY
{
    id_player: int
    id_save: int
}
```

### POST /api/save/join
Un joueur qui est différent de celui d'origine peut rejoindre la partie en entrant le code
```
BODY
{
    online_code: str
}
```

### POST /api/save/win
```
BODY
{
    id_save: int
}
```

### POST /api/save/failed
```
BODY
{
    id_save: int
}
```

### POST /api/save/consumable
Consommer une item
```
BODY
{
    id_item: int
    id_save: int
}
```

### POST /api/save/shoot
Consommer une item
```
BODY
{
    id_sprite: int
    id_save: int
}
```