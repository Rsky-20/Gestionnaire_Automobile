import tkinter as tk
from tkinter.filedialog import *  # pour les gestions de fichiers
from PIL import Image as Img
from PIL import ImageTk
import lib.DataTool as DT


def Export_Page(master):
    """
    [Description]
    Fonction permettant de générer la page Export data.

    :param master: master se réfaire à la page parent
    :return:
    """

    app = tk.Toplevel(master)
    app.geometry('920x640')
    app.w, app.h = app.winfo_screenwidth(), app.winfo_screenheight()
    app.title("Export DataBase")

    File = StringVar()
    File.set("Pas de fichier pour l'instant")

    # Création d'un Label nommé monAffichage
    screen = Label(app, textvariable=File, width=70)
    screen.pack()

    # Recherche de l'adresse du fichier-image voulu
    filename = askopenfilename(title="Importer une BD", filetypes=[('json files', '.json'), ('all files', '.*')])

    # Mise à jour de monFichier
    File.set(filename)
    print(filename)
    type(filename)

    DT.export_bdd(filename, "D:\IPSA\Aero2\Programmation\Grand_Projet\Gestionnaire_Automobile\data")

    app.mainloop()


def Import_Page(master):
    """
    [Description]
    Fonction permettant de générer la page Import data.

    :param master: master se réfaire à la page parent
    :return:
    """

    app = tk.Toplevel(master)
    app.geometry('920x640')
    app.w, app.h = app.winfo_screenwidth(), app.winfo_screenheight()
    app.title("Import DataBase")

    # - - - - - - - - - - - - - - - - - -
    # Création de la fenêtre et des objets associés la fenêtre
    # - - - - - - - - - - - - - - - - - -

    File = StringVar()
    File.set("Pas de fichier pour l'instant")

    # Création d'un Label nommé monAffichage
    screen = Label(app, textvariable=File, width=70)
    screen.pack()

    # Recherche de l'adresse du fichier-image voulu
    filename = askopenfilename(title="Importer une BD", filetypes=[('json files', '.json'), ('all files', '.*')])

    # Mise à jour de monFichier
    File.set(filename)



    app.mainloop()