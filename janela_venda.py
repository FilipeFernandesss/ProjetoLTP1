#janela para exibir notas fiscais e realizar vendas
from janela_realizar_venda import Janela_Venda
from janela_exibir_nota import Janela_Exibir_Nota

from tkinter import *

class Janela_Vendas(Toplevel):
    def __init__(self, parent, controle):
        super().__init__(parent)

        self.controle = controle

        self.geometry('217x213+200+200')
        self.title('VENDA')
        self.transient(parent)
        self.grab_set()

        self.btn_realizar_venda = Button(self, width=13, text='Realizar venda', command=self.criar_realizar_venda)
        self.btn_exibir_nota = Button(self, width=13, text='Exibir Notas', command=self.criar_exibir_nota)
        self.btn_sair = Button(self, width=13, text='Voltar', command=self.destroy)

        self.btn_realizar_venda.place(x=50, y=20)
        self.btn_exibir_nota.place(x=50, y=85)
        self.btn_sair.place(x=50, y=150)

    def criar_realizar_venda(self):
        Janela_Venda(self, self.controle)

    def criar_exibir_nota(self):
        Janela_Exibir_Nota(self, self.controle)