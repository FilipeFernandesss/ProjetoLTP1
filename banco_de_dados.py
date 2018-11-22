#Classe para gravar e recuperar os carros
from carro import Carro

class BD():
    def __init__(self):
        self.lista_carros = self.carregar_carros()


    #Método para carregar os carros do arquivo txt
    def carregar_carros(self):
        carros = []
        arquivo = open('lista_carros.txt', 'r')


        for linha in arquivo:
            print(linha)
            lista = linha.strip('\n').split(',')
            carro = Carro(lista[0], lista[1], int(lista[2]), lista[3], lista[4], lista[5])
            carros.append(carro)

        arquivo.close()
        return carros

    #Método para salvar os carros no arquivo txt
    def salvar_carros(self, lista):


        arquivo = open('lista_carros.txt', 'w')

        for carro in lista:
            linha = carro.marca + ',' + carro.modelo + ',' + str(carro.ano) + ',' + carro.estado + ',' + carro.placa + ',' + str(carro.preco)
            arquivo.write(linha + '\n')

        arquivo.close()


    #Método para retornar a lista de carros
    def get_lista_carros(self):
        return self.lista_carros
