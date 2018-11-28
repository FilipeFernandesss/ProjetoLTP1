from tkinter import *

class Venda_Carro(Toplevel):
    def __init__(self, parent, controle):

        super().__init__(parent)

        self.controle = controle

        self.geometry('215x320+200+200')
        self.title('Carro')
        self.transient(parent)
        self.grab_set()

        self.et_modelo = Entry(self)
        self.lb_modelo = Label(self, text='Modelo:')

        self.et_modelo.place(x=10, y=35)
        self.lb_modelo.place(x=10, y=10)

        self.et_placa = Entry(self)
        self.lbl_placa = Label(self, text='Placa:')

        self.et_placa.place(x=10, y=110)
        self.lbl_placa.place(x=10, y=85)

        self.et_preco = Entry(self)
        self.lbl_preco = Label(self, text='Preço:')

        self.et_preco.place(x=10, y=185)
        self.lbl_preco.place(x=10, y=160)

        self.button = Button(self, width=10, text='Ok', command=self.btn_on_click)
        self.button.place(x=60, y=250)

    def btn_on_click(self):
        print('teste')