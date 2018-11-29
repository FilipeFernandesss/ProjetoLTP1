#Classe para controlar as informações dos vendedores
from banco_de_dados_vendedor import Vendedores
from vendedor import Vendedor


class Controle_Vendedor():
    def __init__(self):
        self.banco_vendedores = Vendedores()

    def inserir_vendedor(self, nome, cpf, matricula):
        novo_vendedor = Vendedor(nome, cpf, matricula)
        self.banco_vendedores.lista_vendedores.append(novo_vendedor)
        self.banco_vendedores.salvar_vendedores(self.banco_vendedores.lista_vendedores)

    def excluir_vendedor(self, nome, matricula):
        ct = 0
        for vendedor in self.banco_vendedores.lista_vendedores:
            if nome == vendedor.get_nome():
                if int(matricula) == vendedor.get_matricula():
                    del self.banco_vendedores.lista_vendedores[ct]
                    self.banco_vendedores.salvar_vendedores(self.banco_vendedores.lista_vendedores)
            ct += 1
