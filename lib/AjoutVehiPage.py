import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import messagebox
import lib.DataTool as DT



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
            reservType = presetVehicule.format("a","z","e","r","t","y", id1,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reservType)
            return reservType

        elif selecType == "T":
            reservType = presetVehicule.format("a","z","e","r","t","y", id2,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reservType)
            return reservType

        else:
            reservType = ""
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, presetVehicule.format("", "", "", "", "", "", "", "", "", "", ""))
            return reservType

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
            reservMarque = presetVehicule.format("a","z","e","r","t","y", id1,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reservMarque)
            return reservMarque

        elif selecMarque == "FERRARI":
            reservMarque = presetVehicule.format("a","z","e","r","t","y", id2,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reservMarque)
            return reservMarque

        elif selecMarque == "VOLKSWAGEN":
            reservMarque = presetVehicule.format("a","z","e","r","t","y", id3,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reservMarque)
            return reservMarque

        elif selecMarque == "RENAULT":
            reservMarque = presetVehicule.format("a","z","e","r","t","y", id4,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reservMarque)
            return reservMarque

        elif selecMarque == "MERCEDES":
            reservMarque = presetVehicule.format("a","z","e","r","t","y", id5,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reservMarque)
            return reservMarque

        elif selecMarque == "PORSCHE":
            reservMarque = presetVehicule.format("a","z","e","r","t","y", id6,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reservMarque)
            return reservMarque

        elif selecMarque == "AUDI":
            reservMarque = presetVehicule.format("a","z","e","r","t","y", id7,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reservMarque)
            return reservMarque

        elif selecMarque == "TESLA":
            reservMarque = presetVehicule.format("a","z","e","r","t","y", id8,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reservMarque)
            return reservMarque

        elif selecMarque == "IVECO":
            reservMarque = presetVehicule.format("a","z","e","r","t","y", id9,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reservMarque)
            return reservMarque

        else:
            reservMarque = ""
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, presetVehicule.format("", "", "", "", "", "", "", "", "", "", ""))
            return reservMarque

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
            reservGamme = presetVehicule.format("a","z","e","r","t","y", id1,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reservGamme)
            return reservGamme

        elif selecGamme == "BERLINE":
            reservGamme = presetVehicule.format("a","z","e","r","t","y", id2,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reservGamme)
            return reservGamme

        elif selecGamme == "MONOSPACE":
            reservGamme = presetVehicule.format("a","z","e","r","t","y", id3,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reservGamme)
            return reservGamme

        elif selecGamme == "SPORTIVE":
            reservGamme = presetVehicule.format("a","z","e","r","t","y", id3,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reservGamme)
            return reservGamme

        elif selecGamme == "ELECTRIQUE":
            reservGamme = presetVehicule.format("a","z","e","r","t","y", id3,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reservGamme)
            return reservGamme

        elif selecGamme == "BENNE":
            reservGamme = presetVehicule.format("a","z","e","r","t","y", id3,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reservGamme)
            return reservGamme

        elif selecGamme == "3 A 5":
            reservGamme = presetVehicule.format("a","z","e","r","t","y", id3,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reservGamme)
            return reservGamme

        elif selecGamme == "6 A 10":
            reservGamme = presetVehicule.format("a","z","e","r","t","y", id3,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reservGamme)
            return reservGamme

        elif selecGamme == "11 A 15":
            reservGamme = presetVehicule.format("a","z","e","r","t","y", id3,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reservGamme)
            return reservGamme

        elif selecGamme == "20 A 25":
            reservGamme = presetVehicule.format("a","z","e","r","t","y", id3,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reservGamme)
            return reservGamme

        else:
            reservGamme = ""
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, presetVehicule.format("", "", "", "", "", "", "", "", "", "", ""))
            return reservGamme

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
            reserv = presetVehicule.format("a","z","e","r","t","y", id1,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reserv)
            return reserv

        elif select == "FERRARI":
            reservModel = presetVehicule.format("a","z","e","r","t","y", id2,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reservModel)
            return reservModel

        elif select == "VOLKSWAGEN":
            reservModel = presetVehicule.format("a","z","e","r","t","y", id3,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reservModel)
            return reservModel

        elif select == "RENAULT":
            reservModel = presetVehicule.format("a","z","e","r","t","y", id3,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reservModel)
            return reservModel

        elif select == "MERCEDES":
            reservModel = presetVehicule.format("a","z","e","r","t","y", id3,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reservModel)
            return reservModel

        elif select == "PORSCHE":
            reservModel = presetVehicule.format("a","z","e","r","t","y", id3,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reservModel)
            return reservModel

        elif select == "AUDI":
            reservModel = presetVehicule.format("a","z","e","r","t","y", id3,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reservModel)
            return reservModel

        elif select == "TESLA":
            reservModel = presetVehicule.format("a","z","e","r","t","y", id3,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reservModel)
            return reservModel

        elif select == "IVECO":
            reservModel = presetVehicule.format("a","z","e","r","t","y", id3,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reservModel)
            return reservModel

        else:
            reservModel = ""
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, presetVehicule.format("", "", "", "", "", "", "", "", "", "", ""))
            return reservModel



    app = tk.Toplevel(master)
    app.geometry('920x640+500+125')
    app.attributes("-toolwindow", 1)# Supprime les boutons Réduire/Agrandir
    app.transient(master)
    app.resizable(False, False)
    app.title("Ajout Véhicle")

    label = tk.LabelFrame(app, text="Sélectionnez l'utilisateur dont vous voulez reserver la réservation")
    label.place(relheight=1, relwidth=1)

    BtnValide = tk.Button(label, text='Valider', command=lambda: valide(reserv, app))
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

    vehiculeInfo = tk.Text(label)
    vehiculeInfo.insert(tk.END,presetVehicule.format("", "", "", "", "", "", "", "", "", "", ""))
    vehiculeInfo.place(relx=0.3, rely=0.15, relheight=0.6, relwidth=0.4)
