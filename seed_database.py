import sqlite3

conn = sqlite3.connect("HiMe.db")
c = conn.cursor()
conn.execute("PRAGMA foreign_keys = ON")

les_mots = """
INSERT INTO vocabulaire VALUES (NULL,'apprendre','mot','Acquérir des connaissances.', 'J’apprends Python chaque jour.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'يتعلّم','arabe', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'réussir','mot','Atteindre un objectif.', 'Je veux réussir mon projet.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'ينجح','arabe', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'échec','mot','Résultat négatif, ne pas atteindre le but.', 'Un échec aide à progresser.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'فشل','arabe', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'effort','mot','Énergie utilisée pour faire quelque chose.', 'Avec de l’effort, tout est possible.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'جهد','arabe', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'patience','mot','Capacité à attendre calmement.', 'La patience est importante en programmation.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'صبر','arabe', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'objectif','mot','But à atteindre.', 'Mon objectif est de trouver un stage.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'هدف','arabe', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'confiance','mot','Sentiment de sécurité en soi.', 'J’ai confiance en moi.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'ثقة','arabe', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'concentration','mot','Attention forte sur une tâche.', 'Je travaille avec concentration.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'تركيز','arabe', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'solution','mot','Réponse à un problème.', 'J’ai trouvé une solution.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'حلّ','arabe', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'problème','mot','Difficulté à résoudre.', 'Ce bug est un problème.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'مشكلة','arabe', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'erreur','mot','Résultat incorrect.', 'J’ai une erreur dans le code.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'خطأ','arabe', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'réparer','mot','Corriger ce qui ne marche pas.', 'Je dois réparer cette fonctionnalité.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'يُصلح','arabe', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'développer','mot','Créer/améliorer une application.', 'Je développe une application.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'يطوّر','arabe', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'partager','mot','Donner à d’autres personnes.', 'Je partage mon code sur GitHub.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'يشارك','arabe', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'responsable','mot','Qui assume une tâche.', 'Je suis responsable du projet.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'مسؤول','arabe', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'important','mot','Qui a beaucoup de valeur.', 'C’est important de réviser.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'مهم','arabe', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'rapide','mot','Qui va vite.', 'Mon PC est rapide.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'سريع','arabe', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'lent','mot','Qui va doucement.', 'Internet est lent aujourd’hui.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'بطيء','arabe', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'révision','mot','Action de revoir pour apprendre.', 'Je fais une révision avant l’examen.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'مراجعة','arabe', last_insert_rowid());


INSERT INTO vocabulaire VALUES (NULL,'bug','mot','Défaut dans un programme.', 'Ce bug bloque l’application.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'bug','anglais', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'corriger','mot','Supprimer une erreur.', 'Je corrige le code.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'fix','anglais', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'tester','mot','Vérifier si ça fonctionne.', 'Je teste la fonctionnalité.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'test','anglais', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'ajouter','mot','Mettre quelque chose en plus.', 'J’ajoute une option au menu.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'add','anglais', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'supprimer','mot','Enlever définitivement.', 'Je supprime une ligne.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'delete','anglais', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'modifier','mot','Changer une partie.', 'Je modifie le CSS.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'edit','anglais', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'enregistrer','mot','Sauvegarder des données.', 'J’enregistre dans la base.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'save','anglais', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'charger','mot','Récupérer et afficher.', 'Je charge la liste.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'load','anglais', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'afficher','mot','Montrer à l’écran.', 'J’affiche le résultat.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'display','anglais', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'rechercher','mot','Chercher une information.', 'Je recherche un mot.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'search','anglais', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'traduction','mot','Texte dans une autre langue.', 'Je veux une traduction.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'translation','anglais', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'définition','mot','Explication du sens.', 'La définition est claire.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'definition','anglais', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'exemple','mot','Phrase qui illustre.', 'Donne un exemple simple.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'example','anglais', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'donnée','mot','Information stockée.', 'Ces données sont propres.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'data','anglais', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'base de données','mot','Système qui stocke des infos.', 'SQLite est une base de données.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'database','anglais', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'table','mot','Ensemble de lignes et colonnes.', 'La table vocabulaire existe.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'table','anglais', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'clé étrangère','mot','Lien vers une autre table.', 'La clé étrangère relie traduction.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'foreign key','anglais', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'clé primaire','mot','Identifiant unique.', 'id_vocab est une clé primaire.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'primary key','anglais', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'requête','mot','Commande SQL.', 'J’écris une requête SELECT.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'query','anglais', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'sélectionner','mot','Choisir des lignes.', 'Je sélectionne 10 mots.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'select','anglais', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'insérer','mot','Ajouter une ligne dans la BD.', 'J’insère un nouveau mot.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'insert','anglais', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'mettre à jour','mot','Modifier une donnée existante.', 'Je mets à jour la traduction.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'update','anglais', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'commit','mot','Valider les changements.', 'Je fais un commit.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'commit','anglais', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'dépôt','mot','Espace Git pour le code.', 'Mon dépôt est sur GitHub.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'repository','anglais', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'branche','mot','Version parallèle du code.', 'Je travaille sur une branche.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'branch','anglais', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'fusionner','mot','Réunir des branches.', 'Je fusionne main et dev.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'merge','anglais', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'déployer','mot','Mettre en ligne.', 'Je déploie mon site.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'deploy','anglais', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'portfolio','mot','Site qui présente tes projets.', 'Mon portfolio est en ligne.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'portfolio','anglais', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'stage','mot','Expérience professionnelle en entreprise.', 'Je cherche un stage en mai.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'internship','anglais', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'entretien','mot','Discussion de recrutement.', 'J’ai un entretien demain.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'interview','anglais', last_insert_rowid());


INSERT INTO vocabulaire VALUES (NULL,'bonjour','mot','Salutation.', 'Je dis bonjour le matin.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'Azul','kabyle', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'merci','mot','Expression de gratitude.', 'Merci pour ton aide.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'Tanemmirt','kabyle', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'au revoir','mot','Salutation de départ.', 'Au revoir, à demain.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'Ar tufat','kabyle', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'comment ça va ?','mot','Question sur l’état.', 'Comment ça va aujourd’hui ?', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'Mataɣ-tṭ ?','kabyle', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'bien','mot','État positif.', 'Je vais bien.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'Lxir','kabyle', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'maison','mot','Lieu où on habite.', 'Je rentre à la maison.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'Axxam','kabyle', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'école','mot','Lieu d’étude.', 'Je vais à l’école.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'Aɣerbaz','kabyle', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'travail','mot','Activité professionnelle.', 'Je suis au travail.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'Axeddim','kabyle', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'ami','mot','Personne proche.', 'Mon ami m’aide.', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'Ameddak','kabyle', last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'force/courage','mot','Énergie morale.', 'Courage, tu peux le faire !', CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'Tuzmert','kabyle', last_insert_rowid());
"""

