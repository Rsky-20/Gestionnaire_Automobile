import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import messagebox
import lib.DataTool as DT

listeUser = ["Selectionner un utilisateur"] + DT.InformationPersonnel(DT.dfc)
reservation = ""
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


def valide(reservationInfo, app):
    msgboxText = """
           Réservation à supprimer : {}
           """.format(None)
    resp = messagebox.askokcancel(title="Voulez-vous annuler cette réservation ?", message=msgboxText)

    if resp == True:
        #DT.louer(DT.dfv, DT.dfc, num_permis, id, date_debut, date_fin, prix)
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
    app.geometry('920x640+500+125')
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

        global annul, listeUser

        # Obtenir l'élément sélectionné
        select = listeCombo1.get()
        print("Vous avez sélectionné : '", select, "'")
        type(select)

        #print(listeUser)
        if select != "Selectionner un utilisateur":
            selectedUser = select.split(" ")
            print(selectedUser)

            user = DT.aff_client(DT.dfc, selectedUser)

            annul = presetReservation.format(user[0], user[1], user[3], None, None, None, None, None, None, None, None)

            userInfo.delete("1.0", "end")
            userInfo.insert(tk.END, annul)
            return user[4]
        else:
            annul = ""
            userInfo.delete("1.0", "end")
            userInfo.insert(tk.END, presetReservation.format("", "", "", "", "", "", "", "", "", "", ""))
            return annul
        
    label = tk.LabelFrame(app, text="Sélectionnez l'utilisateur pour la réservation")
    label.place(relheight=1, relwidth=1)

    listeCombo1 = Combobox(label, height=200, width=27, values=listeUser)
    listeCombo1.current(0)
    listeCombo1.place(relx=0.1, rely=0.1, relheight=0.05, relwidth=0.4)
    listeCombo1.bind("<<ComboboxSelected>>", user_select)
    
    
    varIdVehi = tk.IntVar()
    tk.LabelFrame(app, text="Id Véhicule").place(
        relx=0.1, rely=0.21, relheight=0.09, relwidth=0.2)
    tk.Entry(app, width=14, textvariable=varIdVehi).place(
        relx=0.11, rely=0.235, relheight=0.05, relwidth=0.18) 
    
    varDateDebut = tk.StringVar()
    tk.LabelFrame(app, text="Date de début").place(
        relx=0.1, rely=0.31, relheight=0.09, relwidth=0.2)
    tk.Entry(app, width=14, textvariable=varDateDebut).place(
        relx=0.11, rely=0.335, relheight=0.05, relwidth=0.18) 
    
    varDateFin = tk.StringVar()
    tk.LabelFrame(app, text="Date de début").place(
        relx=0.1, rely=0.41, relheight=0.09, relwidth=0.2)
    tk.Entry(app, width=14, textvariable=varDateFin).place(
        relx=0.11, rely=0.435, relheight=0.05, relwidth=0.18) 

    userInfo = tk.Text(label)
    userInfo.insert(tk.END,presetReservation.format("", "", "", "", "", "", "", "", "", "", ""))
    userInfo.place(relx=0.5, rely=0.1, relheight=0.6, relwidth=0.4)
    
    assuranceBouton = tk.Checkbutton(app, text="Voulez vous souscrire à une assurance ?")
    assuranceBouton.place()
    
    BtnValide = tk.Button(label, text='Valider', command=lambda: valide(0, app))
    BtnValide.place(relx=0.3, rely=0.8, relheight=0.05, relwidth=0.4)