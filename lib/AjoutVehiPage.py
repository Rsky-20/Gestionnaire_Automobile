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
