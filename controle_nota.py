from bd_nota_fiscal import BD_Nota_Fiscal
from nota_fiscal import Nota_Fiscal

class Controle_Nota():
    def __init__(self):
        self.bd_nota = BD_Nota_Fiscal()

    def inserir_comprador(self,nome_vendedor, matricula_vendedor, nome_comprador, cpf_comprador, modelo, placa, preco, data):
        nota = Nota_Fiscal(nome_vendedor, matricula_vendedor, nome_comprador, cpf_comprador, modelo, placa, preco, data)
        self.bd_nota.lista_nota_fiscal.append(nota)
        self.bd_nota.salvar_nota(self.bd_nota.lista_nota_fiscal)
