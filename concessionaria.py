#Classe que controla os comportamentos dos carros(excluir, inserir ...)
from banco_de_dados import BD
from carro import Carro
from banco_de_dados_vendedor import Vendedores
from banco_de_dados_compradores import BD_Compradores


class Concessionaria():
    def __init__(self, nome):
        self.nome = nome
        self.banco = BD()
        self.banco_vendedores = Vendedores()
        self.banco_compradores = BD_Compradores

    def get_nome(self):
        return self.nome

    #Método para inserir carros
    def inserir_carro(self, marca, modelo, ano, estado, placa, preco):
        carro = Carro(marca, modelo, ano, estado, placa, preco)
        self.banco.lista_carros.append(carro)
        self.banco.salvar_carros(self.banco.lista_carros)


    #Método para excluir um carro
    def excluir_carro(self, placa):
        ct = 0
        for i in self.banco.lista_carros:
            if placa in i.get_placa(): #Verifica se a placa pertence à algum carro na lista

                del self.banco.lista_carros[ct]  #Se sim deleta o carro e salva os outros.
                self.banco.salvar_carros(self.banco.lista_carros)

            ct += 1


