import tkinter as tk
from tkinter import *
from PIL import Image

msgBoxAbout = """{}

- createur: Jessy J. | Enora G. | Luc V. | Pierre V.
- date: Mon Jun 7 23:05:34 2021 +0200
- version : GUI_v5.9 / DataTool_v1.8
- github: 
- commit: 7b1746a40993ad879872854a6af2331ec1a0ee6a (HEAD -> main, origin/main, origin/HEAD)
- language de programmation: python 3.8
- liscence: MIT
""".format("Gestionnaire Automobile - Lock'Auto")

def welcome_page(master):
    """
    [Description]
    Fonction permettant de générer la page "à propos".

    :param master: master se réfaire à la page parent
    :return:
    """

    app = tk.Toplevel(master)
    h = app.winfo_screenheight()
    w = app.winfo_screenwidth()
    screen = str(round(w*0.748)) +"x" + str(round(h*0.91)) + "+" + str(round(w*0.246)) + "+" + str(round(h*0.052))
    app.geometry(screen)
    app.attributes("-toolwindow", 1)# Supprime les boutons Réduire/Agrandir
    app.transient(master)
    app.resizable(False, False)
    app.title("Bienvenue")
    
    message_bienvenue = """
        Nous, Luc Vierne, Jessy José, Pierre Vaudry et Enora Guillaume, sommes heureux de vous présenter notre logiciel. 
        Ce dernier a été créé durant un projet d’étude. 

        Pierre Vaudry et Enora Guillaume ont conçu le visuel et la partie graphique de l’application tandis que 
        Luc Vierne et Jessy José se sont occupés de la partie gestions des fichiers.
        Notre logiciel a pour objectif de faciliter la gestion d’un parc automobile. 
        Il permet également de gérer un fichier client ainsi que gérer la location des voitures de ce parc.

        Nous avions pour objectif de créer un logiciel intuitif, 
        utilisable par tous et qui ne nécessite pas forcément de formation pour l’utiliser. 
        En effet chaque fonction est clairement indiquée et ne nécessite pas d’explication préalable."""
    
    text = tk.Text(app)
    text.configure(font=("Tahoma", 16))
    text.insert(tk.END, message_bienvenue)
    text.configure(state='disabled')
    text.place(relx=0, rely=0, relheight=1, relwidth=1)
