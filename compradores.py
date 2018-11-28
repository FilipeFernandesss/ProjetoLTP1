#Classe para criar os compradores

class Compradores():

    def __init__(self, nome, cpf):

        self.nome = nome
        self.cpf = cpf

    def get_nome(self):
        return self.nome

    def get_cpf(self):
        return self.cpf
