import json
import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import messagebox
import lib.DataTool as DT

# On ouvre bloc note ou notpad à l'aide de subprocess
import subprocess



presetUser = """"""
listeUser=["Selectionner une BDD", "BDD Client", "BDD Vehicule", "BDD Tarif"]



def open_json(json_path):
    
    f = open(json_path, 'r')
    s = f.read()
    f.close()
    
    """with open(json_path, 'r') as inside:
        data = json.load(inside)"""
    return s

def valide(numPermis, annulationInfo, app):
    msgboxText = """
           Base de donnée à modifier : {}
           """.format(annulationInfo)
    resp = messagebox.askokcancel(title="Voulez-vous modifier cette base de donnée ?", message=msgboxText)

    if resp == True:
        DT.retirer_client(DT.dfc, numPermis)
        app.destroy()
    else:
        app.destroy()


def modif_bdd_page(master):
    
    app = tk.Toplevel(master)
    h = app.winfo_screenheight()
    w = app.winfo_screenwidth()
    screen = str(round(w*0.748)) +"x" + str(round(h*0.91)) + "+" + str(round(w*0.246)) + "+" + str(round(h*0.052))
    app.geometry(screen)
    app.attributes("-toolwindow", 1)  # Supprime les boutons Réduire/Agrandir
    app.transient(master)
    app.resizable(False, False)
    app.title("Modification")
    
    
    def bdd_select(event):
        """
        [description]
        Fonction permettant de choisir la page à ouvrir parmi un menu déroulant

        :return:
        """

        global listeUser

        # Obtenir l'élément sélectionné
        select = listeCombo1.get()
        print("Vous avez sélectionné : '", select, "'")
        type(select)

        # print(listeUser)
        if select != "Selectionner une BDD":
            if select == "BDD Client":
                text_json = open_json("./data/clients.json")

                modifInfo.delete("1.0", "end")
                modifInfo.insert(tk.END, text_json)
                
                bt_editeur = tk.Button(label, text='Modification avancé depuis un éditeur par défaut',
                          command=lambda: subprocess.run(["notepad","./data/clients.json"]))
                bt_editeur.place(relx=0.3, rely=0.9, relheight=0.05, relwidth=0.4)

                
            if select == "BDD Vehicule":
                text_json = open_json("./data/vehicules.json")

                modifInfo.delete("1.0", "end")
                modifInfo.insert(tk.END, text_json)
                
                bt_editeur = tk.Button(label, text='Modification avancé depuis un éditeur par défaut',
                          command=lambda: subprocess.run(["notepad","./data/vehicules.json"]))
                bt_editeur.place(relx=0.3, rely=0.9, relheight=0.05, relwidth=0.4)
                
            if select == "BDD Tarif":
                text_json = open_json("./data/tarifs.json")

                modifInfo.delete("1.0", "end")
                modifInfo.insert(tk.END, text_json)
                
                bt_editeur = tk.Button(label, text='Modification avancé depuis un éditeur par défaut',
                          command=lambda: subprocess.run(["notepad","./data/tarifs.json"]))
                bt_editeur.place(relx=0.3, rely=0.9, relheight=0.05, relwidth=0.4)

        else:
            text_json = ""
            modifInfo.delete("1.0", "end")
            modifInfo.insert(tk.END, presetUser)
    
    
    label = tk.LabelFrame(app, text="Sélectionnez une Base De Donnée à modifier")
    label.place(relheight=1, relwidth=1)
    
    BtnValide = tk.Button(label, text='Valider', command=lambda: valide(app))
    BtnValide.place(relx=0.3, rely=0.8, relheight=0.05, relwidth=0.4)
    
    
    listeCombo1 = Combobox(label, height=200, width=27, values=listeUser)
    listeCombo1.current(0)
    listeCombo1.place(relx=0.3, rely=0.05, relheight=0.05, relwidth=0.4)
    listeCombo1.bind("<<ComboboxSelected>>", bdd_select)


    txtFrame = tk.Frame(app, borderwidth=1, relief="sunken")
    txtFrame.place(relx=0.1, rely=0.15, relheight=0.65, relwidth=0.8)

    
    modifInfo = tk.Text(txtFrame)
    modifInfo.insert(tk.END,presetUser.format("", "", "", "", ""))
    modifInfo.pack(side="left", fill="both", expand=True)
    
    vscroll = tk.Scrollbar(txtFrame, orient="vertical", command=modifInfo.yview)
    modifInfo['yscroll'] = vscroll.set
    vscroll.pack(side="right", fill="y")
    
    


    