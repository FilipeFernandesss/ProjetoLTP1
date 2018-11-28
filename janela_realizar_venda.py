from tkinter import *
from janela_venda_compradores import Venda_Compradores


class Janela_Venda(Toplevel):

    def __init__(self, parent, controle):
        super().__init__(parent)

        self.controle = controle

        self.geometry('215x320+200+200')
        self.title('Realizar venda')
        self.transient(parent)
        self.grab_set()

        self.et_matricula = Entry(self)
        self.lb_matricula = Label(self, text='Digite a matrícula:')

        self.et_matricula.place(x=10, y=35)
        self.lb_matricula.place(x=10, y=10)

        self.btn = Button(self, width=10, text='OK', command=self.btn_click)
        self.btn.place(x=10, y=50)

    def criar_comprador(self):
        Venda_Compradores(self, self.controle)

    def btn_click(self):
        for vendedor in self.controle.bd_vendedores.lista_vendedores:
            if int(self.et_matricula.get()) == vendedor.get_matricula():
                self.criar_comprador()
