INSERT INTO item_type (id_item_type) VALUES
  ('CONSUMABLE'),
  ('WEAPON'),
  ('AMMO'),
  ('SECRET'),
  ('ELECTRICITY');

INSERT INTO sprite_door_type (id_sprite_door_type, image) VALUES
  ('KEY', './app/assets/textures/bars.png'),
  ('CODE', './app/assets/textures/bars.png');

INSERT INTO item (id_item, name, value, id_item_type, image) VALUES
    ('VODKA',    'Vodka',           0.04, 'CONSUMABLE', './app/assets/game/items/vodka.png'),
    ('CANNED',   'Conserve',        40,   'CONSUMABLE', './app/assets/game/items/canned.png'),
    ('GUN',      'Fusil',           50,   'WEAPON', './app/assets/game/items/gun.png'),
    ('AMMO',     'Munition',        NULL, 'AMMO', './app/assets/game/items/ammo.png'),
    ('KEY',      'Clé',             NULL, 'SECRET', './app/assets/game/items/key.png'),
    ('CODE',     'Morceau de code', NULL, 'SECRET', './app/assets/game/items/code.png'),
    ('BATTERY',  'Batterie',        100,  'ELECTRICITY', './app/assets/game/items/battery.png');