import tkinter as tk
from tkinter import messagebox
import lib.DataTool as DT


def valide(Nom,Prenom, Age, NumPerm, AdressMail, Tel, app):
    """

    :param Nom:
    :param Prenom:
    :param Age:
    :param NumPerm:
    :param AdressMail:
    :param Tel:
    :return:
    """
    MsgboxText = """
    - Nom : {}
    - Prénom : {}
    - Age : {}
    - Numero de permis : {}
    - Numero de telephone : {}
    - Adresse mail : {}
    """.format(Nom,Prenom, Age, NumPerm, AdressMail, Tel)
    resp = messagebox.askokcancel(title="Voulez-vous rajouter cet utilisateur ?", message=MsgboxText)

    if resp == True:
        DT.ajouter_client("./data/clients.json", Nom, Prenom, Age, NumPerm)
        app.destroy()
    else:
        app.destroy()
        pass


def User_Page(master):
    """
    [Description]


    :param master: master se réfaire à la page parent
    :return:
    """

    app = tk.Toplevel(master)
    app.geometry('920x640')
    app.w, app.h = app.winfo_screenwidth(), app.winfo_screenheight()
    app.title("Page User")

    varNom = tk.StringVar()
    tk.LabelFrame(app, text="Nom").place(relx=0.05, rely=0.045, relheight=0.09, relwidth=0.2)
    tk.Entry(app, width=14, textvariable=varNom).place(relx=0.06, rely=0.07, relheight=0.05, relwidth=0.18)

    varPrenom = tk.StringVar()
    tk.LabelFrame(app, text="Prénom").place(relx=0.05, rely=0.145, relheight=0.09, relwidth=0.2)
    tk.Entry(app, width=14, textvariable=varPrenom).place(relx=0.06, rely=0.17, relheight=0.05, relwidth=0.18)

    varAge = tk.DoubleVar()
    tk.LabelFrame(app, text="Age").place(relx=0.05, rely=0.245, relheight=0.09, relwidth=0.5)
    tk.Scale(app, orient='horizontal', from_=18, to=90,
             resolution=1, variable=varAge).place(relx=0.06, rely=0.27, relheight=0.062, relwidth=0.4)

    varNumPerm = tk.StringVar()
    tk.LabelFrame(app, text="Numero de permis").place(relx=0.05, rely=0.345, relheight=0.09, relwidth=0.2)
    tk.Entry(app, width=14, textvariable=varNumPerm).place(relx=0.06, rely=0.37, relheight=0.05, relwidth=0.18)

    varAdressMail = tk.StringVar()
    tk.LabelFrame(app, text="Adresse Mail").place(relx=0.35, rely=0.045, relheight=0.09, relwidth=0.2)
    tk.Entry(app, width=14, textvariable=varAdressMail).place(relx=0.36, rely=0.07, relheight=0.05, relwidth=0.18)

    varTel = tk.StringVar()
    tk.LabelFrame(app, text="Télephone").place(relx=0.35, rely=0.145, relheight=0.09, relwidth=0.2)
    tk.Entry(app, width=14, textvariable=varTel).place(relx=0.36, rely=0.17, relheight=0.05, relwidth=0.18)

    BtnValide = tk.Button(app, text='Valider',
                          command=lambda:valide(varNom.get(), varPrenom.get(), varAge.get(),
                                                varNumPerm.get(), varAdressMail, varTel, app))
    BtnValide.place(relx=0.3, rely=0.55, relheight=0.05, relwidth=0.4)


