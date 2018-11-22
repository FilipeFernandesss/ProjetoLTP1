#Classe controladora
from concessionaria import Concessionaria
from banco_de_dados import BD
from janela_principal import Janela_Principal

class Controle():
    def __init__(self):
        self.concessionaria = Concessionaria('concessionariaTESTE')
        self.bd = BD()
        self.janela_principal = Janela_Principal(self)
        self.janela_principal.mainloop()

    def excluir(self, placa):
        self.concessionaria.excluir_carro(placa)

    def inserir(self, marca, modelo, ano, estado, placa, preco):
        self.concessionaria.inserir_carro(marca, modelo, ano, estado, placa, preco)
