INSERT INTO map(id_map, name) VALUES (1, 'Last Breath Jail');

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
(1, 1, 'Cellule bloquée', 'prisonnier Epstein est enfermé dans une cellule depuis longtemps. la porte est verrouillée, il ne peut pas sortir. il cache quelque chose dans sa cellule (bout de code) mais ne le dit pas.'),
(2, 1, 'Les 5 codes', 'Prisonnier chauve connaît l’existence des codes mais essaie de décourager le joueur tout en lui en donnant un.'),
(3, 1, 'Bloc dangereux', 'Prisonnier Arnaud a vu une zone très infestée et avertit le joueur . la zone en question possède des zombies avec un bout de code dans le coin au fond de la zone'),
(4, 1, 'Couloirs sombres', 'Epstein chercher le bout de code de son compagnon de prison mais ne la jamais trouvé.'),
(5, 1, 'Sortie', 'Prisonnier chauve connaît la sortie mais doute que ce soit une vraie échappatoire.');