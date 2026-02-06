import sqlite3

conn = sqlite3.connect("HiMe.db")
c = conn.cursor()
conn.execute("PRAGMA foreign_keys = ON")

les_mots = """
INSERT INTO vocabulaire VALUES (NULL,'maison','mot','lieu où on habite','j habite dans une grande maison',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'house',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'voiture','mot','moyen de transport','il conduit une voiture rouge',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'car',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'chien','mot','animal domestique','le chien dort',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'dog',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'chat','mot','animal domestique','le chat mange',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'cat',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'livre','mot','objet pour lire','je lis un livre',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'book',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'eau','mot','liquide vital','je bois de l eau',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'water',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'pain','mot','aliment','j achete du pain',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'bread',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'fromage','mot','produit laitier','le fromage est bon',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'cheese',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'soleil','mot','etoile','le soleil brille',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'sun',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'lune','mot','astre','la lune est pleine',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'moon',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'travail','mot','activite professionnelle','je vais au travail',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'work',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'ecole','mot','lieu d apprentissage','il va a l ecole',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'school',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'ami','mot','personne proche','mon ami arrive',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'friend',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'famille','mot','groupe familial','ma famille est ici',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'family',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'temps','mot','notion de duree','le temps passe vite',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'time',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'argent','mot','moyen de paiement','il gagne de l argent',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'money',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'ville','mot','zone urbaine','la ville est grande',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'city',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'pays','mot','territoire','j aime ce pays',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'country',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'route','mot','voie','la route est longue',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'road',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'mer','mot','grande etendue d eau','la mer est bleue',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'sea',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'ciel','mot','espace au dessus','le ciel est clair',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'sky',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'pluie','mot','eau qui tombe','la pluie commence',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'rain',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'neige','mot','precipitation','la neige tombe',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'snow',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'feu','mot','combustion','le feu brule',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'fire',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'air','mot','gaz vital','l air est frais',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'air',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'main','mot','partie du corps','je leve la main',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'hand',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'tete','mot','partie du corps','ma tete fait mal',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'head',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'oeil','mot','organe de la vue','son oeil est ferme',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'eye',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'bouche','mot','organe','ouvre la bouche',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'mouth',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'pied','mot','partie du corps','il se blesse au pied',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'foot',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'jour','mot','periode de 24h','le jour se leve',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'day',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'nuit','mot','absence de soleil','la nuit tombe',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'night',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'heure','mot','unite de temps','une heure passe',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'hour',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'minute','mot','petite unite','attends une minute',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'minute',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'semaine','mot','periode de temps','la semaine commence',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'week',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'annee','mot','periode longue','l annee finit',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'year',last_insert_rowid());
"""
les_expressions = """ 
INSERT INTO vocabulaire VALUES (NULL,'casser la glace','expression','commencer une conversation dans une situation tendue','il a raconte une blague pour casser la glace',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'break the ice',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'avoir le cafard','expression','etre triste','il a le cafard aujourd hui',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'feel blue',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'donner sa langue au chat','expression','abandonner une devinette','je donne ma langue au chat',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'give up',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'mettre les pieds dans le plat','expression','parler sans tact','il a mis les pieds dans le plat',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'put ones foot in it',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'avoir la tete dans les nuages','expression','etre distrait','il a la tete dans les nuages',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'have ones head in the clouds',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'couter les yeux de la tete','expression','etre tres cher','ce telephone coute les yeux de la tete',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'cost an arm and a leg',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'tomber dans les pommes','expression','perdre connaissance','il est tombe dans les pommes',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'faint',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'avoir un coup de foudre','expression','tomber amoureux instantanement','il a eu un coup de foudre',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'fall in love at first sight',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'mettre la main a la pate','expression','aider activement','tout le monde met la main a la pate',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'pitch in',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'prendre son temps','expression','ne pas se presser','prends ton temps',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'take ones time',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'etre sur son trente et un','expression','etre tres bien habille','il est sur son trente et un',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'be dressed to the nines',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'faire d une pierre deux coups','expression','atteindre deux objectifs','il a fait d une pierre deux coups',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'kill two birds with one stone',last_insert_rowid());
"""

conn.execute("BEGIN TRANSACTION;")

c.executescript(les_mots)
c.executescript(les_expressions)

conn.commit()
conn.close()

print("\nLa base de données HiMe a été remplie avec succès !")