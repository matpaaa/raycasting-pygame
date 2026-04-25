CREATE TABLE IF NOT EXISTS item_type (
  id_item_type VARCHAR(16) PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS item (
  id_item VARCHAR(16) PRIMARY KEY,
  name VARCHAR(16) NOT NULL,
  value DECIMAL(10,2),
  id_item_type VARCHAR(16) NOT NULL,

  FOREIGN KEY (id_item_type)
  REFERENCES item_type(id_item_type)
);

CREATE TABLE IF NOT EXISTS sprite (
  id_sprite INT PRIMARY KEY,
  pos_x DECIMAL(10,2) NOT NULL,
  pos_y DECIMAL(10,2) NOT NULL,
  image TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS sprite_door_type (
  id_sprite_door_type VARCHAR(16) PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS map (
  id_map SERIAL PRIMARY KEY,
  name VARCHAR(16) NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS puzzle (
  id_puzzle SERIAL PRIMARY KEY,
  title VARCHAR(128) NOT NULL,
  content VARCHAR(128) NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT NOW(),
  id_sprite_door_type VARCHAR(16) NOT NULL,

  FOREIGN KEY (id_sprite_door_type)
  REFERENCES sprite_door_type(id_sprite_door_type)
);

CREATE TABLE IF NOT EXISTS sprite_door (
  id_sprite INT PRIMARY KEY,
  id_sprite_door_type VARCHAR(16) NOT NULL,
  id_map INT NOT NULL,

  FOREIGN KEY (id_sprite) REFERENCES sprite(id_sprite),
  FOREIGN KEY (id_sprite_door_type) REFERENCES sprite_door_type(id_sprite_door_type),
  FOREIGN KEY (id_map) REFERENCES map(id_map)
);

CREATE TABLE IF NOT EXISTS sprite_item (
  id_sprite INT PRIMARY KEY,
  created_at TIMESTAMP NOT NULL DEFAULT NOW(),
  id_item VARCHAR(16) NOT NULL,

  FOREIGN KEY (id_sprite) REFERENCES sprite(id_sprite),
  FOREIGN KEY (id_item) REFERENCES item(id_item)
);

CREATE TABLE IF NOT EXISTS sprite_enemy (
  id_sprite INT PRIMARY KEY,
  health INT NOT NULL,
  damage INT NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT NOW(),

  FOREIGN KEY (id_sprite) REFERENCES sprite(id_sprite)
);

CREATE TABLE IF NOT EXISTS account (
  id_account SERIAL PRIMARY KEY,
  name VARCHAR(16) NOT NULL UNIQUE,
  password VARCHAR(180) NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT NOW(),
  email VARCHAR(320) NOT NULL UNIQUE,
  is_verified BOOLEAN NOT NULL DEFAULT FALSE,
  verification_code VARCHAR(6) NULL
);

CREATE TABLE IF NOT EXISTS save (
  id_save SERIAL PRIMARY KEY,
  created_at TIMESTAMP NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMP NOT NULL DEFAULT NOW(),
  duration INTEGER NOT NULL,
  is_win BOOLEAN NOT NULL DEFAULT FALSE,
  is_failed BOOLEAN NOT NULL DEFAULT FALSE,
  online_code VARCHAR(6),
  id_map INT NOT NULL,

  FOREIGN KEY (id_map) REFERENCES map(id_map)
);

CREATE TABLE IF NOT EXISTS player (
  id_player SERIAL PRIMARY KEY,
  health SMALLINT NOT NULL,
  energy INTEGER NOT NULL,
  pos_x DECIMAL(10,2) NOT NULL,
  pos_y DECIMAL(10,2) NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT NOW(),
  name VARCHAR(16) NOT NULL,
  is_owner BOOLEAN NOT NULL DEFAULT FALSE,

  id_account INT NOT NULL,
  id_save INT NOT NULL,

  FOREIGN KEY (id_account) REFERENCES account(id_account),
  FOREIGN KEY (id_save) REFERENCES save(id_save)
);

CREATE TABLE IF NOT EXISTS item_possessed (
  id_item_possessed SERIAL PRIMARY KEY,
  created_at TIMESTAMP NOT NULL DEFAULT NOW(),

  id_item VARCHAR(16) NOT NULL,
  id_player INT NOT NULL,

  FOREIGN KEY (id_item) REFERENCES item(id_item),
  FOREIGN KEY (id_player) REFERENCES player(id_player)
);

CREATE TABLE IF NOT EXISTS item_secret_possessed (
  id_item_secret_possessed SERIAL PRIMARY KEY,
  created_at TIMESTAMP NOT NULL DEFAULT NOW(),
  id_item VARCHAR(16) NOT NULL,
  id_save INT NULL,

  FOREIGN KEY (id_item) REFERENCES item(id_item),
  FOREIGN KEY (id_save) REFERENCES save(id_save)
);

CREATE TABLE IF NOT EXISTS to_finish (
  id_save INT NOT NULL,
  id_puzzle INT NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT NOW(),
  PRIMARY KEY (id_save, id_puzzle),
  FOREIGN KEY (id_save) REFERENCES save(id_save),
  FOREIGN KEY (id_puzzle) REFERENCES puzzle(id_puzzle)
);

CREATE TABLE IF NOT EXISTS to_open (
  id_sprite INT NOT NULL,
  id_save INT NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT NOW(),
  PRIMARY KEY (id_save, id_sprite),
  FOREIGN KEY (id_save) REFERENCES save(id_save),
  FOREIGN KEY (id_sprite) REFERENCES sprite_door(id_sprite)
);