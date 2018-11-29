#Tela principal do programa
from tkinter import *
from janela_veiculos import Janela_Veiculos
from janela_vendedores import Janela_Vendedor
from janela_venda import Janela_Vendas
from janela_exibir_compradores import Janela_Exibir_Compradores

class Tela_Principal(Tk):

    def __init__(self, controle):
        self.controle = controle

        super().__init__()

        self.geometry('350x400+200+200')
        self.title('JANELA PRINCIPAL')

        btn_veiculos = Button(self, width=20, text='Veículos', command=self.criar_veiculos)
        btn_vendedores = Button(self, width=20,text='Vendedores', command=self.criar_vendedor)
        btn_compradores = Button(self, width=20, text='Compradores', command=self.criar_exibir_compradores)
        btn_realizar_venda = Button(self, width=20, text='Vendas', command=self.criar_vendas)
        btn_sair = Button(self, width=20, text='Sair', command=self.destroy)

        btn_veiculos.place(x=100, y=20)
        btn_vendedores.place(x=100, y=100)
        btn_compradores.place(x=100, y=180)
        btn_realizar_venda.place(x=100, y=260)
        btn_sair.place(x=100, y=340)

    def criar_veiculos(self):
        Janela_Veiculos(self, self.controle)

    def criar_vendedor(self):
        Janela_Vendedor(self, self.controle)

    def criar_vendas(self):
        Janela_Vendas(self, self.controle)

    def criar_exibir_compradores(self):
        Janela_Exibir_Compradores(self, self.controle)
