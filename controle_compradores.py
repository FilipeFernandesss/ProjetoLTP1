#Classe para controle dos compradores
from banco_de_dados_compradores import BD_Compradores
from compradores import Compradores

class Controle_Compradores():
    def __init__(self):
        self.bd_compradores = BD_Compradores()

    #Método para inserir um novo comprador
    def inserir_comprador(self, nome, cpf):
        comprador = Compradores(nome, cpf)
        self.bd_compradores.lista_compradores.append(comprador)
        self.bd_compradores.salvar_compradores(self.bd_compradores.lista_compradores)
