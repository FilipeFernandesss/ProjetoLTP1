#Classe para representar a nota fiscal


class Nota_Fiscal():

    def __init__(self, nome_vendedor, matricula_vendedor, nome_comprador, cpf_comprador, modelo, placa, preco, data):

        self. nome_vendodor = nome_vendedor
        self.matricula_vendedor = matricula_vendedor
        self.nome_comprador = nome_comprador
        self.cpf_comprador = cpf_comprador
        self.modelo = modelo
        self.placa = placa
        self.preco = preco
        self.data = data

    def get_nome_vendedor(self):
        return self.nome_comprador

    def get_matricula_vendedor(self):
        return self.matricula_vendedor

    def get_nome_comprador(self):
        return self.nome_comprador

    def get_cpf_comprador(self):
        return self.cpf_comprador

    def get_modelo(self):
        return self.modelo

    def get_placa(self):
        return self.placa

    def get_preco(self):
        return self.preco

    def get_data(self):
        return self.data