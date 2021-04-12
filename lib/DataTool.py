import pandas as pa
import json

p_clients = './data/clients.json'
p_tarifs = './data/tarifs.json'
p_vehicules = './data/vehicules.json'

def enregistrer_json(df, path):
    """
    enregistre un dataframe dans un fichier json

    in :
        df : dataframe à enregistrer
        path : adresse du fichier json a creer
    """
    json_df = json.loads(df.to_json(orient="records"))

    f = open(path, 'w')
    json.dump(json_df, f, indent=2)
    f.close()

def vehicules_libres(path):
    """
    renvoie les véhicules disponibles

    in :
        path : adresse de la base de donnees des vehicules
    return :
        dataframe contenant les véhicules non loués ou réservés
    """
    df = pa.read_json(path)

    mask = df['date_debut'] == ''
    return df[mask]

def km_ok(path, id, km):
    """
    vérifie si le kilométrage renseigné à la cloture
    de la location est valide

    in : 
        path : adresse de la base de donnees des vehicules
        id : nouméro d'idendification du véhicule en question
        km : kilométrage renseigné à la cloture
    return : booléen
        (True si le kilométrage est valide, False sinon)
    """
    df = pa.read_json(path)

    mask = df['id'] == id
    kil = df[mask].iloc[0]['kilometrage']
    return kil < km

def vehicules_loues(path):
    """
    renvoie les véhicules loués ou reservés

    in : 
        path : adresse de la base de donnees des vehicules
    return : dataframe contenant les véhicules loués ou réservés
    """
    dfv = pa.read_json(path)

    mask = dfv['date_debut'] != ''
    d = dfv[mask]
    return d

def annuler_location(path_c, path_v, id):
    """
    libère un véhicule réservé

    in :
        path_c : adresse de la base de donnees des clients
        path_v : adresse de la base de donnees des vehicules
        id : numéro d'identification du véhicule
    """
    dfc = pa.read_json(path_c)
    dfv = pa.read_json(path_v)

    mask = dfv['id']==id
    dfv.loc[mask, ['date_debut', 'date_fin']] = ['', '']

    mask = dfc['id_vehicule']==id
    dfc.loc[mask, ['id_vehicule', 'prix_location']] = [-1, 0]

    enregistrer_json(dfv, path_v)
    enregistrer_json(dfc, path_c)

def terminer_location(path_c, path_v, id, km):
    """
    libère un véhicule à la fin de sa location

    in :
        path_c : adresse de la base de donnees des clients
        path_v : adresse de la base de donnees des vehicules
        id : numéro d'identification du véhicule
    """
    dfc = pa.read_json(path_c)
    dfv = pa.read_json(path_v)

    if km_ok(dfv, id, km):
        mask = dfv['id']==id
        dfv.loc[mask, ['date_debut', 'date_fin', 'kilometrage']] = ['', '', km]

        mask = dfc['id_vehicule']==id
        dfc.loc[mask, ['id_vehicule', 'prix_location']] = [-1, 0]
    
    enregistrer_json(dfv, path_v)
    enregistrer_json(dfc, path_c)

def ajouter_vehicule(path, t, mark, mod, carb, gam, km):
    """
    ajoute un véhicule à la base de données

    in :
        path : adresse de la base de donnees des vehicules
        dic : dictionnaire contenant toutes les caractéristiques du véhicule à ajouter,
            sauf le numéro d'identification ('id' : None)
    """
    dfv = pa.read_json(path)

    id = dfv['id'][len(dfv)-1] + 1

    dfv.loc[dfv.shape[0]] = [id, t, mark, mod, carb, km, gam, '', '']
    enregistrer_json(dfv, path)

def retirer_vehicule(path, id):
    """
    supprime un véhicule de la base de données

    in :
        path : adresse de la base de donnees des vehicules
        id : numéro d'identification du véhicule à supprimer
    """
    dfv = pa.read_json(path)

    mask = dfv['id'] != id
    enregistrer_json(dfv[mask], path)

def export_bdd(path_json, path_csv):
    """
    exporte une base de donnees json sous format csv

    in :
        path_json : adresse de la base de donnees a exporter
        path : chemin où sauvegarder le fichier
    """
    df = pa.read_json(path_json)
    df.to_csv(path_csv, sep=';')

def ajouter_client(path, nom, prenom, age, num_permis):
    """
    ajoute un client à la base de donnees

    in :
        path : adresse de la base de donnees des clients
        nom : nom du client à ajouter
        prenom : prenom du client à ajouter
        age : age du client à ajouter
        num_permis : numéro du permis du client à ajouter
    """
    dfc = pa.read_json(path)

    dfc.loc[dfc.shape[0]] = [nom, prenom, age, num_permis, -1, 0]
    enregistrer_json(dfc, path)

    enregistrer_json(dfc, path)

def retirer_client(path, num_permis):
    """
    supprime un client de la base de donnees

    in :
        path : adresse de la base de donnees des clients
        num_permis : numéro du permis du client à retirer
    """
    dfc = pa.read_json(path)

    mask = dfc['num_permis'] != num_permis
    enregistrer_json(dfc[mask],path)

def changer_tarif(path, gamme, t, prix, assur, caut):
    """
    change le tarif d'une gamme de véhicules

    in :
        path : adresse de la base de donnees des tarifs
        gamme : nom de la gamme dont on veut changer les tarfis
        prix : nouveau prix a attribuer
        assur : nouveau montant d'assurance a attribuer
        caut : nouvelle caution a attribuer 
    """
    dft = pa.read_json(path)

    mask = (dft.gamme==gamme) & (dft.type==t)

    dft.loc[mask, ['prix', 'assurance', 'caution']] = [prix, assur, caut]

    enregistrer_json(dft, path)

# my_dict = {"nom": "G", "prenom": "J", "age": 26, "np": 10000, "dd": "13-04-2021", "df": "15-04-2021", "id": 2, "prix": 2048}
def louer(dfv, dfc, data):
    #On renseigne les dates de debut et de fin de location dans la dataframe dfv
    mask = dfv["id"] == data["id"]  #on selectionne le vehicule d'id "id"
    dfv.loc[mask, ["date_debut", "date_fin"]] = [data["dd"], data["df"]]

    #On verifie si le client existe
    mask = dfc["num_permis"] == data["np"]
    if dfc[mask].empty: #si le client n'est pas enregistre, on l'ajoute
        dfc.loc[dfc.shape[0]] = [data["nom"], data["prenom"], data["age"], data["np"], data["id"], data["prix"]]
    else:   #si le client est enregistre
        dfc.loc[mask, ["age", "id_vehicule", "prix_location"]] = [data["age"], data["id"], data["prix"]]