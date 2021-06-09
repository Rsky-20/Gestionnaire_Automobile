# ``` Grand Projet de Programmation IPSA 2021 ```
## Gestionnaire_Automobile

L’objectif de ce projet est de mettre en place un système de gestion de véhicules pour une agence de  location.Le projet doit permettre de gérer les véhicules, les locations ainsi que le côté administration de l’agence (annulation commande, rajout d’un client ou d’un véhicule ainsi que leurs annulations).

## Cahier des charges

L’application python doit permettre d’effectuer les actions suivantes :
•	Louer un véhicule
•	Afficher les locations actuelles
•	Annuler une location 
•	Terminer une location 
•	Modifier le parc automobile

## Organisation du projet

Afin de concevoir l’application python, le projet est divisé en deux parties :
•	Une partie : implémentation du système de gestion (fonctions de contrôle fait par Jessy José et Luc Vierne)
•	Une partie : implémentation de l’interface graphique permettant de gérer l’agence de location (fait par Enora Guillaume et Pierre Vaudry)
Le code est conçu à l’aide de Pycharm Visual Studio Code, IDLE pour la programmation.
Le projet est sauvegardé en temps réelle sur Github, afin d’avoir une gestion de version, ce service (ainsi que l’application Github Desktop) nous permet de gérer le projet de façon global depuis n’importe où et sans besoin de concertation journalière. 
Chaque partie peut être fait indépendamment tout en ayant une visibilité sur le reste du projet.
Cependant, dans l’optique de diriger le projet dans une et même direction, nous avons fait des réunions et des deadlines interne. Durant ces réunions, nous avons pue nous concerter sur l’évolution du projet ainsi que les tâches à effectuer.



# Partie I : Système de Gestion

## Introduction 
Un système de gestion de base de données est un logiciel système servant à stocker, à manipuler ou gérer, et à partager des données dans une base de données, en garantissant la qualité, la pérennité et la confidentialité des informations, tout en cachant la complexité des opérations.
 
C'est une partie primordiale de ce projet, cette partie contient les fonctions qui seront sollicitées pour répondre efficacement au cahier des charges. 
La partie système de gestion, comme le projet en lui-même, nécessite énormément de communication entre les fonctions, ainsi qu’avec la partie interface graphique.
 
Nous avons coupé la conception de cette partie en trois. Premièrement, nous avons répondu optimalement au cahier des charges imposé par le professeur. Deuxièmement, nous nous sommes réunies afin de vérifier la bonne cohésion de nos travaux avec l'équipe chargée de l’interface graphique et nous fixer un nouveau cahier des charges, pour enrichir et repousser les frontières de ce projet. Et enfin nous avons essayé, au mieux possible, de répondre à ce nouvel objectif. 

  
 
## Cahier des charges  
 
L’objectif de ce projet est de mettre en place un système de gestion de véhicules pour une agence de location. 
Votre solution permettra de réaliser, au minimum, les actions suivantes : 

1)Louer un véhicule 

2)Afficher les locations actuelles 

3)Annuler une location 

4)Terminer une location 

5)Modifier le parc automobile 


## Réalisation des fonctions 

1.	Louer le véhicule 
  
    On commence par modifier les informations relatives au véhicule pour le réserver. Pour cela, on l’isole dans la base de données grâce à son numéro d’identification, noté “id”. Une fois cela fait, on modifie ses attributs “date_debut” et “date_fin” pour indiquer au système que ce véhicule est loué. Ensuite, on modifie les informations relatives au client. Comme pour le véhicule, on l’isole grâce  à son numéro de permis, puis on modifie dans la base de données l’id du véhicule loué et le prix que la location coûtera au client.

2.	Afficher les locations actuelles
 
    Pour afficher l’ensemble des locations actuelles, on commence par créer un dataframe vide, contenant les colonnes suivantes : 

    •	Nom et prénom du client

    •	date de début et de fin de la location

    •	id, gamme et type du véhicule loué

    •	prix de la location

Ensuite, on extrait de la base de données tous les clients ayant une réservation en cours. En parcourant chaque client, on remplit les lignes du dataframe avec toutes les informations.

3.	Annuler une location
 
    Pour annuler une location, on commence par supprimer les dates de début et de fin de location du véhicule dans la base de données pour libérer le véhicule. Après ça, on peut remettre la valeur de l’id du véhicule loué à la valeur par défaut (-1) pour signifier que plus aucun véhicule n’est loué par le client, et remettre le prix de sa location à 0.

