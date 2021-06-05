import tkinter as tk
import lib.DataTool as DT

def run(master):
    app = tk.Toplevel(master)
    app.title("Grille Véhicule")
    h = app.winfo_screenheight()
    w = app.winfo_screenwidth()
    screen = str(round(w*0.6)) +"x" + str(round(h*0.60)) + "+" + str(round(w*0.246)) + "+" + str(round(h*0.052))
    app.geometry(screen)
    app.attributes("-toolwindow", 1)  # Supprime les boutons Réduire/Agrandir
    app.transient(master)
    app.resizable(False, False)

    frame = tk.Frame(app)
    frame.place(relwidth=1, relheight=1)

    text = tk.Text(frame)
    text.insert(tk.INSERT, DT.aff_vehicule(DT.dfv))
    text.config(state='disable')
    text.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)
