import tkinter as tk
from tkinter import messagebox
import lib.DataTool as DT


def valide(gamme, t, prix, assur, caut, app):
    """[summary]

    Args:
        gamme ([type]): [description]
        t ([type]): [description]
        prix ([type]): [description]
        assur ([type]): [description]
        caut ([type]): [description]
        app ([type]): [description]
    """    
    
    if gamme == "" or t == "" or prix == "" and assur == 0 or caut == 0:
        msgboxText = """
           Il y a une erreur dans les information renseignées. 
           Merci de bien vouloir les vérifier. 
           """
        messagebox.showerror(title="ERROR", message=msgboxText)
        
        
    else:
        
        msgboxText = """
- Gamme : {}
- Type : {}
- Prix : {}
- Assurance : {}
- Caution : {}
        """.format(gamme, t, prix, assur, caut)
        
        resp = messagebox.askokcancel(
            title="Voulez-vous changer le tarif ?", message=msgboxText)

        if resp:
            DT.ajouter_client(DT.dft, gamme, t, prix, assur, caut)
            app.destroy()
        else:
            #app.destroy()
            pass


def modif_tarif_page(master):
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
    app.title("Modification Tarif")
