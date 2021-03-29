import tkinter as tk
from tkinter.ttk import Combobox
from PIL import ImageTk, Image

class App(tk.Tk):

       def __init__(self):
           super().__init__()
           self.w, self.h = self.winfo_screenwidth(), self.winfo_screenheight()
           self.title("Nouvel onglet")
           self.geometry('1920x1080')
           self.iconbitmap('./image/téléchargement (9).ico')
           self.Widgets()



       def Widgets(self):
           self.var = tk.StringVar()

           tk.Button(self, text='Open another window', command=self.open_Page).place(x=600, y=300, height=60, width=300)

           self.L = tk.Label(self, text="G", font='Times 32', fg='blue').place(x=600, y=10, height=50, width=50)

           self.L1 = tk.Label(self, text="O", font='Times 32', fg='red').place(x=650, y=10, height=50, width=50)

           self.L2 = tk.Label(self, text="O", font='Times 32', fg='yellow').place(x=700, y=10, height=50,
                                                                                         width=50)

           self.L3 = tk.Label(self, text="G", font='Times 32', fg='blue').place(x=750, y=10, height=50, width=50)

           self.L4 = tk.Label(self, text="L", font='Times 32', fg='green').place(x=800, y=10, height=50,
                                                                                        width=50)

           self.L5 = tk.Label(self, text="E", font='Times 32', fg='red').place(x=850, y=10, height=50, width=50)

           self.Entry = tk.Entry(self, width=14, textvariable=self.var).place(x=400, y=70, height=30, width=700)

           self.B = tk.Button(self, text="recherche", command=self.ftest).place(x=700, y=110, height=30,
                                                                                       width=100)

       def ftest(self):


           if str(self.var) == 'Tripadvisor':
               self.l2 = tk.Label(self, text=str(self.var.get()), font='Times 32', bg='white').place(x=550,
                                                                                                            y=150,
                                                                                                            height=50,
                                                                                                            width=400)
               self.open_Page()
           else:
               self.l3 = tk.Label(self, text="ERROR 404", font='Times 32 bold', bg='red').place(x=550, y=150,
                                                                                                    height=50,
                                                                                                    width=400)

       def open_Page(self):
           d = Tripadvisor(self)
           d.wait_window()

class Tripadvisor(tk.Toplevel):

       def __init__(self, parent):
           super().__init__(parent)
           self.image = Image.open("./image/Fond.png")
           self.geometry('1920x1080')
           self.w, self.h = self.winfo_screenwidth(), self.winfo_screenheight()


           self.image = self.image.resize((self.w, self.h))

           # print(image) # <PIL.Image.Image image mode=RGBA size=1920x1080 at 0x43D5AB0>
           self.photo = ImageTk.PhotoImage(self.image)

           # pour que le canvas n'ai pas de bourdure qui reste autour
           self.can = tk.Canvas(self, highlightthickness=0)
           self.can.create_image(0, 0, anchor='nw', image=self.photo)
           self.can.pack(fill='both', expand=1)

           self.iconbitmap('./image/TA_brand_logo.ico')
           self.title("Page Tripadvisor")
           self.page()



       def l(self):
           # Obtenir l'élément sélectionné
           tk.Label(self, height=2, width=27, text='Error No data available').place(x=358, y=45, height=40,
                                                                                         width=348)

       def action1(self):
           # Obtenir l'élément sélectionné
           self.select = self.listeCombo1.get()
           print("Vous avez sélectionné la devise : '", self.select, "'")
           tk.Label(self, height=2, width=27, text=self.select).place(x=1005, y=700)

       def action2(self):
           # Obtenir l'élément sélectionné
           self.select = self.listeCombo2.get()
           print("Vous avez sélectionné le pays : '", self.select, "'")
           tk.Label(self, height=2, width=27, text=self.select).place(x=1230, y=700)

       def f(self):
           self.image = Image.open("./image/Capture5.PNG")

           self.render = ImageTk.PhotoImage(self.image)
           self.img = tk.Label(self, image=self.render)
           self.img.image = self.render
           self.img.place(x=300, y=100)

       def clicked(self):
           print(self.selected.get())
           tk.Label(self, text="Vous avez choisie l'annonce rapide : " + self.selected.get()).place(x=750, y=400)

       def page(self):
           self.var = tk.StringVar()
           self.Entry = tk.Entry(self, width=14, textvariable=self.var)
           self.Entry.place(x=358, y=45, height=40, width=348)

           self.B = tk.Button(self, text="recherche", command=self.l)
           self.B.place(x=700, y=45, height=40, width=100)

           # labelChoix = Label(root, text = "Veuillez faire un choix !")
           # labelChoix.place()

           self.listeDevise = ["€ EUR Euros", "$ US-USD Dollars américains", "£ GBP Livres sterling",
                               "JPY Yens japonais"]

           self.listeCombo1 = Combobox(self, height=200, width=27, values=self.listeDevise)

           self.listeCombo1.current(0)

           self.listeCombo1.place(x=1005, y=750)

           self.listeCombo1.bind("<<ComboboxSelected>>", self.action1)

           self.listePays = ["France", "USA", "Angleterre", "Japon"]

           self.listeCombo2 = Combobox(self, height=200, width=27, values=self.listePays)

           self.listeCombo2.current(0)

           self.listeCombo2.place(x=1230, y=750)

           self.listeCombo2.bind("<<ComboboxSelected>>", self.action2)

           tk.Button(self, text='Annonce Rapide', command=self.f).place(x=805, y=45, height=40, width=100)

           self.selected = tk.StringVar()

           self.rad1 = tk.Radiobutton(self, text='First', value=1, variable=self.selected).place(x=620, y=360)

           self.rad2 = tk.Radiobutton(self, text='Second', value=2, variable=self.selected).place(x=850, y=360)

           self.rad3 = tk.Radiobutton(self, text='Third', value=3, variable=self.selected).place(x=1100, y=360)

           self.btn = tk.Button(self, text="Click Me", command=self.clicked).place(x=400, y=360)


if __name__ == '__main__':
       app = App()
       app.mainloop()