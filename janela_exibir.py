#Classe para a exibição dos carros
from tkinter import *
from janela_exibir_label import Janela_Exibir_Label


class Janela_Exibir(Toplevel):

    def __init__(self, parent, controle):
        super().__init__(parent)

        self.controle = controle

        self.geometry('307x328+200+200')
        self.title('Exibir')
        self.transient(parent)
        self.grab_set()

        self.btn = []
        varianca = 1
        ct = 0
        text = None

        for carro in self.controle.bd.lista_carros:
            print(carro)

            text = 'Carro', ct+1

            botao = Button(self, width=8, text=text, command=self.criar_label)

            self.btn.append(botao)
            self.btn[ct].place(x=varianca*10, y=15)
            ct += 1
            varianca += 7.5


        print(self.btn)

    def criar_label(self):
        Janela_Exibir_Label(self, self.controle)