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
import lib.FinLocPage as FP
import lib.ReservPage as RP
import lib.SupClientPage as SCP
import lib.SupVehiPage as SVP
import lib.ClientPage as CP
import lib.ExpImp_Data as EIData
import lib.grille_tarifaire as gt
import lib.grille_client as gc
import lib.grille_vehicule as gv
import lib.grille_reservation as gr

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
        menu1.add_command(label="Quitter et Sauvegarder", command=self.quit_app)
        menubar.add_cascade(label="Fichier", menu=menu1)

        menu2 = Menu(menubar, tearoff=0)
        menu2.add_command(label="Grille Tariffaires",
                          command=lambda: gt.run(self.root))
        menu2.add_command(label="Grille Véhicules", command=lambda: gv.run(self.root))
        menu2.add_command(label="Grille Clients", command=lambda: gc.run(self.root))
        menu2.add_command(label="Réservation actuelle", command=lambda: gr.run(self.root))
        
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
        
        self.root.wm_state(newstate="zoomed")

        
        #self.root.attributes('-fullscreen', 0)


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

        tk.Button(self.banner, text='CLIENT',
            command=lambda: CP.client_page(self.root),
                bg="lightgrey").place(relx=0.3,
                    rely=0.2, relheight=0.05, relwidth=0.4)
        tk.Button(self.banner, text='RESERVATION',
                  command=lambda: RP.reserv_page(self.root),
                  bg="lightgrey").place(relx=0.3, rely=0.3,
                  relheight=0.05, relwidth=0.4)
        tk.Button(self.banner, text='TERMINER Location',
                                    command=lambda: FP.fin_loc_page(self.root), 
                                    bg="lightgrey").place(
                                        relx=0.3, rely=0.4, relheight=0.05,
                                        relwidth=0.4)
                                    
        self.admin = tk.Button(self.banner, text='ADMIN',
        command=self.admin, bg="lightgrey").place(relx=0.3, rely=0.55,
        relheight=0.05, relwidth=0.4)

        self.listeAdmin = ["Selectionner une action", "Ajout Véhicule",
        "Suppression Véhicule", "Suppression Client",
        "Annulation d'une location"]
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
        elif self.select == "Suppression Client":
            SCP.sup_client_page(self.root)
        elif self.select == "Annulation d'une location":
            AnP.annul_page(self.root)

# ------ Run & Start server program ------ #


if __name__ == '__main__':
    print(__doc__)

    # Run the program
    app = MainApp()
