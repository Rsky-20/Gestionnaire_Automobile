import tkinter as tk
from tkinter import messagebox
import lib.DataTool as DT


def valide(nom, prenom, age, num_perm, adress_mail, tel, app):
    """[summary]

    Args:
        nom ([type]): [description]
        prenom ([type]): [description]
        age ([type]): [description]
        num_perm ([type]): [description]
        adress_mail ([type]): [description]
        tel ([type]): [description]
        app ([type]): [description]
    """    
    
    if nom or prenom == "" and age or num_perm == 0:
        msgboxText = """
           Il y a une erreur dans les information renseignées. 
           Merci de bien vouloir les vérifier. 
           """
        messagebox.showerror(title="ERROR", message=msgboxText)
        
        
    else:
        
        msgboxText = """
        - Nom : {}
        - Prénom : {}
        - Age : {}
        - Numero de permis : {}
        - Numero de telephone : {}
        - Adresse mail : {}
        """.format(nom, prenom, age, int(num_perm), adress_mail, tel)
        
        resp = messagebox.askokcancel(
            title="Voulez-vous rajouter cet utilisateur ?", message=msgboxText)

        if resp:
            DT.ajouter_client(DT.dfc, nom, prenom, age, num_perm)
            app.destroy()
        else:
            #app.destroy()
            pass


def client_page(master):
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
    app.title("Page User")

    varNom = tk.StringVar()
    tk.LabelFrame(app, text="Nom").place(
        relx=0.05, rely=0.045, relheight=0.09, relwidth=0.2)
    tk.Entry(app, width=14, textvariable=varNom).place(
        relx=0.06, rely=0.07, relheight=0.05, relwidth=0.18)

    varPrenom = tk.StringVar()
    tk.LabelFrame(app, text="Prénom").place(
        relx=0.05, rely=0.145, relheight=0.09, relwidth=0.2)
    tk.Entry(app, width=14, textvariable=varPrenom).place(
        relx=0.06, rely=0.17, relheight=0.05, relwidth=0.18)

    varAge = tk.DoubleVar()
    tk.LabelFrame(app, text="Age").place(
        relx=0.05, rely=0.245, relheight=0.09, relwidth=0.5)
    tk.Scale(app, orient='horizontal', from_=18, to=90,
             resolution=1, variable=varAge).place(
                 relx=0.06, rely=0.27, relheight=0.062, relwidth=0.4)

    varNumPerm = tk.IntVar()
    tk.LabelFrame(app, text="Numero de permis").place(
        relx=0.05, rely=0.345, relheight=0.09, relwidth=0.2)
    tk.Entry(app, width=14, textvariable=varNumPerm).place(
        relx=0.06, rely=0.37, relheight=0.05, relwidth=0.18)

    varAdressMail = tk.StringVar()
    tk.LabelFrame(app, text="Adresse Mail").place(
        relx=0.35, rely=0.045, relheight=0.09, relwidth=0.2)
    tk.Entry(app, width=14, textvariable=varAdressMail).place(
        relx=0.36, rely=0.07, relheight=0.05, relwidth=0.18)

    varTel = tk.StringVar()
    tk.LabelFrame(app, text="Télephone").place(
        relx=0.35, rely=0.145, relheight=0.09, relwidth=0.2)
    tk.Entry(app, width=14, textvariable=varTel).place(
        relx=0.36, rely=0.17, relheight=0.05, relwidth=0.18)
    
    print(type(varNom),type(varPrenom),type(varAge),type(varNumPerm))


    btnValide = tk.Button(app, text='Valider', command=lambda: valide(
        varNom.get(), varPrenom.get(), varAge.get(),
        varNumPerm.get(), varAdressMail, varTel, app))
    btnValide.place(relx=0.3, rely=0.55, relheight=0.05, relwidth=0.4)
