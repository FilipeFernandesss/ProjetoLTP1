from tkinter import *
from tkinter import messagebox
from janela_venda_carro import Venda_Carro

class Venda_Compradores(Toplevel):

    def __init__(self, parent, controle):
        super().__init__(parent)

        self.controle = controle

        self.geometry('201x230+200+200')
        self.title('Comprador')
        self.transient(parent)
        self.grab_set()

        self.et_nome = Entry(self)
        self.lb_nome = Label(self, text='Nome:')

        self.et_nome.place(x=10, y=35)
        self.lb_nome.place(x=10, y=10)

        self.et_cpf = Entry(self)
        self.lb_cpf = Label(self, text='CPF:')

        self.et_cpf.place(x=10, y=110)
        self.lb_cpf.place(x=10, y=85)

        self.button = Button(self, width=10, text='OK', command=self.btn_click)
        self.button.place(x=60, y=150)

    def criar_venda_carro(self):
        Venda_Carro(self, self.controle)

    def btn_click(self):
        if len(self.et_nome.get()) == 0 or len(self.et_cpf.get()) == 0:
            messagebox.showinfo(title='Erro', message='Campo em branco')
        else:
            self.controle.inserir_comprador(self.et_nome.get(), self.et_cpf.get())
            self.criar_venda_carro()