les_expressions ="""
INSERT INTO vocabulaire VALUES (NULL,'briser la glace','expression','Commencer une conversation dans une situation tendue.','Il a raconté une blague pour briser la glace.',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'break the ice','anglais',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'c’est du gâteau','expression','Quelque chose de très facile.','Cet exercice, c’est du gâteau.',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'piece of cake','anglais',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'une fois tous les cent ans','expression','Quelque chose de très rare.','Je le vois une fois tous les cent ans.',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'once in a blue moon','anglais',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'mettre dans le mille','expression','Dire exactement la bonne chose.','Tu as mis dans le mille.',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'hit the nail on the head','anglais',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'ne pas être en forme','expression','Se sentir un peu malade.','Aujourd’hui, je ne suis pas en forme.',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'under the weather','anglais',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'s’arrêter pour aujourd’hui','expression','Arrêter de travailler.','On s’arrête pour aujourd’hui.',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'call it a day','anglais',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'revenir à la case départ','expression','Revenir au point de départ.','On est revenus à la case départ.',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'back to square one','anglais',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'coûter les yeux de la tête','expression','Être très cher.','Ce PC coûte les yeux de la tête.',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'cost an arm and a leg','anglais',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'prendre le coup','expression','Commencer à comprendre.','Je commence à prendre le coup avec SQLite.',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'get the hang of it','anglais',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'à long terme','expression','Sur le long terme.','À long terme, ça va t’aider.',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'in the long run','anglais',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'être sur la même longueur d’onde','expression','Être d’accord.','On est sur la même longueur d’onde.',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'on the same page','anglais',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'penser autrement','expression','Penser différemment.','Il faut penser autrement pour résoudre ce bug.',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'think outside the box','anglais',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'reprends-toi','expression','Se calmer / se ressaisir.','Allez, reprends-toi.',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'pull yourself together','anglais',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'tenir pour acquis','expression','Considérer comme acquis.','Ne le tiens pas pour acquis.',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'take it for granted','anglais',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'avoir le trac','expression','Avoir peur avant d’agir.','J’ai le trac avant l’entretien.',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'get cold feet','anglais',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'rater l’essentiel','expression','Ne pas comprendre l’essentiel.','Tu as raté l’essentiel.',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'miss the point','anglais',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'garder un œil sur','expression','Surveiller.','Garde un œil sur ce fichier.',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'keep an eye on','anglais',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'au final','expression','Finalement.','Au final, ça a marché.',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'at the end of the day','anglais',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'apprendre à ses dépens','expression','Apprendre par l’erreur.','J’ai appris à mes dépens.',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'learn the hard way','anglais',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'faire un effort en plus','expression','Faire plus que nécessaire.','Il fait toujours un effort en plus.',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'go the extra mile','anglais',last_insert_rowid());


INSERT INTO vocabulaire VALUES (NULL,'ça va ?','expression','Question sur l’état de quelqu’un.','Ça va aujourd’hui ?',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'Mataɣ-tṭ ?','kabyle',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'pas de problème','expression','Aucune difficulté.','Pas de problème pour moi.',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'Ulac ugur','kabyle',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'bon courage','expression','Encouragement.','Bon courage pour ton examen.',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'Aɛiwnek','kabyle',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'prends ton temps','expression','Ne te presse pas.','Prends ton temps.',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'Xdem s leɛqel','kabyle',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'c’est la vie','expression','Acceptation de la réalité.','C’est la vie.',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'D amkan n tudert','kabyle',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'tout va bien','expression','Situation positive.','Tout va bien maintenant.',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'Kullec lxir','kabyle',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'viens ici','expression','Appel.','Viens ici s’il te plaît.',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'Ddu dagi','kabyle',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'laisse tomber','expression','Abandonner.','Laisse tomber ce bug.',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'Err-it','kabyle',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'fais attention','expression','Avertissement.','Fais attention à toi.',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'Ḥader iman-ik','kabyle',last_insert_rowid());

INSERT INTO vocabulaire VALUES (NULL,'inchallah','expression','Espoir pour le futur.','Inchallah ça marchera.',CURRENT_TIMESTAMP);
INSERT INTO traduction VALUES (NULL,'Inchallah','kabyle',last_insert_rowid());
"""

conn.execute("BEGIN TRANSACTION;")

c.executescript(les_mots)
c.executescript(les_expressions)

conn.commit()
conn.close()

print("\nLa base de données HiMe a été remplie avec succès !")