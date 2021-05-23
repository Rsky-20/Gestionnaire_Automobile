import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import messagebox
import lib.DataTool as DT

listeUser = ["Selectionner un utilisateur"] + DT.InformationPersonnel(DT.dfc)
annul = ""
presetUser = """
Nom: {}
Prenom: {}
Numero permis: {}
Tel: {}
Email: {}

---------Information de reservation---------

date de reservation: {}
id vehicle: {}
vehicul: {}
categorie: {}
assurance: {}
prix: {}

"""


def valide(annulationInfo, app):
    msgboxText = """
           Réservation à supprimer : {}
           """.format(annulationInfo)
    resp = messagebox.askokcancel(title="Voulez-vous annuler cette réservation ?", message=msgboxText)

    if resp == True:
        DT.annuler_location(DT.dfc, DT.dfv, id)
        app.destroy()
    else:
        app.destroy()


def annul_page(master):
    """
    [Description]

    :param master: master se réfaire à la page parent
    :return:
    """

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

            annul = presetUser.format(user[0], user[1], user[3], "r", "t", "y", user[4], "u", "i", "o", user[-1])

            userInfo.delete("1.0", "end")
            userInfo.insert(tk.END, annul)
            return user[4]
        else:
            annul = ""
            userInfo.delete("1.0", "end")
            userInfo.insert(tk.END, presetUser.format("", "", "", "", "", "", "", "", "", "", ""))
            return annul

    app = tk.Toplevel(master)
    app.geometry('1148x786+378+45')
    app.attributes("-toolwindow", 1)  # Supprime les boutons Réduire/Agrandir
    app.transient(master)
    app.resizable(False, False)
    app.title("Annulation")

    label = tk.LabelFrame(app, text="Sélectionnez l'utilisateur dont vous voulez annuler la réservation")
    label.place(relheight=1, relwidth=1)

    BtnValide = tk.Button(label, text='Valider', command=lambda: valide(annul, app))
    BtnValide.place(relx=0.3, rely=0.8, relheight=0.05, relwidth=0.4)

    listeCombo1 = Combobox(label, height=200, width=27, values=listeUser)
    listeCombo1.current(0)
    listeCombo1.place(relx=0.3, rely=0.1, relheight=0.05, relwidth=0.4)
    listeCombo1.bind("<<ComboboxSelected>>", user_select)

    userInfo = tk.Text(label)
    userInfo.insert(tk.END,presetUser.format("", "", "", "", "", "", "", "", "", "", ""))
    userInfo.place(relx=0.3, rely=0.15, relheight=0.6, relwidth=0.4)

