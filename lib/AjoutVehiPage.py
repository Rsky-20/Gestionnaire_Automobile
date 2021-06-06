import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import messagebox
import lib.DataTool as DT

type_vehicule = ""
gamme_vehicule = ""
carburant_vehicule = ""

def valide(type_vehicule, marque_vehicule, modele_vehicule, gamme_vehicule,
           carburant_vehicule, km_vehicule, app):
    MsgboxText = """
------------Information véhicule-----------

Type: {}
Marque: {}
Modèle: {}
Gamme: {}
Carburant: {}
Km: {}
Location: NA (par défault)

""".format(type_vehicule, marque_vehicule, modele_vehicule, gamme_vehicule,
           carburant_vehicule, km_vehicule)

    if type_vehicule == "" or marque_vehicule == "" or modele_vehicule == "" or gamme_vehicule == "" or carburant_vehicule == "":
        msgboxText = """
           Il y a une erreur dans les information renseignées. 
           Merci de bien vouloir les vérifier. 
           """
        messagebox.showerror(title="ERROR", message=msgboxText)
    
    else:
        
        resp = messagebox.askokcancel(title="Voulez-vous Ajouter ce véhicules ?", message=MsgboxText)

        if resp == True:
            DT.ajouter_vehicule(DT.dfv, type_vehicule, marque_vehicule, modele_vehicule,
                                gamme_vehicule, carburant_vehicule, km_vehicule)
            app.destroy()
        else:
            pass



def ajout_vehi_page(master):
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
    app.attributes("-toolwindow", 1)# Supprime les boutons Réduire/Agrandir
    app.transient(master)
    app.resizable(False, False)
    app.title("Ajout Véhicle")
    
    def type_select(event):
        """
        [description]
        Fonction permettant de choisir la page à ouvrir parmi un menu déroulant

        :return:
        """

        global type_vehicule, carburant_vehicule
        #global km_vehicule, marque_vehicule, modele_vehicule

        # Obtenir l'élément sélectionné
        select = listeComboType.get()
        print("Vous avez sélectionné : '", select, "'")
        type(select)

        #print(listeUser)
        if select != "Selectionner un type de véhicule":
            if select == "T":
                type_vehicule = "T"
                
                tk.LabelFrame(app, text="Gamme du Véhicule").place(relx=0.35, rely=0.245, relheight=0.16, relwidth=0.221)
                lb_gamme = tk.Listbox(app)
                lb_gamme.insert(1, "BERLINE")
                lb_gamme.insert(2, "MONOSPACE")
                lb_gamme.insert(3, "SPORTIVE")
                lb_gamme.insert(4, "ELECTRIQUE")
                lb_gamme.place(relx=0.36, rely=0.27, relheight=0.12, relwidth=0.2)
                
                def select_lb(event):
                    global gamme_vehicule
                    i=lb_gamme.curselection()
                    gamme_vehicule = lb_gamme.get(i)
                lb_gamme.bind('<ButtonRelease-1>',select_lb)
                
            elif select == "U":
                type_vehicule = "T"
                
                tk.LabelFrame(app, text="Gamme du Véhicule").place(relx=0.35, rely=0.245, relheight=0.16, relwidth=0.221)
                lb_gamme = tk.Listbox(app)
                lb_gamme.insert(1, "3 A 5")
                lb_gamme.insert(2, "6 A 10")
                lb_gamme.insert(3, "11 A 15")
                lb_gamme.insert(4, "20 A 25") 
                lb_gamme.insert(4, "BENNE")
                lb_gamme.place(relx=0.36, rely=0.27,relheight=0.12, relwidth=0.2)
                
                def select_lb(event):
                    global gamme_vehicule
                    i=lb_gamme.curselection()
                    gamme_vehicule = lb_gamme.get(i)
                lb_gamme.bind('<ButtonRelease-1>',select_lb)
        else:
            print("ERROR No Selection Fund")
            pass
        
            
    
    labeLT = tk.LabelFrame(app, text="Sélectionnez un type")
    labeLT.place(relheight=1, relwidth=1)

    listeComboType = Combobox(labeLT, height=200, width=27, values=["Selectionner un type", "T", "U"])
    listeComboType.current(0)
    listeComboType.place(relx=0.1, rely=0.1, relheight=0.05, relwidth=0.2)
    listeComboType.bind("<<ComboboxSelected>>", type_select)
    
    ####
    
    varMarque = tk.StringVar()
    tk.LabelFrame(app, text="Marque du Véhicule").place(relx=0.1, rely=0.245, relheight=0.09, relwidth=0.2)
    tk.Entry(app, width=14, textvariable=varMarque).place(relx=0.11, rely=0.27, relheight=0.05, relwidth=0.18)
    
    varModele = tk.StringVar()
    tk.LabelFrame(app, text="Modèle du Véhicule").place(relx=0.1, rely=0.345, relheight=0.09, relwidth=0.2)
    tk.Entry(app, width=14, textvariable=varModele).place(relx=0.11, rely=0.37, relheight=0.05, relwidth=0.18)
        
    varKm = tk.StringVar()
    tk.LabelFrame(app, text="Km du Véhicule").place(relx=0.1, rely=0.445, relheight=0.09, relwidth=0.2)
    tk.Entry(app, width=14, textvariable=varKm).place(relx=0.11, rely=0.47, relheight=0.05, relwidth=0.18)
    
    def select_carburant():
        global carburant_vehicule
        carburant_vehicule = varCarburant.get()
    
    varCarburant = tk.StringVar()
    tk.LabelFrame(app, text="Carburant du Véhicule").place(relx=0.1, rely=0.545, relheight=0.09, relwidth=0.287)
    tk.Radiobutton(app, variable=varCarburant, text="ESSENCE", value="ESSENCE", indicatoron=0, command=select_carburant).place(relx=0.11, rely=0.58)
    tk.Radiobutton(app, variable=varCarburant, text="DIESEL", value="DIESEL", indicatoron=0, command=select_carburant).place(relx=0.21, rely=0.58)
    tk.Radiobutton(app, variable=varCarburant, text="ELECTRICITE", value="ELECTRICITE", indicatoron=0, command=select_carburant).place(relx=0.31, rely=0.58)
    
    ####
    
    BtnValide = tk.Button(app, text='Valider',
                          command=lambda: valide(type_vehicule,
                                                 varMarque.get(), varModele.get(), gamme_vehicule,
                                                 carburant_vehicule, varKm.get(), app))
    BtnValide.place(relx=0.3, rely=0.8, relheight=0.05, relwidth=0.4)
