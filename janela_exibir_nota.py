from tkinter import *


class Janela_Exibir_Nota(Toplevel):
    def __init__(self, parent, controle):
        super().__init__(parent)

        self.controle = controle

        self.geometry('1360x768+0+0')
        self.title('Exibir Notas Fiscais')
        self.transient(parent)
        self.grab_set()


        self.label = []
        ct = 0
        variancia = 1

        for nota_fiscal in self.controle.bd_nota.lista_nota_fiscal:

            texto ='Nome Vendedor: ' + nota_fiscal.nome_vendodor + ' ; ' + 'Matrícula Vendedor: ' + str(nota_fiscal.matricula_vendedor) + \
                   ' ; ' + 'Nome Comprador: ' + nota_fiscal.nome_comprador + ' ; ' + 'CPF Comprador: ' + nota_fiscal.cpf_comprador + ' ; ' + 'Modelo Carro: ' + nota_fiscal.modelo + ' ; ' + 'Placa Carro: ' + nota_fiscal.placa + ' ; ' + 'Preço Carro: ' + str(nota_fiscal.preco) + ' ; ' + 'Data: ' + str(nota_fiscal.data)


            label = Label(self, text=texto, font='Arial 11')
            self.label.append(label)
            self.label[ct].place(x=5, y=variancia*25)
            ct += 1
            variancia += 1.8
