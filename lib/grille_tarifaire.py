import tkinter as tk
import lib.DataTool as DT

def run(master):
    app = tk.Toplevel(master)
    app.title("Grille tarifiare")
    app.geometry("400x250+500+150")
    app.attributes("-toolwindow", 1)  # Supprime les boutons Réduire/Agrandir
    app.transient(master)
    app.resizable(False, False)

    frame = tk.Frame(app)
    frame.place(relwidth=1, relheight=1)

    text = tk.Text(frame)
    text.insert(tk.INSERT, DT.aff_tarifs())
    text.config(state='disable')
    text.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)
