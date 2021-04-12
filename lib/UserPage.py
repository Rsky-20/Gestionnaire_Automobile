import tkinter as tk



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

    app.Nom = tk.LabelFrame(app, text="Nom")
    app.Nom.place(relx=0.05, rely=0.045, relheight=0.09, relwidth=0.2)
    varNom = tk.StringVar()
    tk.Entry(app, width=14, textvariable=varNom).place(relx=0.06, rely=0.07, relheight=0.05, relwidth=0.18)

    app.Prenom = tk.LabelFrame(app, text="Prénom")
    app.Prenom.place(relx=0.05, rely=0.145, relheight=0.09, relwidth=0.2)
    varPrenom = tk.StringVar()
    tk.Entry(app, width=14, textvariable=varPrenom).place(relx=0.06, rely=0.17, relheight=0.05, relwidth=0.18)

    app.Age = tk.LabelFrame(app, text="Age")
    app.Age.place(relx=0.05, rely=0.245, relheight=0.09, relwidth=0.5)

    varAge = tk.DoubleVar()
    tk.Scale(app.Age, orient='horizontal', from_=18, to=150,
          resolution=1, variable=varAge).place(relx=0, rely=0, relheight=1, relwidth=1)

    print(str(varAge.get()))

    #tk.Entry(app, width=14, textvariable=varAge)

    app.NumPerm = tk.LabelFrame(app, text="Numero de permis")
    app.NumPerm.place(relx=0.05, rely=0.345, relheight=0.09, relwidth=0.2)
    varNumPerm = tk.StringVar()
    tk.Entry(app, width=14, textvariable=varNumPerm).place(relx=0.06, rely=0.37, relheight=0.05, relwidth=0.18)

    app.AdressMail = tk.LabelFrame(app, text="Adresse Mail")
    app.AdressMail.place(relx=0.35, rely=0.045, relheight=0.09, relwidth=0.2)
    varAdressMail = tk.StringVar()
    tk.Entry(app, width=14, textvariable=varAdressMail).place(relx=0.36, rely=0.07, relheight=0.05, relwidth=0.18)

    app.Tel = tk.LabelFrame(app, text="Télephone")
    app.Tel.place(relx=0.35, rely=0.145, relheight=0.09, relwidth=0.2)
    varTel = tk.StringVar()
    tk.Entry(app, width=14, textvariable=varTel).place(relx=0.36, rely=0.17, relheight=0.05, relwidth=0.18)