4.	Terminer une location
 
    La première étape est de vérifier si le kilométrage annoncé au retour est cohérent. Pour cela, on a créé une fonction km_ok qui vérifie que le kilométrage est supérieur au kilométrage avant la location. Si le kilométrage est cohérent, alors procède de la même manière que pour l’annulation, en modifiant d’abord les informations liées au véhicule, puis celles du client.

5.	Modifier le parc Automobile

    La modification du parc automobile se fait grâce à trois fonctions. La première est la fonction “ajouter_vehicule” :

    Cette fonction prend en argument le dataframe contenant tous les véhicules de la flotte, et les informations relatives au véhicule à ajouter. Pour l’attribution de l’identifiant, on ajoute 1 à l’id du dernier véhicule de la liste. On ajoute ensuite un nouvel élément au dataframe, contenant toutes les informations du véhicule.
    La deuxième fonction est la fonction “modifier_vehicule” :

    Les arguments sont les mêmes que la fonction précédente, mais en renseignant le numéro d’identification du véhicule. La fonction va alors isoler le véhicule recherché, puis mettre à jour toutes ses données.
    La dernière fonction est “retirer_vehicule”:

    Elle isole le véhicule recherché et le supprime du dataframe. Cette fonction ne modifie pas la variable globale mais retourne le nouveau dataframe actualisé, il faut donc l’utiliser de la manière suivante:

        dfv = retirer_vehicule(dfv, id)




# Partie II : Interface Graphique
## Introduction
	
L’interface graphique est un élément essentiel, il permet à l’utilisateur d’interagir avec les outils de gestion (fonction / processus fait par notre équipe responsable de cette partie). Cette interface doit être ergonomique, simple et intuitive. 
Afin de répondre au mieux à ces critères, nous avons décidé de couper la conception graphique en plusieurs étapes : 
•	Etape 1 : Cahier des charges et réflexion sur les problématiques, les aboutissements 
•	Etape 2 : Conception des Templates et de l’idée générale sur papier
•	Etape 3 : Création du squelette, de l’application en programmation orienté objet
•	Etape 4 : Répartition des pages à effectuer une fois le squelette en place
•	Etape 5 : Implémentation des fonctionnalités à travers l’interface graphique

## Cahier des charges de l’interface graphique

Pour suivre une ligne directive dans la conception de l’interface graphique nous avons mis en place un cahier des charges pour notre partie.
En effet, il est essentiel de définir les besoins, les problèmes possibles ainsi que les demandes du potentiel client. Nous nous sommes donc mis du côté client/utilisateur, et nous avons fait un travail de réflexion. 
A l’issu de notre réflexion lors de l’une de nos premières réunions, nous avons abouti à la rédaction du cahier des charges suivant :

    i.	L’interface graphique doit être simple et intuitive

    ii.	L’interface doit permettre l’utilisation de toutes les fonctions faites par notre seconde équipe 

    iii.	L’interface doit être instancié si jamais nous voulons l’exporter dans une autre application

    iv.	Comme demandé, l’interface des pages/fonctionnalités doivent être faite dans des fichiers python importé sous forme de module 

    v.	L’interface doit répondre avant tout à une utilisation au niveau d’une entreprise (et non une utilisation personnelle)

    vi.	La programmation de l’interface doit répondre aux normes de programmation demandé (documentations/nom de classes, fonctions, variables clair et qui respecte les règles de programmation voir document annexe)


## Conception des Templates
	
Une fois le cahier des charges effectué, nous avons conçu des templates sur papier (voir annexe). Les templates nous ont permis d’appliquer sur papier le cahier des charges et nous ont permis d’avoir un visuel définit pour la suite.

## Création du squelette

	Après avoir fait les templates, il était essentiel de créer le squelette de l’application, c’est-à-dire, la création de la base permettant de lié l’interface graphique principale ainsi que les différente page faisant intervenir différentes fonctions et outils. 

Le squelette étant très important, nous avons eu quelque difficulté pour le mettre en place. En effet, nous voulions en faire un objet et l’instancié. Cela nous a demandé de la réflexion et du travail. 
Cependant, cette instanciation nous permet de pouvoir si besoin exporter ce projet sous forme d’autre projet. 
En effet, le programme App.py 




