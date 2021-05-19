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
            reserv = presetVehicule.format("a","z","e","r","t","y", id1,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reserv)
            return reserv

        elif selecType == "T":
            reserv = presetVehicule.format("a","z","e","r","t","y", id2,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reserv)
            return reserv

        else:
            reserv = ""
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, presetVehicule.format("", "", "", "", "", "", "", "", "", "", ""))
            return reserv

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
            reserv = presetVehicule.format("a","z","e","r","t","y", id1,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reserv)
            return reserv

        elif selecMarque == "FERRARI":
            reserv = presetVehicule.format("a","z","e","r","t","y", id2,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reserv)
            return reserv

        elif selecMarque == "VOLKSWAGEN":
            reserv = presetVehicule.format("a","z","e","r","t","y", id3,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reserv)
            return reserv

        elif selecMarque == "RENAULT":
            reserv = presetVehicule.format("a","z","e","r","t","y", id4,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reserv)
            return reserv

        elif selecMarque == "MERCEDES":
            reserv = presetVehicule.format("a","z","e","r","t","y", id5,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reserv)
            return reserv

        elif selecMarque == "PORSCHE":
            reserv = presetVehicule.format("a","z","e","r","t","y", id6,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reserv)
            return reserv

        elif selecMarque == "AUDI":
            reserv = presetVehicule.format("a","z","e","r","t","y", id7,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reserv)
            return reserv

        elif selecMarque == "TESLA":
            reserv = presetVehicule.format("a","z","e","r","t","y", id8,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reserv)
            return reserv

        elif selecMarque == "IVECO":
            reserv = presetVehicule.format("a","z","e","r","t","y", id9,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reserv)
            return reserv

        else:
            reserv = ""
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, presetVehicule.format("", "", "", "", "", "", "", "", "", "", ""))
            return reserv

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
            reserv = presetVehicule.format("a","z","e","r","t","y", id1,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reserv)
            return reserv

        elif selecGamme == "BERLINE":
            reserv = presetVehicule.format("a","z","e","r","t","y", id2,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reserv)
            return reserv

        elif selecGamme == "MONOSPACE":
            reserv = presetVehicule.format("a","z","e","r","t","y", id3,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reserv)
            return reserv

        elif selecGamme == "SPORTIVE":
            reserv = presetVehicule.format("a","z","e","r","t","y", id3,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reserv)
            return reserv

        elif selecGamme == "ELECTRIQUE":
            reserv = presetVehicule.format("a","z","e","r","t","y", id3,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reserv)
            return reserv

        elif selecGamme == "BENNE":
            reserv = presetVehicule.format("a","z","e","r","t","y", id3,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reserv)
            return reserv

        elif selecGamme == "3 A 5":
            reserv = presetVehicule.format("a","z","e","r","t","y", id3,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reserv)
            return reserv

        elif selecGamme == "6 A 10":
            reserv = presetVehicule.format("a","z","e","r","t","y", id3,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reserv)
            return reserv

        elif selecGamme == "11 A 15":
            reserv = presetVehicule.format("a","z","e","r","t","y", id3,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reserv)
            return reserv

        elif selecGamme == "20 A 25":
            reserv = presetVehicule.format("a","z","e","r","t","y", id3,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reserv)
            return reserv

        else:
            reserv = ""
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, presetVehicule.format("", "", "", "", "", "", "", "", "", "", ""))
            return reserv

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
            reserv = presetVehicule.format("a","z","e","r","t","y", id2,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reserv)
            return reserv

        elif select == "VOLKSWAGEN":
            reserv = presetVehicule.format("a","z","e","r","t","y", id3,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reserv)
            return reserv

        elif select == "RENAULT":
            reserv = presetVehicule.format("a","z","e","r","t","y", id3,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reserv)
            return reserv

        elif select == "MERCEDES":
            reserv = presetVehicule.format("a","z","e","r","t","y", id3,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reserv)
            return reserv

        elif select == "PORSCHE":
            reserv = presetVehicule.format("a","z","e","r","t","y", id3,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reserv)
            return reserv

        elif select == "AUDI":
            reserv = presetVehicule.format("a","z","e","r","t","y", id3,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reserv)
            return reserv

        elif select == "TESLA":
            reserv = presetVehicule.format("a","z","e","r","t","y", id3,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reserv)
            return reserv

        elif select == "IVECO":
            reserv = presetVehicule.format("a","z","e","r","t","y", id3,"u","i","o","p")
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, reserv)
            return reserv

        else:
            reserv = ""
            vehiculeInfo.delete("1.0", "end")
            vehiculeInfo.insert(tk.END, presetVehicule.format("", "", "", "", "", "", "", "", "", "", ""))
            return reserv
        
    def selecCarbu():
        pass



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
