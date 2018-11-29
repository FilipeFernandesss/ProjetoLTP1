from nota_fiscal import Nota_Fiscal

class BD_Nota_Fiscal():
    def __init__(self):
        self.lista_nota_fiscal = self.carregar_nota()

    def carregar_nota(self):
        notas = []
        arquivo = open('lista_nota_fiscal.txt', 'r')

        for linha in arquivo:
            lista = linha.strip('\n').split(',')
            nota = Nota_Fiscal(lista[0], int(lista[1]), lista[2], lista[3], lista[4], lista[5], float(lista[6]), lista[7])
            notas.append(nota)

        arquivo.close()
        return notas

    def salvar_nota(self, lista):

        arquivo = open('lista_nota_fiscal.txt', 'w')

        for nota_fiscal in lista:
            linha = nota_fiscal.nome_vendodor + ',' + str(nota_fiscal.matricula_vendedor) + ',' + nota_fiscal.nome_comprador + ',' + nota_fiscal.cpf_comprador + ',' + nota_fiscal.modelo + ',' + nota_fiscal.placa + ',' + str(nota_fiscal.preco) + ',' + str(nota_fiscal.data)
            arquivo.write(linha + '\n')

        arquivo.close()