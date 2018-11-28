#Classe para armazenar os compradores no txt
from compradores import Compradores

class BD_Compradores():

    def __init__(self):
        self.lista_compradores = self.carregar_compradores()

    def carregar_compradores(self):
        compradores = []
        arquivo = open('lista_compradores.txt', 'r')

        for linha in arquivo:
            lista = linha.strip('\n').split(',')
            comprador = Compradores(lista[0], lista[1])
            compradores.append(comprador)

        arquivo.close()
        return compradores

    def salvar_compradores(self, lista):
        arquivo = open('lista_compradores.txt', 'w')

        for comprador in lista:
            linha = comprador.nome + ',' + comprador.cpf
            arquivo.write(linha + '\n')

        arquivo.close()

    def get_lista_compradores(self):
        return self.lista_compradores
