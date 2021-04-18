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

    Many other constants and variable may be defined; these may be used in calls

"""

# ---------------------------------------------Import module section-------------------------------------------------- #

import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox
from PIL import Image
import lib.AboutPage as AbP
import lib.AjoutVehiPage as AVP
import lib.AnnulPage as AnP
import lib.ReservPage as RP
import lib.SupUserPage as SUP
import lib.SupVehiPage as SVP
import lib.UserPage as UP


# -----------------------------------------------Class and process-----------------------------------------------------#

class MainApp:
    """
    [description]
    MainApp est la class permettant de générer, charger et instancier la base du programme de gestion. Cette class
    contient la base graphique.
    """

    def __init__(self):
        super().__init__()
        self.root = tk.Tk()
        self.w, self.h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.title("Gestionnaire Automobile")
        self.root.geometry('1920x1080')
        self.root.bind("<Escape>", lambda e: (e.widget.withdraw(), e.widget.quit()))

        # self.iconbitmap('./images/téléchargement (9).ico')
        self.Widgets()

        self.photo = PhotoImage(file='./images/Service_img.gif')
        espace_image = Canvas(self.root, bg='blue')
        espace_image.place(rely=0.0, relx=0.25, relwidth=0.75, relheight=1, )
        espace_image.create_image(600, 550, image=self.photo) #600, 550,

        self.root.mainloop()

    def Widgets(self):
        """
        [description]
        Function contenant tout les élément de la page principale du programme. Cette fonction rassemble tout les
        boutons et object d'interraction.

        :return:
        """

        menubar = Menu(self.root)

        menu1 = Menu(menubar, tearoff=0)
        menu1.add_command(label="Creer", command=0)
        menu1.add_command(label="Editer", command=0)
        menu1.add_command(label="Importer base de donnée", command=0)
        menu1.add_command(label="Exporter base de donnée", command=0)
        menu1.add_separator()
        menu1.add_command(label="Quitter", command=self.root.quit)
        menubar.add_cascade(label="Fichier", menu=menu1)

        menu2 = Menu(menubar, tearoff=0)
        menu2.add_command(label="Couper", command=0)
        menu2.add_command(label="Copier", command=0)
        menu2.add_command(label="Coller", command=0)
        menubar.add_cascade(label="Editer", menu=menu2)

        menu3 = Menu(menubar, tearoff=0)
        menu3.add_command(label="A propos", command=lambda: AbP.About_Page(self.root))
        menubar.add_cascade(label="Aide", menu=menu3)

        self.root.config(menu=menubar)

        self.banner = tk.Frame(self.root, bg="#CFC7C5")
        self.banner.place(relwidth=0.25, relheight=1)

        self.user = tk.Button(self.banner, text='USER',
                              command=lambda: UP.User_Page(self.root)).place(relx=0.3,
                                                                              rely=0.2, relheight=0.05, relwidth=0.4)
        self.reservation = tk.Button(self.banner, text='RESERVATION',
                                     command=lambda: RP.Reserv_Page(self.root)).place(relx=0.3, rely=0.3,
                                                                                       relheight=0.05, relwidth=0.4)
        self.annulation = tk.Button(self.banner, text='ANNULATION',
                                    command=lambda: AnP.Annul_Page(self.root)).place(
            relx=0.3, rely=0.4, relheight=0.05,
            relwidth=0.4)
        self.admin = tk.Button(self.banner, text='ADMIN',
                               command=self.admin).place(relx=0.3, rely=0.55, relheight=0.05, relwidth=0.4)

        self.listeAdmin = ["", "Ajout Véhicule", "Suppression Véhicule", "Suppréssion Utilisateur"]
        self.listeCombo1 = Combobox(self.banner, height=200, width=27, values=self.listeAdmin)
        self.listeCombo1.current(0)
        self.listeCombo1.place(relx=0.3, rely=0.6, relheight=0.05, relwidth=0.4)
        self.listeCombo1.bind("<<ComboboxSelected>>", self.admin)



    def admin(self):
        """
        [description]
        Fonction permettant de choisir la page à ouvrir parmi un menu déroulant

        :return:
        """

        # Obtenir l'élément sélectionné
        self.select = self.listeCombo1.get()
        print("Vous avez sélectionné : '", self.select, "'")

        if self.select == "Ajout Véhicule":
            AVP.AjoutVehi_Page(self.root)
        elif self.select == "Suppression Véhicule":
            SVP.SupVehi_Page(self.root)
        elif self.select == "Suppréssion Utilisateur":
            SUP.SupUser_Page(self.root)


# -------------------------------------------Run & Start server program----------------------------------------------- #


if __name__ == '__main__':
    print(__doc__)

    # Run the program
    app = MainApp()
