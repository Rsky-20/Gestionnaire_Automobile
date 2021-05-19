#!/bin/python3 -*- coding: utf-8 -*-
"""
@Author : Jessy JOSE -- Pierre VAUDRY -- Enora GUILLAUME -- Luc VIERNE
IPSA Aero2 - Prim1
Release date: 07/04/2021


[other information]
Licence: MIT


[Description]

    Ce projet a pour but de permettre la gestion d'un parc automonile


[Class]

    MainApp() -- main class to make first page and instance all functions


[Other variable]:

    Many other constants and variable may be defined;
    these may be used in calls

"""

# --------- Import module section --------- #

import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from PIL import Image, ImageTk
import lib.DataTool as DT
import lib.AboutPage as AbP
import lib.AjoutVehiPage as AVP
import lib.AnnulPage as AnP
import lib.ReservPage as RP
import lib.SupUserPage as SUP
import lib.SupVehiPage as SVP
import lib.UserPage as UP
import lib.ExpImp_Data as EIData
import lib.grille_tarifaire as gt

# --------- Class and process --------- #

class ToolBar:
    """

    """

    def __init__(self, master):
        self.root = master
        self.top_menu()

    def top_menu(self):
        menubar = Menu(self.root)

        menu1 = Menu(menubar, tearoff=0)
        menu1.add_command(
            label="Modifier BDD Grille tarifaire [Not_Finished]", command=0)
        menu1.add_command(
            label="Modifier BDD véhicule [Not_Finished]", command=0)
        menu1.add_command(
            label="Modifier BDD client [Not_Finished]", command=0)
        menu1.add_separator()
        menu1.add_command(
            label="Importer base de donnée [Not_Finished]", command=0)
        menu1.add_command(
            label="Exporter base de donnée [Not_Finished]",
            command=lambda: EIData.export_page(self.root))
        menu1.add_separator()
        menu1.add_command(label="Quitter", command=self.quit_app)
        menubar.add_cascade(label="Fichier", menu=menu1)

        menu2 = Menu(menubar, tearoff=0)
        menu2.add_command(label="Grille Tariffaires",
                          command=lambda: gt.run(self.root))
        menu2.add_command(label="Véhicules", command=lambda: self.vehicules)
        menu2.add_command(label="clients", command=lambda: self.clients)
        menubar.add_cascade(label="Informations", menu=menu2)

        menu3 = Menu(menubar, tearoff=0)
        menu3.add_command(label="A propos",
                          command=lambda: AbP.about_page(self.root))
        menu3.add_command(label="? Aide ?",
                          command=lambda: 0)
        menubar.add_cascade(label="Aide", menu=menu3)

        self.root.config(menu=menubar)

    def quit_app(self):
        """
        [description]

        :return:
        """
        MessageBox = """
        Voulez-vous quittez l'application ?
        """
        resp = messagebox.askokcancel(
            title="Quitter Lock'Auto", message=MessageBox)
        if resp:
            DT.enregistrer_json(DT.dfc, "./data/clients.json")
            DT.enregistrer_json(DT.dft, "./data/tarifs.json")
            DT.enregistrer_json(DT.dfv, "./data/vehicules.json")
            self.root.destroy()
        else:
            pass

    def grille_tarrifaires(self):
        MsgboxText = """
        {}
        """.format(DT.aff_tarifs())
        print(MsgboxText)
        messagebox.showinfo(title="Grille Tarrifaires", message=MsgboxText)

    def vehicules(self):
        MsgboxText = """
        {}
        """.format(0)
        print(MsgboxText)
        messagebox.showinfo(title="vehicules", message=MsgboxText)

    def clients(self):
        MsgboxText = """
        {}
        """.format(0)
        print(MsgboxText)
        messagebox.showinfo(title="clients", message=MsgboxText)


class MainApp:
    """
    [description]
    MainApp est la class permettant de générer,
    charger et instancier la base du programme de gestion.
    Cette class contient la base graphique.
    """

    def __init__(self):
        # super().__init__()
        self.root = tk.Tk()
        self.root.wm_attributes('-transparentcolor', 'red')
        self.w = self.root.winfo_screenwidth(),
        self.h = self.root.winfo_screenheight()
        self.root.title("Gestionnaire Automobile - Lock'Auto")
        self.root.geometry('1920x1080')
        self.root.resizable(True, True)

        # Menu : Fichier
        ToolBar(self.root)

        # Background image
        self.image = PhotoImage(file='./images/ABF8686-bewerkt.gif')
        self.canvas = Canvas(self.root, width=self.w, height=self.h)
        self.canvas.place(rely=0.0, relx=0.0, relwidth=1, relheight=1)
        self.canvas.create_image(0, 0, image=self.image, anchor=NW, )

        # self.iconbitmap('./images/téléchargement (9).ico')
        self.widgets()

        self.root.mainloop()

    def widgets(self):
        """
        [description]
        Function contenant tout les élément de la page principale du programme.
        Cette fonction rassemble tout les boutons et object d'interraction.

        :return:
        """

        self.banner = tk.Frame(self.root, bg="#0d0d0d")
        self.banner.place(relx=0.001, rely=0.01,
                          relwidth=0.25, relheight=0.988)

        tk.Button(self.banner, text='USER',
            command=lambda: UP.user_page(self.root),
                bg="lightgrey").place(relx=0.3,
                    rely=0.2, relheight=0.05, relwidth=0.4)
        tk.Button(self.banner, text='RESERVATION',
                  command=lambda: RP.reserv_page(self.root),
                  bg="lightgrey").place(relx=0.3, rely=0.3,
                  relheight=0.05, relwidth=0.4)
        tk.Button(self.banner, text='ANNULATION',
                                    command=lambda: AnP.annul_page(self.root), 
                                    bg="lightgrey").place(
                                        relx=0.3, rely=0.4, relheight=0.05,
                                        relwidth=0.4)
        self.admin = tk.Button(self.banner, text='ADMIN',
        command=self.admin, bg="lightgrey").place(relx=0.3, rely=0.55,
        relheight=0.05, relwidth=0.4)

        self.listeAdmin = ["Selectionner une action", "Ajout Véhicule",
        "Suppression Véhicule",
                           "Suppréssion Utilisateur"]
        self.listeCombo1 = Combobox(
            self.banner, height=200, width=27, values=self.listeAdmin)
        self.listeCombo1.current(0)
        self.listeCombo1.place(
            relx=0.3, rely=0.6, relheight=0.05, relwidth=0.4)
        self.listeCombo1.bind("<<ComboboxSelected>>", self.admin)

    def admin(self):  # pylint: disable=E0202
        """
        [description]
        Fonction permettant de choisir la page à ouvrir parmi un menu déroulant

        :return:
        """

        # Obtenir l'élément sélectionné
        self.select = self.listeCombo1.get()
        print("Vous avez sélectionné : '", self.select, "'")

        if self.select == "Ajout Véhicule":
            AVP.ajout_vehi_page(self.root)
        elif self.select == "Suppression Véhicule":
            SVP.sup_vehi_page(self.root)
        elif self.select == "Suppréssion Utilisateur":
            SUP.sup_user_page(self.root)

# ------ Run & Start server program ------ #


if __name__ == '__main__':
    print(__doc__)

    # Run the program
    app = MainApp()
