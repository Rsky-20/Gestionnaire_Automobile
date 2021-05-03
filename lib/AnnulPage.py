import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import messagebox
import lib.DataTool as DT

listeUser = ["Selectionner un utilisateur"] + DT.InformationPersonnel(DT.dfc)
Annul = ""
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


def valide(a, app):
    MsgboxText = """
           Réservation à supprimer : {}
           """.format(a)
    resp = messagebox.askokcancel(title="Voulez-vous Annuler cette réservation ?", message=MsgboxText)

    if resp == True:
        DT.annuler_location(DT.dfc, DT.dfv, id)
        app.destroy()
    else:
        app.destroy()


def Annul_Page(master):
    """
    [Description]

    :param master: master se réfaire à la page parent
    :return:
    """

    def UserSelect(event):
        """
        [description]
        Fonction permettant de choisir la page à ouvrir parmi un menu déroulant

        :return:
        """

        global Annul, listeUser

        # Obtenir l'élément sélectionné
        select = listeCombo1.get()
        print("Vous avez sélectionné : '", select, "'")
        type(select)

        #print(listeUser)
        if select != "Selectionner un utilisateur":
            LUser = select.split(" ")
            print(LUser)

            User = DT.aff_client(DT.dfc, LUser)

            Annul = presetUser.format(User[0], User[1], User[3], "r", "t", "y", User[4], "u", "i", "o", User[-1])

            UserInfo.delete("1.0", "end")
            UserInfo.insert(tk.END, Annul)
            return User[4]
        else:
            Annul = ""
            UserInfo.delete("1.0", "end")
            UserInfo.insert(tk.END, presetUser.format("", "", "", "", "", "", "", "", "", "", ""))
            return Annul

    app = tk.Toplevel(master)
    app.geometry('920x640')
    app.w, app.h = app.winfo_screenwidth(), app.winfo_screenheight()
    app.title("Annulation")

    label = tk.LabelFrame(app, text="Sélectionnez l'utilisateur dont vous voulez annuler la réservation")
    label.place(relheight=1, relwidth=1)

    BtnValide = tk.Button(label, text='Valider', command=lambda: valide(Annul, app))
    BtnValide.place(relx=0.3, rely=0.8, relheight=0.05, relwidth=0.4)

    listeCombo1 = Combobox(label, height=200, width=27, values=listeUser)
    listeCombo1.current(0)
    listeCombo1.place(relx=0.3, rely=0.1, relheight=0.05, relwidth=0.4)
    listeCombo1.bind("<<ComboboxSelected>>", UserSelect)

    UserInfo = tk.Text(label)
    UserInfo.insert(tk.END,presetUser.format("", "", "", "", "", "", "", "", "", "", ""))
    UserInfo.place(relx=0.3, rely=0.15, relheight=0.6, relwidth=0.4)

