import tkinter as tk
import lib.DataTool as DT

def run(master):
    app = tk.Toplevel(master)
    app.title("Grille Client")
    app.geometry("600x450+500+150")
    app.attributes("-toolwindow", 1)  # Supprime les boutons Réduire/Agrandir
    app.transient(master)
    app.resizable(False, False)

    frame = tk.Frame(app)
    frame.place(relwidth=1, relheight=1)

    text = tk.Text(frame)
    text.insert(tk.INSERT, DT.InformationPersonnelClientReserver(DT.dfc))
    text.config(state='disable')
    text.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)