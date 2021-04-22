import tkinter as tk
from tkinter.ttk import Combobox

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
    print(a)
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

        global Annul

        id1 = 1
        id2 = 2
        id3 = 3

        # Obtenir l'élément sélectionné
        select = listeCombo1.get()
        print("Vous avez sélectionné : '", select, "'")

        if select == "user1":
            Annul = presetUser.format("a","z","e","r","t","y", id1,"u","i","o","p")
            UserInfo.delete("1.0", "end")
            UserInfo.insert(tk.END, Annul)
            return Annul

        elif select == "user2":
            Annul = presetUser.format("a","z","e","r","t","y", id2,"u","i","o","p")
            UserInfo.delete("1.0", "end")
            UserInfo.insert(tk.END, Annul)
            return Annul

        elif select == "userX":
            Annul = presetUser.format("a","z","e","r","t","y", id3,"u","i","o","p")
            UserInfo.delete("1.0", "end")
            UserInfo.insert(tk.END, Annul)
            return Annul

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

    listeAdmin = ["", "user1", "user2", "userX"]
    listeCombo1 = Combobox(label, height=200, width=27, values=listeAdmin)
    listeCombo1.current(0)
    listeCombo1.place(relx=0.3, rely=0.1, relheight=0.05, relwidth=0.4)
    listeCombo1.bind("<<ComboboxSelected>>", UserSelect)

    UserInfo = tk.Text(label)
    UserInfo.insert(tk.END,presetUser.format("", "", "", "", "", "", "", "", "", "", ""))
    UserInfo.place(relx=0.3, rely=0.15, relheight=0.6, relwidth=0.4)

