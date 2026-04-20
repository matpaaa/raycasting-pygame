-- ----------------------------------------------------------
-- Script PostgreSQL pour MCD
-- ----------------------------------------------------------

-- ----------------------------
-- Table: item_type
-- ----------------------------
CREATE TABLE IF NOT EXISTS item_type (
    id_item_type VARCHAR(16) NOT NULL,
    is_required BOOLEAN NOT NULL,
    CONSTRAINT item_type_pk PRIMARY KEY (id_item_type)
);


-- ----------------------------
-- Table: map
-- ----------------------------
CREATE TABLE IF NOT EXISTS map (
    id_map SERIAL NOT NULL,
    name VARCHAR(16) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    CONSTRAINT map_pk PRIMARY KEY (id_map)
);


-- ----------------------------
-- Table: account
-- ----------------------------
CREATE TABLE IF NOT EXISTS account (
    id_account SERIAL NOT NULL,
    name VARCHAR(16) NOT NULL,
    password VARCHAR(60) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    email VARCHAR(320) NOT NULL,
    CONSTRAINT account_pk PRIMARY KEY (id_account)
);


-- ----------------------------
-- Table: save
-- ----------------------------
CREATE TABLE IF NOT EXISTS save (
    id_save SERIAL NOT NULL,
    pos_y NUMERIC(10,2) NOT NULL,
    pox_x NUMERIC(10,2) NOT NULL,
    health SMALLINT NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,
    id_account INT NOT NULL,
    id_map INT NOT NULL,
    CONSTRAINT save_pk PRIMARY KEY (id_save),
    CONSTRAINT save_id_account_fk 
        FOREIGN KEY (id_account) 
        REFERENCES account (id_account),
    CONSTRAINT save_id_map_fk 
        FOREIGN KEY (id_map) 
        REFERENCES map (id_map)
);


-- ----------------------------
-- Table: item_possessed
-- ----------------------------
CREATE TABLE IF NOT EXISTS item_possessed (
    id_item_possessed SERIAL NOT NULL,
    created_at TIMESTAMP NOT NULL,
    id_save INT NOT NULL,
    CONSTRAINT item_possessed_pk PRIMARY KEY (id_item_possessed),
    CONSTRAINT item_possessed_id_save_fk 
        FOREIGN KEY (id_save) 
        REFERENCES save (id_save)
);


-- ----------------------------
-- Table: item
-- ----------------------------
CREATE TABLE IF NOT EXISTS item (
    id_item VARCHAR(16) NOT NULL,
    name VARCHAR(16) NOT NULL,
    value NUMERIC(10,2) NOT NULL,
    id_item_type VARCHAR(16) NOT NULL,
    id_item_possessed INT NOT NULL,
    CONSTRAINT item_pk PRIMARY KEY (id_item),
    CONSTRAINT item_id_item_type_fk 
        FOREIGN KEY (id_item_type) 
        REFERENCES item_type (id_item_type),
    CONSTRAINT item_id_item_possessed_fk 
        FOREIGN KEY (id_item_possessed) 
        REFERENCES item_possessed (id_item_possessed)
);