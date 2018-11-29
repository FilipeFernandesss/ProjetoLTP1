#Janela para exibir os compradores
from tkinter import *

class Janela_Exibir_Compradores(Toplevel):
    def __init__(self, parent, controle):
        super().__init__(parent)

        self.controle = controle

        self.geometry('631x730+370+0')
        self.title('Exibir Notas Fiscais')
        self.transient(parent)
        self.grab_set()

        self.label = []
        ct = 0
        variancia = 1

        #Realiza um for na lista de notas fiscal e recebe o nome e cpf do comprador e o modelo e placa do carro e exibe em um label
        for nota_fiscal in self.controle.bd_nota.lista_nota_fiscal:
            texto = 'Nome Comprador: ' + nota_fiscal.nome_comprador + ' ; ' + 'CPF Comprador: ' + nota_fiscal.cpf_comprador \
                    + ' ; ' + 'Modelo: ' + nota_fiscal.modelo + ' ; ' + 'Placa: ' + nota_fiscal.placa


            label = Label(self, text=texto, font='Arial 11')
            self.label.append(label)
            self.label[ct].place(x=5, y=variancia * 25)
            ct += 1
            variancia += 1.8

