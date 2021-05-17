import tkinter as tk
from tkinter import *
from PIL import Image


def About_Page(master):
    """
    [Description]
    Fonction permettant de générer la page "à propos".

    :param master: master se réfaire à la page parent
    :return:
    """

    app = tk.Toplevel(master)
    app.geometry('920x640+500+125')
    app.attributes("-toolwindow", 1)# Supprime les boutons Réduire/Agrandir
    app.transient(master)
    app.resizable(False, False)
    app.title("A propos")

    # Background image
    self.image = PhotoImage(file='./images/fond.gif')
    self.canvas = Canvas(self.root, width=self.w, height=self.h)
    self.canvas.place(rely=0.0, relx=0.0, relwidth=1, relheight=1)
    self.canvas.create_image(0, 0, image=self.image, anchor=NW, )
    