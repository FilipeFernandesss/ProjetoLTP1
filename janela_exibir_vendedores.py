#janela para exibir vendedores

from tkinter import *

class Janela_Exibir_Vendedores(Toplevel):
    def __init__(self, parent, controle):
        super().__init__(parent)

        self.controle = controle

        self.geometry('507x730+370+0')
        self.title('Exibir Vendedores')
        self.transient(parent)
        self.grab_set()


        self.label = []
        ct = 0
        variancia = 1


        for vendedor in self.controle.bd_vendedores.lista_vendedores:

            texto = 'Nome Vendedor: ' + vendedor.nome + ' ; ' + 'CPF Vendedor: ' + vendedor.cpf + ' ; ' + 'Matrícula: ' + str(vendedor.matricula)

            label = Label(self, text=texto, font='Arial 11')
            self.label.append(label)
            self.label[ct].place(x=5, y=variancia*25)
            ct += 1
            variancia += 1.8
