#Janela referente aos vendedores
from tkinter import *
from janela_inserir_vendedor import Janela_Inserir_Vendedor
from janela_excluir_vendedor import Janela_Exluir_Vendeder
from janela_exibir_vendedores import Janela_Exibir_Vendedores


class Janela_Vendedor(Toplevel):
    def __init__(self, parent, controle):
        super().__init__(parent)

        self.controle = controle

        self.geometry('350x400+200+200')
        self.title('VENDEDORES')
        self.transient(parent)
        self.grab_set()

        btn_exibir_vendedeores = Button(self, width=20, text='Exibir Vendedores', command=self.criar_janela_exibir)
        btn_inserir_vendedor = Button(self, width=20, text='Inserir Novo Vendedor', command=self.criar_janela_inserir)
        btn_excluir_vendedor = Button(self, width=20, text='Excluir Vendedor', command=self.criar_janela_excluir)
        btn_sair = Button(self, width=20, text='Voltar', command=self.destroy)

        btn_exibir_vendedeores.place(x=100, y=40)
        btn_inserir_vendedor.place(x=100, y=140)
        btn_excluir_vendedor.place(x=100, y=240)
        btn_sair.place(x=100, y=340)

    def criar_janela_inserir(self):
        Janela_Inserir_Vendedor(self, self.controle)

    def criar_janela_excluir(self):
        Janela_Exluir_Vendeder(self, self.controle)

    def criar_janela_exibir(self):
        Janela_Exibir_Vendedores(self, self.controle)
