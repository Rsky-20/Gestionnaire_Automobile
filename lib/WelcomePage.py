import tkinter as tk
from tkinter import *
from PIL import Image

msgBoxAbout = """{}

- createur: Jessy J. | Enora G. | Luc V. | Pierre V.
- date: Sun Jun 6 15:59:57 2021 +0200
- version : GUI_v5.9 / DataTool_v1.8
- github: 
- commit: 3e81f68f871d3d5d766dff0201dc578888f25e37 (HEAD -> main, origin/main, origin/HEAD)
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
    app.title("A propos")
