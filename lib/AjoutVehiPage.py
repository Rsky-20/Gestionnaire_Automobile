import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import messagebox
import lib.DataTool as DT

def valide(a, app):
    MsgboxText = """
           Réservation à supprimer : {}
           """.format(a)
    resp = messagebox.askokcancel(title="Voulez-vous Annuler cette réservation ?", message=MsgboxText)

    if resp == True:
        print(a)
        app.destroy()
    else:
        app.destroy()

def AjoutVehi_Page(master):
    """
    [Description]

    :param master: master se réfaire à la page parent
    :return:
    """

    def selecType(event):
        """
        [description]
        Fonction permettant de choisir la page à ouvrir parmi un menu déroulant

        :return:
        """

        global selecType

        id1 = 1
        id2 = 2
        id3 = 3

        # Obtenir l'élément sélectionné
        select = listeCombo1.get()
        print("Vous avez sélectionné : '", select, "'")

        if selecType == "U":
            Annul = presetUser.format("a","z","e","r","t","y", id1,"u","i","o","p")
            UserInfo.delete("1.0", "end")
            UserInfo.insert(tk.END, Annul)
            return Annul

        elif selecType == "T":
            Annul = presetUser.format("a","z","e","r","t","y", id2,"u","i","o","p")
            UserInfo.delete("1.0", "end")
            UserInfo.insert(tk.END, Annul)
            return Annul

        else:
            Annul = ""
            UserInfo.delete("1.0", "end")
            UserInfo.insert(tk.END, presetUser.format("", "", "", "", "", "", "", "", "", "", ""))
            return Annul

    def selecMarque(event):
        """
        [description]
        Fonction permettant de choisir la page à ouvrir parmi un menu déroulant

        :return:
        """

        global selecMarque

        id1 = 1
        id2 = 2
        id3 = 3

        # Obtenir l'élément sélectionné
        select = listeCombo1.get()
        print("Vous avez sélectionné : '", select, "'")

        
        if selecMarque == "PEUGEOT":
            Annul = presetUser.format("a","z","e","r","t","y", id1,"u","i","o","p")
            UserInfo.delete("1.0", "end")
            UserInfo.insert(tk.END, Annul)
            return Annul

        elif selecMarque == "FERRARI":
            Annul = presetUser.format("a","z","e","r","t","y", id2,"u","i","o","p")
            UserInfo.delete("1.0", "end")
            UserInfo.insert(tk.END, Annul)
            return Annul

        elif selecMarque == "VOLKSWAGEN":
            Annul = presetUser.format("a","z","e","r","t","y", id3,"u","i","o","p")
            UserInfo.delete("1.0", "end")
            UserInfo.insert(tk.END, Annul)
            return Annul

        elif selecMarque == "RENAULT":
            Annul = presetUser.format("a","z","e","r","t","y", id4,"u","i","o","p")
            UserInfo.delete("1.0", "end")
            UserInfo.insert(tk.END, Annul)
            return Annul

        elif selecMarque == "MERCEDES":
            Annul = presetUser.format("a","z","e","r","t","y", id5,"u","i","o","p")
            UserInfo.delete("1.0", "end")
            UserInfo.insert(tk.END, Annul)
            return Annul

        elif selecMarque == "PORSCHE":
            Annul = presetUser.format("a","z","e","r","t","y", id6,"u","i","o","p")
            UserInfo.delete("1.0", "end")
            UserInfo.insert(tk.END, Annul)
            return Annul

        elif selecMarque == "AUDI":
            Annul = presetUser.format("a","z","e","r","t","y", id7,"u","i","o","p")
            UserInfo.delete("1.0", "end")
            UserInfo.insert(tk.END, Annul)
            return Annul

        elif selecMarque == "TESLA":
            Annul = presetUser.format("a","z","e","r","t","y", id8,"u","i","o","p")
            UserInfo.delete("1.0", "end")
            UserInfo.insert(tk.END, Annul)
            return Annul

        elif selecMarque == "IVECO":
            Annul = presetUser.format("a","z","e","r","t","y", id9,"u","i","o","p")
            UserInfo.delete("1.0", "end")
            UserInfo.insert(tk.END, Annul)
            return Annul

        else:
            Annul = ""
            UserInfo.delete("1.0", "end")
            UserInfo.insert(tk.END, presetUser.format("", "", "", "", "", "", "", "", "", "", ""))
            return Annul

    def selecGamme(event):
        """
        [description]
        Fonction permettant de choisir la page à ouvrir parmi un menu déroulant

        :return:
        """

        global selecGamme

        id1 = 1
        id2 = 2
        id3 = 3

        # Obtenir l'élément sélectionné
        select = listeCombo1.get()
        print("Vous avez sélectionné : '", select, "'")

        if selecGamme == "SUV":
            Annul = presetUser.format("a","z","e","r","t","y", id1,"u","i","o","p")
            UserInfo.delete("1.0", "end")
            UserInfo.insert(tk.END, Annul)
            return Annul

        elif selecGamme == "BERLINE":
            Annul = presetUser.format("a","z","e","r","t","y", id2,"u","i","o","p")
            UserInfo.delete("1.0", "end")
            UserInfo.insert(tk.END, Annul)
            return Annul

        elif selecGamme == "MONOSPACE":
            Annul = presetUser.format("a","z","e","r","t","y", id3,"u","i","o","p")
            UserInfo.delete("1.0", "end")
            UserInfo.insert(tk.END, Annul)
            return Annul

        elif selecGamme == "SPORTIVE":
            Annul = presetUser.format("a","z","e","r","t","y", id3,"u","i","o","p")
            UserInfo.delete("1.0", "end")
            UserInfo.insert(tk.END, Annul)
            return Annul

        elif selecGamme == "ELECTRIQUE":
            Annul = presetUser.format("a","z","e","r","t","y", id3,"u","i","o","p")
            UserInfo.delete("1.0", "end")
            UserInfo.insert(tk.END, Annul)
            return Annul

        elif selecGamme == "BENNE":
            Annul = presetUser.format("a","z","e","r","t","y", id3,"u","i","o","p")
            UserInfo.delete("1.0", "end")
            UserInfo.insert(tk.END, Annul)
            return Annul

        elif selecGamme == "3 A 5":
            Annul = presetUser.format("a","z","e","r","t","y", id3,"u","i","o","p")
            UserInfo.delete("1.0", "end")
            UserInfo.insert(tk.END, Annul)
            return Annul

        elif selecGamme == "6 A 10":
            Annul = presetUser.format("a","z","e","r","t","y", id3,"u","i","o","p")
            UserInfo.delete("1.0", "end")
            UserInfo.insert(tk.END, Annul)
            return Annul

        elif selecGamme == "11 A 15":
            Annul = presetUser.format("a","z","e","r","t","y", id3,"u","i","o","p")
            UserInfo.delete("1.0", "end")
            UserInfo.insert(tk.END, Annul)
            return Annul

        elif selecGamme == "20 A 25":
            Annul = presetUser.format("a","z","e","r","t","y", id3,"u","i","o","p")
            UserInfo.delete("1.0", "end")
            UserInfo.insert(tk.END, Annul)
            return Annul

        else:
            Annul = ""
            UserInfo.delete("1.0", "end")
            UserInfo.insert(tk.END, presetUser.format("", "", "", "", "", "", "", "", "", "", ""))
            return Annul

    def selecModel(event):
        """
        [description]
        Fonction permettant de choisir la page à ouvrir parmi un menu déroulant

        :return:
        """

        global selec

        id1 = 1
        id2 = 2
        id3 = 3

        # Obtenir l'élément sélectionné
        select = listeCombo1.get()
        print("Vous avez sélectionné : '", select, "'")

        if select == "PEUGEOT":
            Annul = presetUser.format("a","z","e","r","t","y", id1,"u","i","o","p")
            UserInfo.delete("1.0", "end")
            UserInfo.insert(tk.END, Annul)
            return Annul

        elif select == "FERRARI":
            Annul = presetUser.format("a","z","e","r","t","y", id2,"u","i","o","p")
            UserInfo.delete("1.0", "end")
            UserInfo.insert(tk.END, Annul)
            return Annul

        elif select == "VOLKSWAGEN":
            Annul = presetUser.format("a","z","e","r","t","y", id3,"u","i","o","p")
            UserInfo.delete("1.0", "end")
            UserInfo.insert(tk.END, Annul)
            return Annul

        elif select == "RENAULT":
            Annul = presetUser.format("a","z","e","r","t","y", id3,"u","i","o","p")
            UserInfo.delete("1.0", "end")
            UserInfo.insert(tk.END, Annul)
            return Annul

        elif select == "MERCEDES":
            Annul = presetUser.format("a","z","e","r","t","y", id3,"u","i","o","p")
            UserInfo.delete("1.0", "end")
            UserInfo.insert(tk.END, Annul)
            return Annul

        elif select == "PORSCHE":
            Annul = presetUser.format("a","z","e","r","t","y", id3,"u","i","o","p")
            UserInfo.delete("1.0", "end")
            UserInfo.insert(tk.END, Annul)
            return Annul

        elif select == "AUDI":
            Annul = presetUser.format("a","z","e","r","t","y", id3,"u","i","o","p")
            UserInfo.delete("1.0", "end")
            UserInfo.insert(tk.END, Annul)
            return Annul

        elif select == "TESLA":
            Annul = presetUser.format("a","z","e","r","t","y", id3,"u","i","o","p")
            UserInfo.delete("1.0", "end")
            UserInfo.insert(tk.END, Annul)
            return Annul

        elif select == "IVECO":
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
    app.geometry('920x640+500+125')
    app.attributes("-toolwindow", 1)# Supprime les boutons Réduire/Agrandir
    app.transient(master)
    app.resizable(False, False)
    app.title("Ajout Véhicle")

    label = tk.LabelFrame(app, text="Sélectionnez l'utilisateur dont vous voulez annuler la réservation")
    label.place(relheight=1, relwidth=1)

    BtnValide = tk.Button(label, text='Valider', command=lambda: valide(Annul, app))
    BtnValide.place(relx=0.3, rely=0.8, relheight=0.05, relwidth=0.4)

    listeType = ["Type a selectionner", "U", "T"]
    listeCombo1 = Combobox(label, height=200, width=27, values=listeType)
    listeCombo1.current(0)
    listeCombo1.place(relx=0.3, rely=0.1, relheight=0.05, relwidth=0.4)
    listeCombo1.bind("<<ComboboxSelected>>", selecType)

    listeMarque = ["Marque a selectionner", "PEUGEOT", "FERRARI", "VOLKSWAGEN", "RENAULT", "MERCEDES", "PORSCHE", "AUDI", "TESLA", "IVECO"]
    listeCombo2 = Combobox(label, height=200, width=27, values=listeMarque)
    listeCombo2.current(0)
    listeCombo2.place(relx=0.3, rely=0.15, relheight=0.05, relwidth=0.4)
    listeCombo2.bind("<<ComboboxSelected>>", selecMarque)

    listeModel = ["Model a selectionner", "MONOSPACE", "SUV", "BERLIN", "SPORTIVE", "ELECTRIQUE", "3 A 5L", "6 A 10L", "11 A 15L", "20 A 25L", "BENNE"]
    listeCombo3 = Combobox(label, height=200, width=27, values=listeModel)
    listeCombo3.current(0)
    listeCombo3.place(relx=0.3, rely=0.2, relheight=0.05, relwidth=0.4)
    listeCombo3.bind("<<ComboboxSelected>>", selecModel)

    listeGamme = ["Gamme a selectionner", "MONOSPACE", "SUV", "BERLIN", "SPORTIVE", "ELECTRIQUE", "3 A 5L", "6 A 10L", "11 A 15L", "20 A 25L", "BENNE"]
    listeCombo4 = Combobox(label, height=200, width=27, values=listeGamme)
    listeCombo4.current(0)
    listeCombo4.place(relx=0.3, rely=0.25, relheight=0.05, relwidth=0.4)
    listeCombo4.bind("<<ComboboxSelected>>", selecGamme)

    listeCarbu = ["Carburant a selectionner", "ELECTRIQUE", "DIESEL", "ESSENCE"]
    listeCombo5 = Combobox(label, height=200, width=27, values=listeCarbu)
    listeCombo5.current(0)
    listeCombo5.place(relx=0.3, rely=0.3, relheight=0.05, relwidth=0.4)
    listeCombo5.bind("<<ComboboxSelected>>", selecCarbu)

    UserInfo = tk.Text(label)
    UserInfo.insert(tk.END,presetUser.format("", "", "", "", "", "", "", "", "", "", ""))
    UserInfo.place(relx=0.3, rely=0.15, relheight=0.6, relwidth=0.4)
