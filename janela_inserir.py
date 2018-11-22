#Janela para inserir carros
from tkinter import *

class Janela_Inserir(Toplevel):

    def __init__(self, parent, controle):
        super().__init__(parent)

        self.controle = controle


        self.geometry('320x350+150+150')
        self.title('Inserir')
        self.transient(parent)
        self.grab_set()


        self.ed1 = Entry(self)
        self.btn1 = Button(self, width=7, text='OK')
        self.lbl1 = Label(self, text='Marca:')

        self.ed1.place(x=10, y=35)
        #self.btn1.place(x=10, y=55)
        self.lbl1.place(x=10, y=10)

        self.ed2 = Entry(self)
        self.btn2 = Button(self, width=7, text='OK')
        self.lbl2 = Label(self, text='Modelo:')

        self.ed2.place(x=175, y=35)
        #self.btn2.place(x=175, y=55)
        self.lbl2.place(x=175, y=10)

        self.ed3 = Entry(self)
        self.btn3 = Button(self, width=7, text='OK')
        self.lbl3 = Label(self, text='Ano:')

        self.ed3.place(x=10, y=150)
        #self.btn3.place(x=10, y=175)
        self.lbl3.place(x=10, y=125)

        self.ed4 = Entry(self)
        self.btn4 = Button(self, width=7, text='OK')
        self.lbl4 = Label(self, text='Estado:')

        self.ed4.place(x=175, y=150)
        #self.btn4.place(x=175, y=175)
        self.lbl4.place(x=175, y=125)

        self.ed5 = Entry(self)
        self.btn5 = Button(self, width=7, text='OK')
        self.lbl5 = Label(self, text='Placa:')

        self.ed5.place(x=10, y=265)
        #self.btn5.place(x=10, y=290)
        self.lbl5.place(x=10, y=240)

        self.ed6 = Entry(self)
        self.btn6 = Button(self, width=7, text='OK')
        self.lbl6 = Label(self, text='Preço:')

        self.ed6.place(x=175, y=265)
        #self.btn6.place(x=175, y=290)
        self.lbl6.place(x=175, y=240)

        self.botao = Button(self, width=12, text='OK', command=self.btn_on_click)
        self.botao.place(x=100, y=300)

    def btn_on_click(self):
        self.controle.inserir(self.ed1.get(), self.ed2.get(), self.ed3.get(),
                              self.ed4.get(), self.ed5.get(), self.ed6.get())
        self.destroy()


