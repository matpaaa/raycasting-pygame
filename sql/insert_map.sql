INSERT INTO map(id_map, name, default_pos_x, defautl_pos_y) VALUES (1, 'Last Breath Jail', 2.5, 21);

INSERT INTO sprite (id_sprite, pos_x, pos_y) VALUES
(1000000000, 5.5, 3),
(1000000001, 10.5, 14),
(1000000002, 17, 8.5),
(1000000003, 29, 15.5),
(1000000004, 16.5, 17),
(1000000005, 25.5, 13);

INSERT INTO sprite_door (id_sprite, id_sprite_door_type, id_map) VALUES
(1000000000, 'CODE', 1),
(1000000001, 'KEY', 1),
(1000000002, 'KEY', 1),
(1000000003, 'KEY', 1),
(1000000005, 'KEY', 1);

INSERT INTO puzzle (id_puzzle, id_map, title, content) VALUES
(1, 1, 'Prisonnier inconnu', 
'Un détenu parle des cinq gardes qui contrôlaient autrefois la prison. Selon lui, ils possédaient quelque chose qui aurait pu sauver les prisonniers avant leur disparition soudaine.'),
(2, 1, 'Epstein', 
'Epstein est enfermé dans cette prison depuis des années. Il supplie le joueur de le faire sortir mais évoque aussi un mystérieux morceau de code introuvable dans les couloirs sombres de la prison.'),
(3, 1, 'Le demi-zombie', 
'Un prisonnier à moitié transformé affirme qu’un morceau de code se trouve dans une salle infestée de zombies.'),
(4, 1, 'Arnaud', 
'Arnaud semble terrifié par une zone au nord de la prison. Il parle d’un tunnel dangereux. Quelque chose se cache dans ce bloc abandonné ?'),
(5, 1, 'Le vieux prisonnier', 
'Le vieux prisonnier radote sans arrêt à propos des codes, des zombies et d’une sortie impossible. Malgré sa confusion, certaines de ses phrases semblent cacher des indices importants sur la prison et ses secrets.');