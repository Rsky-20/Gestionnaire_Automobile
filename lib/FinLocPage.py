import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import messagebox
import lib.DataTool as DT

def valide(id_vehicule, km, app):
    msgboxText = """
           Status de location : terminé ! 
           """
    resp = messagebox.askokcancel(title="Voulez-vous valider cette oppération ?",
                                  message=msgboxText)

    if resp == True:
        DT.terminer_location(DT.dfc, DT.dfv, id_vehicule, km)
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
    
    varId = tk.IntVar()
    tk.LabelFrame(app, text="Id du véhicule").place(
        relx=0.4, rely=0.245, relheight=0.09, relwidth=0.2)
    tk.Entry(app, width=14, textvariable=varId).place(
        relx=0.41, rely=0.27, relheight=0.05, relwidth=0.18)
    
    varKm = tk.IntVar()
    tk.LabelFrame(app, text="Nombre de kilomètre parcourue").place(
        relx=0.4, rely=0.345, relheight=0.09, relwidth=0.2)
    tk.Entry(app, width=14, textvariable=varKm).place(
        relx=0.41, rely=0.37, relheight=0.05, relwidth=0.18)
    
    btnValide = tk.Button(app, text='Valider', command=lambda: valide(varId.get(),varKm.get(), app))
    btnValide.place(relx=0.3, rely=0.55, relheight=0.05, relwidth=0.4)