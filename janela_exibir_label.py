#classe para exibição das informações dos carros
from tkinter import *

class Janela_Exibir_Label(Toplevel):
    def __init__(self, parent, controle):
        super().__init__(parent)

        self.controle = controle

        self.geometry('307x328+200+200')
        self.title('Exibir Informações')
        self.transient(parent)
        self.grab_set()

        self.label = []
        ct = 0

        car = self.controle.bd.lista_carros


        for carro in self.controle.bd.lista_carros:
            print(carro)
            texto = 'Marca:' + carro.marca + '\n' + 'Modelo:' + carro.modelo
            print(texto)

            label = Label(self, text=texto)
            self.label.append(label)
            self.label[ct].place(x=10, y=25)
            ct += 1