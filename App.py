import tkinter as tk
from tkinter import *
#from lib.packages import NewScreen
import lib.packages as pkg

class MainApp():

    def __init__(self):
        super().__init__()
        self.root = tk.Tk()
        self.w, self.h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.title("Gestionnaire Automobile")
        self.root.geometry('1920x1080')
        # self.iconbitmap('./image/téléchargement (9).ico')
        self.Widgets()
        self.root.mainloop()

    def Widgets(self):
        self.banner = tk.Frame(self.root, bg="black")
        self.banner.place(relwidth=0.25, relheight=1)

        self.user = tk.Button(self.banner, text='USER',command=lambda:pkg.User_Page(self.root)).place(relx=0.3, rely=0.2, relheight=0.05, relwidth=0.4)

        self.reservation = tk.Button(self.banner, text='RESERVATION').place(relx=0.3, rely=0.3, relheight=0.05,
                                                                            relwidth=0.4)

        self.annulation = tk.Button(self.banner, text='ANNULATION').place(relx=0.3, rely=0.4, relheight=0.05,
                                                                          relwidth=0.4)

        self.admin = tk.Button(self.banner, text='ADMIN').place(relx=0.3, rely=0.55,
                                                                                           relheight=0.05,
                                                                                           relwidth=0.4)
        # command=self.start_onglet,
        self.listeAdmin = tk.Listbox(self.banner, height=10, width=10)
        self.listeAdmin.place(relx=0.3, rely=0.60, relheight=0.07, relwidth=0.4)

        for element in ["Ajout Véhicule", "Suppression Véhicule", "Suppréssion Utilisateur"]:
            self.listeAdmin.insert(END, element)

    def user_Page(self):
        d = (self.root)
        d.wait_window()


if __name__ == '__main__':
    app = MainApp()