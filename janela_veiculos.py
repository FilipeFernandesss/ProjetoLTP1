#Janela principal do programa
from tkinter import *
from janela_excluir import Janela_Excluir
from janela_inserir import Janela_Inserir
from janela_exibir import Janela_Exibir


class Janela_Veiculos(Toplevel):
    def __init__(self,parent, controle):
        super().__init__(parent)

        self.controle = controle


        self.geometry('350x400+200+200')
        self.title('VEÍCULOS')
        self.transient(parent)
        self.grab_set()

        btn_exibit = Button(self, width=20, text='Exibir carros', command=self.janela_exibir)
        btn_inserir = Button(self, width=20,text='Inserir novo carro', command=self.janela_inserir)
        btn_excluir = Button(self, width=20, text='Excluir carro', command=self.janela_excluir)
        btn_sair = Button(self, width=20, text='Voltar', command=self.destroy)

        btn_exibit.place(x=100,y=40)
        btn_inserir.place(x=100,y=140)
        btn_excluir.place(x=100,y=240)
        btn_sair.place(x=100, y=340)

    def janela_excluir(self):
        Janela_Excluir(self, self.controle)

    def janela_inserir(self):
        Janela_Inserir(self, self.controle)

    def janela_exibir(self):
        Janela_Exibir(self, self.controle)

