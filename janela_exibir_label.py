#janela para exibição das informações dos carros
from tkinter import *



class Janela_Exibir_Label(Toplevel):
    def __init__(self, parent, controle):
        super().__init__(parent)

        self.controle = controle

        self.geometry('495x730+370+0')
        self.title('Exibir Informações')
        self.transient(parent)
        self.grab_set()

        self.texto = []
        ct = 0
        variancia = 1



        for carro in self.controle.bd.lista_carros:
            print(carro.get_modelo())
            texto ='Marca: ' + carro.marca + '\n' + 'Modelo: ' + carro.modelo + '\n' + 'Ano: ' + str(carro.ano) \
                   + '\n' + 'Estado: ' + carro.estado + '\n' + 'Placa: ' + carro.placa + '\n' + 'Preço: ' + str(carro.preco)
            print(texto)

            self.text = Text(self, height=6)

            self.text.insert(INSERT, texto)
            self.text.pack()
            self.texto.append(texto)
            ct += 1
