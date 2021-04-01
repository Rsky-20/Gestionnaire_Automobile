import tkinter as tk

def User_Page(master):
    app = tk.Toplevel(master)
    app.geometry('920x640')
    app.w, app.h = app.winfo_screenwidth(), app.winfo_screenheight()
    app.title("Page User")
    app.B = tk.Button(app, text="recherche", command=None)
    app.B.place(x=700, y=45, height=40, width=100)

