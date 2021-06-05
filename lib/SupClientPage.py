import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import messagebox
import lib.DataTool as DT


listeUser = ["Selectionner un utilisateur"] + DT.InformationPersonnel(DT.dfc) #DT.InformationPersonnel(DT.dfc)
supClient = ""
numPermis = int()
presetUser = """
Nom: {}
Prenom: {}
Numero permis: {}
Tel: {}
Email: {}

"""


def valide(numPermis, annulationInfo, app):
    msgboxText = """
           Réservation à supprimer : {}
           """.format(annulationInfo)
    resp = messagebox.askokcancel(title="Voulez-vous annuler ce client ?", message=msgboxText)

    if resp == True:
        print(type(numPermis))
        print(numPermis)
        print()
        print(DT.dfc)
        DT.dfc = DT.retirer_client(DT.dfc, numPermis)
        print(DT.dfc)
        app.destroy()
    else:
        app.destroy()



def sup_client_page(master):
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
    app.title("Supréssion Client")
    
    
    def user_select(event):
        """
        [description]
        Fonction permettant de choisir la page à ouvrir parmi un menu déroulant

        :return:
        """

        global supClient, listeUser, numPermis

        # Obtenir l'élément sélectionné
        select = listeCombo1.get()
        print("Vous avez sélectionné : '", select, "'")
        type(select)

        # print(listeUser)
        if select != "Selectionner un utilisateur":
            selectedUser = select.split(" ")
            print(selectedUser)

            user = DT.aff_info_client(DT.dfc, selectedUser)

            supClient = presetUser.format(user[0], user[1], user[3], "", "",)
            numPermis = user[3]
            print(numPermis)

            userInfo.delete("1.0", "end")
            userInfo.insert(tk.END, supClient)

        else:
            supClient = ""
            userInfo.delete("1.0", "end")
            userInfo.insert(tk.END, presetUser.format("", "", "", "", ""))
            
    
    label = tk.LabelFrame(app, text="Sélectionnez l'utilisateur à supprimer")
    label.place(relheight=1, relwidth=1)
    
    BtnValide = tk.Button(label, text='Valider', command=lambda: valide(numPermis, supClient, app))
    BtnValide.place(relx=0.3, rely=0.8, relheight=0.05, relwidth=0.4)
    
    listeCombo1 = Combobox(label, height=200, width=27, values=listeUser)
    listeCombo1.current(0)
    listeCombo1.place(relx=0.3, rely=0.1, relheight=0.05, relwidth=0.4)
    listeCombo1.bind("<<ComboboxSelected>>", user_select)

    userInfo = tk.Text(label)
    userInfo.insert(tk.END,presetUser.format("", "", "", "", ""))
    userInfo.place(relx=0.3, rely=0.15, relheight=0.6, relwidth=0.4)