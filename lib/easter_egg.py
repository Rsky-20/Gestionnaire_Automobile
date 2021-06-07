import tkinter as tk
from tkinter import *
import lib.DataTool as DT
from PIL import Image, ImageTk
import time

ind = -1

def easter_egg_page(x, y, master):
    """
    [Description]
    Fonction permettant de générer la page "à propos".

    :param master: master se réfaire à la page parent
    :return:
    """

    app = tk.Toplevel(master)
    h = app.winfo_screenheight()
    w = app.winfo_screenwidth()
    screen = str(round(w*0.45)) +"x" + str(round(h*0.60)) + "+" + str(x) + "+" + str(y) ## round(w*0.246) round(h*0.052)
    app.geometry(screen)
    app.attributes("-toolwindow", 1)# Supprime les boutons Réduire/Agrandir
    app.transient(master)
    app.resizable(False, False)
    app.title("Easter Egg")
    
    can = Canvas(app, width=50, height=50, bg='white')
    can.pack(side='top', fill='both', expand='yes')
    photo = PhotoImage(file="./easter_egg/dancing-rabbit-30.gif")
    can.create_image(0,0,anchor='nw', image=photo, tag='photo')
    
    def update(delay=200):
        global ind
        ind += 1
        if ind == 8: ind = 0
        photo.configure(format="gif -index " + str(ind))
        app.after(delay, update)
    
    update()
    
"""    image = PhotoImage(file="./easter_egg/dancing-rabbit-30.gif")
    canvas = Canvas(app)
    canvas.place(rely=0.0, relx=0.0, relwidth=1, relheight=1)
    canvas.create_image(0, 0, image=image, anchor=NW, )"""