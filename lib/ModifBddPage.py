import json
import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import messagebox
import lib.DataTool as DT

# On ouvre bloc note ou notpad à l'aide de subprocess
import subprocess



preset_BDD = """"""
liste_BDD = ["Selectionner une BDD", "BDD Client", "BDD Vehicule", "BDD Tarif"]
text_json = ""
selected_BDD = ""



def open_json(json_path):
    
    with open(json_path, 'r') as json_file:
        js_read = json_file.read()
        
    return js_read

def enregistre_json(json_path, data):
        json_file = open(json_path, 'w')
        js_write = json_file.write(data) #, indent=4
        json_file.close()
        return js_write


def valide(bdd, selected_BDD, app):
    msgboxText = """
Base de donnée à modifier :
{}
           """.format(selected_BDD)
    resp = messagebox.askokcancel(title="Voulez-vous modifier cette base de donnée ?", message=msgboxText)

    if resp == True:
        enregistre_json(selected_BDD, bdd)
        app.destroy()
    else:
        pass


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

        global liste_BDD, text_json, selected_BDD

        # Obtenir l'élément sélectionné
        select = listeCombo1.get()
        print("Vous avez sélectionné : '", select, "'")
        type(select)

        # print(liste_BDD)
        if select != "Selectionner une BDD":
            if select == "BDD Client":
                selected_BDD = "./data/clients.json"
                text_json = open_json(selected_BDD)
                ##test print(text_json)

                modifInfo.delete("1.0", "end")
                modifInfo.insert(tk.END, text_json)
                
                bt_editeur = tk.Button(label, text='Modification avancé depuis un éditeur par défaut',
                          command=lambda: subprocess.run(["notepad","./data/clients.json"]))
                bt_editeur.place(relx=0.3, rely=0.9, relheight=0.05, relwidth=0.4)

                
            if select == "BDD Vehicule":
                selected_BDD = "./data/vehicules.json"
                text_json = open_json(selected_BDD)
                ##test print(text_json)

                modifInfo.delete("1.0", "end")
                modifInfo.insert(tk.END, text_json)
                
                bt_editeur = tk.Button(label, text='Modification avancé depuis un éditeur par défaut',
                          command=lambda: subprocess.run(["notepad","./data/vehicules.json"]))
                bt_editeur.place(relx=0.3, rely=0.9, relheight=0.05, relwidth=0.4)
                
            if select == "BDD Tarif":
                selected_BDD = "./data/tarifs.json"
                text_json = open_json(selected_BDD)
                ##test print(text_json)

                modifInfo.delete("1.0", "end")
                modifInfo.insert(tk.END, text_json)
                
                bt_editeur = tk.Button(label, text='Modification avancé depuis un éditeur par défaut',
                          command=lambda: subprocess.run(["notepad","./data/tarifs.json"]))
                bt_editeur.place(relx=0.3, rely=0.9, relheight=0.05, relwidth=0.4)

        else:
            text_json = ""
            modifInfo.delete("1.0", "end")
            modifInfo.insert(tk.END, preset_BDD)
    
    
    label = tk.LabelFrame(app, text="Sélectionnez une Base De Donnée à modifier")
    label.place(relheight=1, relwidth=1)
    
    BtnValide = tk.Button(label, text='Valider', command=lambda: valide(modifInfo.get(1.0, tk.END), selected_BDD, app))
    BtnValide.place(relx=0.3, rely=0.8, relheight=0.05, relwidth=0.4)
    
    
    listeCombo1 = Combobox(label, height=200, width=27, values=liste_BDD)
    listeCombo1.current(0)
    listeCombo1.place(relx=0.3, rely=0.05, relheight=0.05, relwidth=0.4)
    listeCombo1.bind("<<ComboboxSelected>>", bdd_select)


    txtFrame = tk.Frame(app, borderwidth=1, relief="sunken")
    txtFrame.place(relx=0.1, rely=0.15, relheight=0.65, relwidth=0.8)

    
    modifInfo = tk.Text(txtFrame)
    modifInfo.configure(font=("Tahoma", 16))
    modifInfo.insert(tk.END,preset_BDD.format("", "", "", "", ""))
    modifInfo.pack(side="left", fill="both", expand=True)
    
    vscroll = tk.Scrollbar(txtFrame, orient="vertical", command=modifInfo.yview)
    modifInfo['yscroll'] = vscroll.set
    vscroll.pack(side="right", fill="y")
    
    


    