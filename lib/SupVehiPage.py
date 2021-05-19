import tkinter as tk
from tkinter import messagebox
import lib.DataTool as DT

def valide(idVehicule, app):

    MsgboxText = """
       ID du véhicule à supprimer : {}
       """.format(idVehicule)
    resp = messagebox.askokcancel(title="Voulez-vous supprimer ce véhicule ?", message=MsgboxText)

    if resp == True:
        DT.retirer_vehicule("./data/vehicules.json", int(idVehicule))
        app.destroy()
    else:
        app.destroy()


def sup_vehi_page(master):
    """
    [Description]

    :param master: master se réfaire à la page parent
    :return:
    """

    app = tk.Toplevel(master)
    app.geometry('920x640+500+125')
    app.attributes("-toolwindow", 1)# Supprime les boutons Réduire/Agrandir
    app.transient(master)
    app.resizable(False, False)
    app.title("Suupression Véhicle")

    varID = tk.StringVar()
    tk.LabelFrame(app, text="Nom").place(relx=0.05, rely=0.045, relheight=0.09, relwidth=0.2)
    tk.Entry(app, width=14, textvariable=varID).place(relx=0.06, rely=0.07, relheight=0.05, relwidth=0.18)

    btnValide = tk.Button(app, text='Valider',
                          command=lambda: valide(varID.get(), app))
    btnValide.place(relx=0.3, rely=0.55, relheight=0.05, relwidth=0.4)
