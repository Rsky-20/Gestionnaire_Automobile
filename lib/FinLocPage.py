import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import messagebox
import lib.DataTool as DT

def valide(annulationInfo, app):
    msgboxText = """
           Réservation à supprimer : {}
           """.format(annulationInfo)
    resp = messagebox.askokcancel(title="Voulez-vous annuler cette réservation ?", message=msgboxText)

    if resp == True:
        DT.annuler_location(DT.dfc, DT.dfv, id)
        app.destroy()
    else:
        app.destroy()
        
def fin_loc_page(master):
    """
    [Description]

    :param master: master se réfaire à la page parent
    :return:
    """
    
    
    app = tk.Toplevel(master)
    app.geometry('1148x786+378+45')
    app.attributes("-toolwindow", 1)  # Supprime les boutons Réduire/Agrandir
    app.transient(master)
    app.resizable(False, False)
    app.title("Terminer Location")