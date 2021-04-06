#!/bin/python3 -*- coding: utf-8 -*-
"""
@Author : Jessy JOSE -- Pierre VAUDRY -- Enora GUILLAUME -- Luc VIERNE
IPSA Aero2 - Prim1
Release date: 07/04/2021


[other information]
Licence: MIT


[Description]

    Ce package rajoute toute les fonctionnalités nécessaire au programme de gestion d'un parc automonile


[Functions]:
    About_Page() --
    User_Page() --
    Reserv_Page() --
    Annul_Page() --
    AjoutVehi_Page() --
    SupVehi_Page() --
    SupUser_Page() --


[Other variable]:

    Many other constants and variable may be defined; these may be used in calls

"""

# ---------------------------------------------Import module section-------------------------------------------------- #

import tkinter as tk


def About_Page(master):
    """
    [Description]
    Fonction permettant de générer la page "à propos".

    :param master: master se réfaire à la page parent
    :return:
    """

    app = tk.Toplevel(master)
    app.geometry('920x640')
    app.w, app.h = app.winfo_screenwidth(), app.winfo_screenheight()
    app.title("A propos")


def User_Page(master):
    """
    [Description]


    :param master: master se réfaire à la page parent
    :return:
    """

    app = tk.Toplevel(master)
    app.geometry('920x640')
    app.w, app.h = app.winfo_screenwidth(), app.winfo_screenheight()
    app.title("Page User")

    app.Nom = tk.LabelFrame(app, text="Nom")
    app.Nom.place(relx=0.05, rely=0.045, relheight=0.09, relwidth=0.2)
    varNom = tk.StringVar()
    tk.Entry(app, width=14, textvariable=varNom).place(relx=0.06, rely=0.07, relheight=0.05, relwidth=0.18)

    app.Prenom = tk.LabelFrame(app, text="Prénom")
    app.Prenom.place(relx=0.05, rely=0.145, relheight=0.09, relwidth=0.2)
    varPrenom = tk.StringVar()
    tk.Entry(app, width=14, textvariable=varPrenom).place(relx=0.06, rely=0.17, relheight=0.05, relwidth=0.18)

    app.Age = tk.LabelFrame(app, text="Age")
    app.Age.place(relx=0.05, rely=0.245, relheight=0.09, relwidth=0.2)
    varAge = tk.StringVar()
    tk.Entry(app, width=14, textvariable=varAge).place(relx=0.06, rely=0.27, relheight=0.05, relwidth=0.18)

    app.NumPerm = tk.LabelFrame(app, text="Numero de permis")
    app.NumPerm.place(relx=0.05, rely=0.345, relheight=0.09, relwidth=0.2)
    varNumPerm = tk.StringVar()
    tk.Entry(app, width=14, textvariable=varNumPerm).place(relx=0.06, rely=0.37, relheight=0.05, relwidth=0.18)

    app.AdressMail = tk.LabelFrame(app, text="Adresse Mail")
    app.AdressMail.place(relx=0.05, rely=0.445, relheight=0.09, relwidth=0.2)
    varAdressMail = tk.StringVar()
    tk.Entry(app, width=14, textvariable=varAdressMail).place(relx=0.06, rely=0.47, relheight=0.05, relwidth=0.18)

    app.Tel = tk.LabelFrame(app, text="Télephone")
    app.Tel.place(relx=0.05, rely=0.545, relheight=0.09, relwidth=0.2)
    varTel = tk.StringVar()
    tk.Entry(app, width=14, textvariable=varTel).place(relx=0.06, rely=0.57, relheight=0.05, relwidth=0.18)


def Reserv_Page(master):
    """
    [Description]

    :param master: master se réfaire à la page parent
    :return:
    """

    app = tk.Toplevel(master)
    app.geometry('920x640')
    app.w, app.h = app.winfo_screenwidth(), app.winfo_screenheight()
    app.title("Réservation")


def Annul_Page(master):
    """
    [Description]

    :param master: master se réfaire à la page parent
    :return:
    """

    app = tk.Toplevel(master)
    app.geometry('920x640')
    app.w, app.h = app.winfo_screenwidth(), app.winfo_screenheight()
    app.title("Annulation")


def AjoutVehi_Page(master):
    """
    [Description]

    :param master: master se réfaire à la page parent
    :return:
    """

    app = tk.Toplevel(master)
    app.geometry('920x640')
    app.w, app.h = app.winfo_screenwidth(), app.winfo_screenheight()
    app.title("Ajout Véhicle")


def SupVehi_Page(master):
    """
    [Description]

    :param master: master se réfaire à la page parent
    :return:
    """

    app = tk.Toplevel(master)
    app.geometry('920x640')
    app.w, app.h = app.winfo_screenwidth(), app.winfo_screenheight()
    app.title("Suupression Véhicle")


def SupUser_Page(master):
    """
    [Description]

    :param master: master se réfaire à la page parent
    :return:
    """

    app = tk.Toplevel(master)
    app.geometry('920x640')
    app.w, app.h = app.winfo_screenwidth(), app.winfo_screenheight()
    app.title("Suupression Utilisateur")
