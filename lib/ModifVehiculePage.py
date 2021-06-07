import tkinter as tk
from tkinter import messagebox
import lib.DataTool as DT


def valide(id_vehi, type, mark, mod, carb, gamme, kilo, app):
    """[summary]

    Args:
        id_vehi ([type]): [description]
        type ([type]): [description]
        mark ([type]): [description]
        mod ([type]): [description]
        carb ([type]): [description]
        gamme ([type]): [description]
        kilo ([type]): [description]
        app ([type]): [description]
    """    
    
    if type == "" or mark == "" or mod == "" or carb == "" or gamme == "" and id_vehi != 0 or kilo == 0:
        msgboxText = """
           Il y a une erreur dans les information renseignées. 
           Merci de bien vouloir les vérifier. 
           """
        messagebox.showerror(title="ERROR", message=msgboxText)
        
        
    else:
        
        msgboxText = """
- Id : {}
- Type : {}
- Marque : {}
- Modèle : {}
- Carburant : {}
- Gamme : {}
- Nombre de Km : {}
        """.format(id_vehi, type, mark, mod, carb, gamme, kilo)
        
        resp = messagebox.askokcancel(
            title="Voulez-vous modifier ce vehicule ?", message=msgboxText)

        if resp:
            DT.modifier_véhicule(DT.dfv, id_vehi, type, mark, mod, carb, gamme, kilo)
            app.destroy()
        else:
            #app.destroy()
            pass



def modif_vehicule_page(master):
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
    app.title("Modification Client")
    
    varId = tk.IntVar()
    tk.LabelFrame(app, text="Id véhicule").place(
        relx=0.4, rely=0.045, relheight=0.09, relwidth=0.2)
    tk.Entry(app, width=14, textvariable=varId).place(
        relx=0.41, rely=0.07, relheight=0.05, relwidth=0.18)

    varType = tk.StringVar()
    tk.LabelFrame(app, text="Type [T/U]").place(
        relx=0.4, rely=0.145, relheight=0.09, relwidth=0.2)
    tk.Entry(app, width=14, textvariable=varType).place(
        relx=0.41, rely=0.17, relheight=0.05, relwidth=0.18)

    varMarque = tk.StringVar()
    tk.LabelFrame(app, text="Marque").place(
        relx=0.4, rely=0.245, relheight=0.09, relwidth=0.2)
    tk.Entry(app, width=14, textvariable=varMarque).place(
        relx=0.41, rely=0.27, relheight=0.05, relwidth=0.18)
    
    varModele = tk.StringVar()
    tk.LabelFrame(app, text="Modèle").place(
        relx=0.4, rely=0.345, relheight=0.09, relwidth=0.2)
    tk.Entry(app, width=14, textvariable=varModele).place(
        relx=0.41, rely=0.37, relheight=0.05, relwidth=0.18)
    
    varCarburant = tk.StringVar()
    tk.LabelFrame(app, text="Carburant [ESSENCE, DIESEL, ELECTRIC").place(
        relx=0.4, rely=0.445, relheight=0.09, relwidth=0.2)
    tk.Entry(app, width=14, textvariable=varCarburant).place(
        relx=0.41, rely=0.47, relheight=0.05, relwidth=0.18)
    
    varGamme = tk.StringVar()
    tk.LabelFrame(app, text="Gamme").place(
        relx=0.4, rely=0.545, relheight=0.09, relwidth=0.2)
    tk.Entry(app, width=14, textvariable=varGamme).place(
        relx=0.41, rely=0.57, relheight=0.05, relwidth=0.18)
    
    varKm = tk.IntVar()
    tk.LabelFrame(app, text="Nombre de KM").place(
        relx=0.4, rely=0.645, relheight=0.09, relwidth=0.2)
    tk.Entry(app, width=14, textvariable=varKm).place(
        relx=0.41, rely=0.67, relheight=0.05, relwidth=0.18)


    btnValide = tk.Button(app,
                          text='Valider',
                          command=lambda: valide(varId.get(),
                                                 varType.get(),varMarque.get(),
                                                 varModele.get(),varCarburant.get(),
                                                 varGamme.get(),varKm, app))
    btnValide.place(relx=0.3, rely=0.75, relheight=0.05, relwidth=0.4)