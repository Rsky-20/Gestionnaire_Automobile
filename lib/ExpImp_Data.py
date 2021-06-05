#from os import path
import tkinter as tk
from tkinter.filedialog import *  # pour les gestions de fichiers
from PIL import Image as Img
from PIL import ImageTk
import lib.DataTool as DT
from tkinter import messagebox


def export_page(fileToExport):
    """
    [Description]
    Fonction permettant de générer la page Export data.

    :param master: master se réfaire à la page parent
    :return:
    """
    
    if fileToExport == "vehicule":
        DT.export_bdd(DT.dfv, "./data/CSV_export_vehicule.csv")
        MsgboxText = """
/!\ La base de donnée {} a été exporté avec succès /!\ 
    path:../Gestionnaire_Automonile/data/CSV_export_vehicule.csv
    """.format(fileToExport)
        messagebox.showwarning(title="Export base de donnée", message=MsgboxText)
            
    elif fileToExport == "client":
        DT.export_bdd(DT.dfc, "./data/CSV_export_client.csv")
        MsgboxText = """
/!\ La base de donnée {} a été exporté avec succès /!\ 
    path:../Gestionnaire_Automonile/data/CSV_export_client.csv 
    """.format(fileToExport)
        messagebox.showwarning(title="Export base de donnée", message=MsgboxText)
            
    elif fileToExport == "tarif":
        DT.export_bdd(DT.dft, "./data/CSV_export_tarif.csv")
        MsgboxText = """
/!\ La base de donnée {} a été exporté avec succès /!\ 
    path:../Gestionnaire_Automonile/data/CSV_export_tarif.csv
    """.format(fileToExport)
        messagebox.showwarning(title="Export base de donnée", message=MsgboxText)

    else:
        pass
    

def import_page(master):
    """
    [Description]
    Fonction permettant de générer la page Import data.

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
    app.title("Import DataBase")

    # - - - - - - - - - - - - - - - - - -
    # Création de la fenêtre et des objets associés la fenêtre
    # - - - - - - - - - - - - - - - - - -

    file = tk.StringVar()
    file.set("Pas de fichier pour l'instant")

    # Création d'un Label nommé monAffichage
    screen = tk.Label(app, textvariable=file, width=70)
    screen.pack()

    # Recherche de l'adresse du fichier-image voulu
    filename = askopenfilename(title="Importer une Base de Donnée", filetypes=[('csv files', '.csv'), ('all files', '.*')])

    # Mise à jour de monFichier
    file.set(filename)



    app.mainloop()