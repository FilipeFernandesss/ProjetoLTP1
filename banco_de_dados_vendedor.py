#Classe para armazenar os vendedores
from vendedor import Vendedor

class Vendedores():
    def __init__(self):
        self.lista_vendedores = self.carregar_vendedores()

    def carregar_vendedores(self):
        vendedores = []
        arquivo = open('lista_vendedores.txt', 'r')

        for linha in arquivo:
            lista = linha.strip('\n').split(',')
            vendedor = Vendedor(lista[0], lista[1], int(lista[2]))
            vendedores.append(vendedor)

        arquivo.close()
        return vendedores

    def salvar_vendedores(self, lista):

        arquivo = open('lista_vendedores.txt', 'w')

        for vendedor in lista:
            linha = vendedor.nome + ',' + vendedor.cpf + ',' + str(vendedor.matricula)
            arquivo.write(linha + '\n')

        arquivo.close()

    def get_lista(self):
        return self.lista_vendedores
