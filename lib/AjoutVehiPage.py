import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import messagebox
import lib.DataTool as DT

listeUser = ["Selectionner un utilisateur"] + DT.InformationPersonnel(DT.dfc)
selectedUser = []
presetVehicule = """
------------Information véhicule-----------

Nom: {}
Prenom: {}
Numero permis: {}

"""

def valide(ajoutInfo, app):
    MsgboxText = """
           Véhicule à ajouter : {}
           """.format(ajoutInfo)
    resp = messagebox.askokcancel(title="Voulez-vous Ajouter ce véhicules ?", message=MsgboxText)

    if resp == True:
        print(ajoutInfo)
        app.destroy()
    else:
        app.destroy()

def ajout_vehi_page(master):
    """
    [Description]

    :param master: master se réfaire à la page parent
    :return:
    """

    app = tk.Toplevel(master)
    app.geometry('1148x786+378+45')
    app.attributes("-toolwindow", 1)# Supprime les boutons Réduire/Agrandir
    app.transient(master)
    app.resizable(False, False)
    app.title("Ajout Véhicle")
    
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

            user = DT.aff_client(DT.dfc, selectedUser)

            annul = presetReservation.format(user[0], user[1], user[3], None, None, None, None, None, None, None, None)

            userInfo.delete("1.0", "end")
            userInfo.insert(tk.END, annul)
            print(user[3])
            reservation = user[3]
            
        else:
            annul = ""
            userInfo.delete("1.0", "end")
            userInfo.insert(tk.END, presetReservation.format("", "", "", "", "", "", "", "", "", "", ""))
            
    
    label = tk.LabelFrame(app, text="Sélectionnez l'utilisateur")
    label.place(relheight=1, relwidth=1)

    listeCombo1 = Combobox(label, height=200, width=27, values=listeUser)
    listeCombo1.current(0)
    listeCombo1.place(relx=0.1, rely=0.1, relheight=0.05, relwidth=0.2)
    listeCombo1.bind("<<ComboboxSelected>>", user_select)
