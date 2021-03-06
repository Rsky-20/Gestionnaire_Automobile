import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import messagebox
import lib.DataTool as DT

def valide(id_vehicule, km, app):
    
    #test = DT.km_ok(DT.dfv,id_vehicule,km)
    #print(test)
    print(type(id_vehicule))
    print(type(km))
    
    if id_vehicule and km != 0:
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
    else:
        msgboxText = """
           Il y a une erreur dans les information renseignées. 
           Merci de bien vouloir les vérifier. 
           """
        messagebox.showerror(title="ERROR", message=msgboxText)


        
def fin_loc_page(master):
    """
    [Description]

    :param master: master se réfaire à la page parent
    :return:
    """
    
    
    app = tk.Toplevel(master)
    h = app.winfo_screenheight()
    w = app.winfo_screenwidth()
    screen = str(round(w*0.748)) +"x" + str(round(h*0.91)) + "+" + str(round(w*0.246)) + "+" + str(round(h*0.052))
    app.geometry(screen)
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
    tk.LabelFrame(app, text="Nombre de kilomètre parcourus").place(
        relx=0.4, rely=0.345, relheight=0.09, relwidth=0.2)
    tk.Entry(app, width=14, textvariable=varKm).place(
        relx=0.41, rely=0.37, relheight=0.05, relwidth=0.18)
    
    btnValide = tk.Button(app, text='Valider', command=lambda: valide(varId.get(),varKm.get(), app))
    btnValide.place(relx=0.3, rely=0.55, relheight=0.05, relwidth=0.4)