INSERT INTO item_type (id_item_type) VALUES
  ('CONSUMABLE'),
  ('WEAPON'),
  ('AMMO'),
  ('SECRET'),
  ('ELECTRICITY');

INSERT INTO sprite_door_type (id_sprite_door_type) VALUES
  ('KEY'),
  ('CODE');

INSERT INTO item (id_item, name, value, id_item_type) VALUES
    ('VODKA',    'Vodka',           0.04, 'CONSUMABLE'),
    ('CANNED',   'Conserve',        40,   'CONSUMABLE'),
    ('GUN',      'Fusil',           50,   'WEAPON'),
    ('AMMO',     'Munition',        NULL, 'AMMO'),
    ('KEY',      'Clé',             NULL, 'SECRET'),
    ('CODE',     'Morceau de code', NULL, 'SECRET'),
    ('BATTERY',  'Batterie',        100,  'ELECTRICITY');