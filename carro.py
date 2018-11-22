#Classe referente aos carros

class Carro():
    #Método construtor
    def __init__(self, marca, modelo, ano, estado, placa, preco):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.estado = estado
        self.placa = placa
        self.preco = preco

    #Métodos GETS
    def get_marca(self):
        return self.marca

    def get_modelo(self):
        return self.modelo

    def get_ano(self):
        return self.ano

    def get_estado(self):
        return self.estado

    def get_placa(self):
        return self.placa

    def get_preco(self):
       return self.preco