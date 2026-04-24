INSERT INTO item_type (id_item_type) VALUES
  ('CONSUMABLE'),
  ('WEAPON'),
  ('AMMO'),
  ('SECRET'),
  ('ELECTRICITY');

INSERT INTO sprite_door_type (id_sprite_door_type) VALUES
  ('KEY'),
  ('CODE');

INSERT INTO item (id_item, name, value) VALUES
    ('VODKA', 'Vodka', 0.04),
    ('CANNED', 'Conserve', 40),
    ('GUN', 'Fusil', 50),
    ('AMMO', 'Munition', NULL),
    ('KEY', 'Clé', NULL),
    ('CODE', 'Morceau de code', NULL),
    ('BATTERY', 'Battery', 100);