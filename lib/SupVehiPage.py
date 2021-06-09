import tkinter as tk
from tkinter import messagebox
import lib.DataTool as DT

def valide(id_vehicule, app):
    
    if id_vehicule == "":
        
        msgboxText = """
           Il y a une erreur dans les information renseignées. 
           Merci de bien vouloir les vérifier. 
           """
           
        messagebox.showerror(title="ERROR", message=msgboxText)
        
    else:

        MsgboxText = """
    /!\ Attention cette opération sera définitif /!\ 
    ID du véhicule à supprimer : {}
        """.format(id_vehicule)
        
        resp = messagebox.askokcancel(title="Voulez-vous supprimer ce véhicule ?", message=MsgboxText)

        if resp == True:
            DT.dfv = DT.retirer_vehicule(DT.dfv, int(id_vehicule))
            app.destroy()
        else:
            pass


def sup_vehi_page(master):
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
    app.title("Supression Véhicle")

    varID = tk.StringVar()
    tk.LabelFrame(app, text="Id du Véhicule à supprimer").place(relx=0.05, rely=0.045, relheight=0.09, relwidth=0.2)
    tk.Entry(app, width=14, textvariable=varID).place(relx=0.06, rely=0.07, relheight=0.05, relwidth=0.18)

    btnValide = tk.Button(app, text='Valider',
                          command=lambda: valide(varID.get(), app))
    btnValide.place(relx=0.3, rely=0.55, relheight=0.05, relwidth=0.4)
