import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import messagebox
import lib.DataTool as DT
import lib.grille_vehicule_dispo as gvd

listeUser = ["Selectionner un utilisateur"] + DT.InformationPersonnel(DT.dfc)
reservation = int()
selectedUser = []
presetReservation = """
------------Information client-----------

Nom: {}
Prenom: {}
Numero permis: {}

---------Information reservation---------

date de début de réservation: {}
date de fin de réservation: {}
id vehicle: {}
véhicule: {}
catégorie: {}
assurance: {}
prix: {}
"""


def valide(num_permis, id_vehicule, date_debut, date_fin, assurance, app):
    
    if num_permis or id_vehicule == 0 and date_debut or date_fin == "":
        msgboxText = """
           Il y a une erreur dans les information renseignées. 
           Merci de bien vouloir les vérifier. 
           """
        messagebox.showerror(title="ERROR", message=msgboxText)
    
    msgboxText = """
           Information de Réservation : 
           Numéro de permis client : {}
           Id véhicule : {}
           Date de début : {}
           Date de fin : {}
           Sousciption assurance : {}
           """.format(num_permis, id_vehicule, date_debut, date_fin, assurance)
    resp = messagebox.askokcancel(title="Voulez-vous annuler cette réservation ?", message=msgboxText)

    if resp == True:
        
        gamme = DT.aff_vehicule(DT.dfv, id_vehicule)
        print(gamme)
        print(gamme[5])
        
        prix = DT.calculer_prix(DT.dfv, DT.dft, date_debut, date_fin, gamme[5])
        print(prix)
        
        DT.louer(DT.dfv, DT.dfc, num_permis, id_vehicule, date_debut, date_fin, prix)
        DT.aff_client(DT.dfc, selectedUser)
        app.destroy()
    else:
        app.destroy()

def reserv_page(master):
    """
    [Description]

    :param master: master se réfaire à la page parent
    :return:
    """

    app = tk.Toplevel(master)
    h = app.winfo_screenheight()
    w = app.winfo_screenwidth()
    screen = str(round(w*0.748)) +"x" + str(round(h*0.91)) + "+" + str(round(w*0.246)) + "+" + str(round(h*0.052))
    app.geometry(screen)
    app.attributes("-toolwindow", 1)  # Supprime les boutons Réduire/Agrandir
    app.transient(master)
    app.resizable(False, False)
    app.title("Réservation")
    
    def user_select(event):
        """
        [description]
        Fonction permettant de choisir la page à ouvrir parmi un menu déroulant

        :return:
        """

        global reservation, listeUser, selectedUser

        # Obtenir l'élément sélectionné
        select = listeCombo1.get()
        print("Vous avez sélectionné : '", select, "'")
        type(select)

        #print(listeUser)
        if select != "Selectionner un utilisateur":
            selectedUser = select.split(" ")
            print(selectedUser)

            user = DT.aff_info_client(DT.dfc, selectedUser)

            annul = presetReservation.format(user[0], user[1], user[3], None, None, None, None, None, None, None, None)

            userInfo.delete("1.0", "end")
            userInfo.insert(tk.END, annul)
            print(user[3])
            reservation = user[3]
            
        else:
            annul = ""
            userInfo.delete("1.0", "end")
            userInfo.insert(tk.END, presetReservation.format("", "", "", "", "", "", "", "", "", "", ""))
            
        
    label = tk.LabelFrame(app, text="Sélectionnez l'utilisateur pour la réservation")
    label.place(relheight=1, relwidth=1)

    listeCombo1 = Combobox(label, height=200, width=27, values=listeUser)
    listeCombo1.current(0)
    listeCombo1.place(relx=0.1, rely=0.1, relheight=0.05, relwidth=0.2)
    listeCombo1.bind("<<ComboboxSelected>>", user_select)
    
    varIdVehi = tk.IntVar()
    tk.LabelFrame(app, text="Id Véhicule").place(
        relx=0.1, rely=0.21, relheight=0.09, relwidth=0.2)
    tk.Entry(app, width=14, textvariable=varIdVehi).place(
        relx=0.11, rely=0.235, relheight=0.05, relwidth=0.18) 
    
    varDateDebut = tk.StringVar()
    tk.LabelFrame(app, text="Date de début").place(
        relx=0.1, rely=0.41, relheight=0.09, relwidth=0.2)
    tk.Entry(app, width=14, textvariable=varDateDebut).place(
        relx=0.11, rely=0.435, relheight=0.05, relwidth=0.18) 
    
    varDateFin = tk.StringVar()
    tk.LabelFrame(app, text="Date de début").place(
        relx=0.1, rely=0.51, relheight=0.09, relwidth=0.2)
    tk.Entry(app, width=14, textvariable=varDateFin).place(
        relx=0.11, rely=0.535, relheight=0.05, relwidth=0.18) 
    
    varAssurance = tk.StringVar()
    assuranceBouton = tk.Checkbutton(app, text="Voulez vous souscrire à une assurance ?", variable=varAssurance)
    assuranceBouton.deselect()
    assuranceBouton.place(relx=0.1, rely=0.61, relheight=0.09, relwidth=0.2)
    
    # Affiche avec un bouton une liste de véhicule disponible
    dispoVehicule = tk.Button(app, text='Afficher véhicule disponible', command=lambda:gvd.run(app))
    dispoVehicule.place(relx=0.1, rely=0.31, relheight=0.09, relwidth=0.2)
    
    userInfo = tk.Text(label)
    userInfo.insert(tk.END,presetReservation.format("", "", "", "", "", "", "", "", "", "", ""))
    userInfo.place(relx=0.5, rely=0.1, relheight=0.6, relwidth=0.4)
    
    BtnValide = tk.Button(label, text='Valider',
                          command=lambda: valide(reservation, varIdVehi.get(),
                                                 varDateDebut.get(), varDateFin.get(),
                                                 varAssurance.get(), app))
    BtnValide.place(relx=0.3, rely=0.8, relheight=0.05, relwidth=0.4)