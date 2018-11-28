#Classe controladora
from concessionaria import Concessionaria
from banco_de_dados import BD
from tela_principal import Tela_Principal
from controle_vendedor import Controle_Vendedor
from banco_de_dados_vendedor import Vendedores
from banco_de_dados_compradores import BD_Compradores
from controle_compradores import Controle_Compradores

class Controle():
    def __init__(self):
        self.concessionaria = Concessionaria('concessionariaTESTE')
        self.bd = BD()
        self.controle_vendedor = Controle_Vendedor()
        self.bd_vendedores = Vendedores()
        self.controle_compradores = Controle_Compradores()
        self.bd_compradores = BD_Compradores()
        self.tela_principal = Tela_Principal(self)
        self.tela_principal.mainloop()

    def excluir(self, placa):
        self.concessionaria.excluir_carro(placa)

    def inserir(self, marca, modelo, ano, estado, placa, preco):
        self.concessionaria.inserir_carro(marca, modelo, ano, estado, placa, preco)

    def inserir_vendedor(self, nome, cpf, matricula):
        self.controle_vendedor.inserir_vendedor(nome, cpf, matricula)

    def excluir_vendedor(self, nome, matricula):
        self.controle_vendedor.excluir_vendedor(nome, matricula)

    def inserir_comprador(self, nome, cpf):
        self.controle_compradores.inserir_comprador(nome, cpf)
