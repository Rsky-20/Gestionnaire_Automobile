import tkinter as tk
import lib.DataTool as DT

def run(master):
    app = tk.Toplevel(master)
    app.title("Grille Véhicule")
    app.geometry("850x600+378+45")
    app.attributes("-toolwindow", 1)  # Supprime les boutons Réduire/Agrandir
    app.transient(master)
    app.resizable(False, False)

    frame = tk.Frame(app)
    frame.place(relwidth=1, relheight=1)
    
    text = tk.Text(frame)
    text.insert(tk.INSERT, DT.vehicules_libres(DT.dfv))
    text.config(state='disable')
    text.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)
    
    defilY = tk.Scrollbar(app, orient='vertical',
    command=text.yview)
    defilY.place(relx=0.9, rely=0.9, sticky='ns')