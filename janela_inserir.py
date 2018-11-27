#Janela para inserir carros
from tkinter import *
from tkinter import messagebox

class Janela_Inserir(Toplevel):

    def __init__(self, parent, controle):
        super().__init__(parent)

        self.controle = controle


        self.geometry('328x340+200+200')
        self.title('Inserir')
        self.transient(parent)
        self.grab_set()
        self.deiconify()


        self.ed1 = Entry(self)
        self.lbl1 = Label(self, text='Marca:')

        self.ed1.place(x=10, y=35)
        self.lbl1.place(x=10, y=10)

        self.ed2 = Entry(self)
        self.lbl2 = Label(self, text='Modelo:')

        self.ed2.place(x=175, y=35)
        self.lbl2.place(x=175, y=10)

        self.ed3 = Entry(self)
        self.lbl3 = Label(self, text='Ano:')

        self.ed3.place(x=10, y=110)
        self.lbl3.place(x=10, y=85)

        self.ed4 = Entry(self)
        self.lbl4 = Label(self, text='Estado:')

        self.ed4.place(x=175, y=110)
        self.lbl4.place(x=175, y=85)

        self.ed5 = Entry(self)
        self.lbl5 = Label(self, text='Placa:')

        self.ed5.place(x=10, y=185)
        self.lbl5.place(x=10, y=160)

        self.ed6 = Entry(self)
        self.lbl6 = Label(self, text='Preço:')

        self.ed6.place(x=175, y=185)
        self.lbl6.place(x=175, y=160)

        self.botao = Button(self, width=15, text='OK', command=self.btn_on_click)
        self.botao.place(x=100, y=250)

    def btn_on_click(self):
        if len(self.ed1.get()) == 0 or len(self.ed2.get()) == 0 or len(self.ed3.get()) == 0 or len(self.ed4.get()) == 0 \
                or len(self.ed5.get()) == 0 or len(self.ed6.get()) == 0:

            messagebox.showerror("Error", "CAMPO EM BRANCO!")

        elif (str(self.ed3.get()).isnumeric() and str(self.ed6.get()).isnumeric()):
            self.controle.inserir(self.ed1.get(), self.ed2.get(), int(self.ed3.get()),
                                  self.ed4.get(), self.ed5.get(), float(self.ed6.get()))
            self.destroy()

        else:
            messagebox.showerror("Error", "Informação Incorreta")


