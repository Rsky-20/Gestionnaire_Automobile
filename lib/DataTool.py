import pandas as pa
import json
import datetime as dt

dfc = pa.read_json('./data/clients.json')
dft = pa.read_json('./data/tarifs.json')
dfv = pa.read_json('./data/vehicules.json')

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

def vehicules_libres(df):
    """
    renvoie les véhicules disponibles

    in :
        df : dataframe de la base de donnees des vehicules
    return :
        dataframe contenant les véhicules non loués ou réservés
    """

    mask = df['date_debut'] == ''
    return df[mask]

def km_ok(df, id, km):
    """
    vérifie si le kilométrage renseigné à la cloture
    de la location est valide

    in : 
        df : dataframe de la base de donnees des vehicules
        id : nouméro d'idendification du véhicule en question
        km : kilométrage renseigné à la cloture
    return : booléen
        (True si le kilométrage est valide, False sinon)
    """

    mask = df['id'] == id
    kil = df[mask].iloc[0]['kilometrage']
    return kil < km

def vehicules_loues(dfv):
    """
    renvoie les véhicules loués ou reservés

    in : 
        df : dataframe de la base de donnees des vehicules
    return : dataframe contenant les véhicules loués ou réservés
    """

    mask = dfv['date_debut'] != ''
    d = dfv[mask]
    return d

def annuler_location(dfc, dfv, id):
    """
    libère un véhicule réservé

    in :
        dfc : dataframe de la base de donnees des clients
        dfv : dataframe de la base de donnees des vehicules
        id : numéro d'identification du véhicule
    """

    mask = dfv['id']==id
    dfv.loc[mask, ['date_debut', 'date_fin']] = ['', '']

    mask = dfc['id_vehicule']==id
    dfc.loc[mask, ['id_vehicule', 'prix_location']] = [-1, 0]


def terminer_location(dfc, dfv, id, km):
    """
    libère un véhicule à la fin de sa location

    in :
        dfc : dataframe de la base de donnees des clients
        dfv : dataframe de la base de donnees des vehicules
        id : numéro d'identification du véhicule
    """

    if km_ok(dfv, id, km):
        mask = dfv['id']==id
        dfv.loc[mask, ['date_debut', 'date_fin', 'kilometrage']] = ['', '', km]

        mask = dfc['id_vehicule']==id
        dfc.loc[mask, ['id_vehicule', 'prix_location']] = [-1, 0]
    

def ajouter_vehicule(dfv, t, mark, mod, carb, gam, km):
    """
    ajoute un véhicule à la base de données

    in :
        dfv : dataframe de la base de donnees des vehicules
        dic : dictionnaire contenant toutes les caractéristiques du véhicule à ajouter,
            sauf le numéro d'identification ('id' : None)
    """

    id = dfv['id'][len(dfv)-1] + 1

    dfv.loc[dfv.shape[0]] = [id, t, mark, mod, carb, km, gam, '', '']


def retirer_vehicule(dfv, id):
    """
    supprime un véhicule de la base de données

    in :
        dfv : dataframe de la base de donnees des vehicules
        id : numéro d'identification du véhicule à supprimer
    """

    mask = dfv['id'] != id
    dfv = dfv[mask]


def export_bdd(df, path_csv):
    """
    exporte une base de donnees json sous format csv

    in :
        path_json : adresse de la base de donnees a exporter
        path : chemin où sauvegarder le fichier
    """
    df.to_csv(path_csv, sep=',')


def import_bdd(path_csv, path_json):
    df = pa.read_csv(path_csv, sep=';')
    enregistrer_json(df, path_json)

    global dfc, dft, dfv

    dfc = pa.read_json('data/clients.json')
    dft = pa.read_json('data/tarifs.json')
    dfv = pa.read_json('data/vehicules.json')

def ajouter_client(dfc, nom, prenom, age, num_permis):
    """
    ajoute un client à la base de donnees

    in :
        path : adresse de la base de donnees des clients
        nom : nom du client à ajouter
        prenom : prenom du client à ajouter
        age : age du client à ajouter
        num_permis : numéro du permis du client à ajouter
    """

    dfc.loc[dfc.shape[0]] = [nom, prenom, age, num_permis, -1, 0]


def retirer_client(dfc, num_permis):
    """
    supprime un client de la base de donnees

    in :
        dfc : dataframe de la base de donnees des clients
        num_permis : numéro du permis du client à retirer
    """
    mask = dfc['num_permis'] != num_permis
    dfc = dfc[mask]

def changer_tarif(dft, gamme, t, prix, assur, caut):
    """
    change le tarif d'une gamme de véhicules

    in :
        dft : dataframe de la base de donnees des tarifs
        gamme : nom de la gamme dont on veut changer les tarfis
        prix : nouveau prix a attribuer
        assur : nouveau montant d'assurance a attribuer
        caut : nouvelle caution a attribuer 
    """
    mask = (dft.gamme==gamme) & (dft.type==t)

    dft.loc[mask, ['prix', 'assurance', 'caution']] = [prix, assur, caut]


def louer(dfv, dfc, num_permis, id, date_debut, date_fin, prix):
    mask = dfv["id"] == id
    dfv.loc[mask, ["date_debut", "date_fin"]] = [date_debut, date_fin]

    mask = dfc["num_permis"] == num_permis

    dfc.loc[mask, ["id_vehicule", "prix_location"]] = [id, prix]

def calculer_prix(dfv, dft, date_debut, date_fin, gamme):
    L_debut = date_debut.split('-')
    L_fin = date_fin.split('-')

    debut = dt.date(int(L_debut[2]), int(L_debut[1]), int(L_debut[0]))
    fin = dt.date(int(L_fin[2]), int(L_fin[1]), int(L_fin[0]))
    duree = (fin-debut).days

    mask = (dft.gamme==gamme)
    prix, assurance = int(dft[mask]['prix']), int(dft[mask]['assurance'])

    return (fin-debut).days*(prix+assurance)

#afficher des informations personnelles
def InformationPersonnel(dfc):
    return(list(dfc["nom"] + " " + dfc["prenom"]))

def InformationPersonnelClientReserver(dfc):
    mask = dfc["id_vehicule"] != -1
    return(list(dfc[mask]["nom"] + " " + dfc[mask]["prenom"]))


def aff_client(dfc):
    return dfc.to_string(index=False)

def aff_info_client(dfc, nom_prenom):
    mask = (dfc.nom==nom_prenom[0]) & (dfc.prenom==nom_prenom[1])
    return dfc[mask].values[0].tolist()

def aff_vehicule(dfv):
    return dfv.to_string(index=False)

def aff_vehicule_id(dfv, id):
    mask = dfv["id"] == id
    return dfv[mask].values[0].tolist()

# Afficher le tarif au utilisateur
def aff_tarifs():
    return dft.to_string(index=False)

def aff_reservation(dfc):
    """
    
    """
    pass

if __name__=='__main__':
    #TESTS
    print(aff_vehicule_id(dfv, 42))
    #print(InformationPersonnelClientReserver(dfc))
    #print(aff_info_client(dfc, ["Vaudry","Pierre"]))
    retirer_vehicule(dfv, 42)
    print(aff_vehicule(dfv))
    #enregistrer_json(dfv, "./test.json")
    
    #print(aff_vehicule_id(dfv, 42))

    #retirer_client(dfc, 10005)
    #print(aff_info_client(dfc, ["Vaudry","Pierre"]))
