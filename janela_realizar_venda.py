from tkinter import *
from tkinter import messagebox
from janela_venda_compradores import Venda_Compradores
from datetime import date


class Janela_Venda(Toplevel):

    def __init__(self, parent, controle):
        super().__init__(parent)

        self.controle = controle

        self.geometry('300x350+200+200')
        self.title('Realizar venda')
        self.transient(parent)
        self.grab_set()

        self.et_nome_vendedor = Entry(self)
        self.lb_nome_vendedor = Label(self, text='Nome Vendedor:')

        self.et_nome_vendedor.place(x=130, y= 10)
        self.lb_nome_vendedor.place(x=10, y=10)

        self.et_matricula = Entry(self, width=15)
        self.lb_matricula = Label(self, text='Matrícula Vendedor:')

        self.et_matricula.place(x=130, y=35)
        self.lb_matricula.place(x=10, y=35)

        self.et_nome = Entry(self)
        self.lb_nome = Label(self, text='Nome Cliente:')

        self.et_nome.place(x=100, y=80)
        self.lb_nome.place(x=10, y=80)

        self.et_cpf = Entry(self)
        self.lb_cpf = Label(self, text='CPF Cliente:')

        self.et_cpf.place(x=100, y=110)
        self.lb_cpf.place(x=10, y=110)

        self.et_modelo = Entry(self)
        self.lb_modelo = Label(self, text='Modelo:')

        self.et_modelo.place(x=100, y=160)
        self.lb_modelo.place(x=10, y=160)

        self.et_placa = Entry(self)
        self.lbl_placa = Label(self, text='Placa:')

        self.et_placa.place(x=100, y=190)
        self.lbl_placa.place(x=10, y=190)

        self.et_preco = Entry(self)
        self.lbl_preco = Label(self, text='Preço:')

        self.et_preco.place(x=100, y=220)
        self.lbl_preco.place(x=10, y=220)

        self.button = Button(self, width=10, text='OK', command=self.btn_click)
        self.button.place(x=100, y=275)


    def btn_click(self):
        data_atual = date.today()
        if len(self.et_nome_vendedor.get()) == 0 or len(self.et_matricula.get()) == 0:
            messagebox.showinfo(title='Erro', message='Campo em branco')

        else:
            for vendedor in self.controle.bd_vendedores.lista_vendedores:

                if int(self.et_matricula.get()) == vendedor.get_matricula():
                    if len(self.et_nome.get()) == 0 or len(self.et_cpf.get()) == 0:
                        messagebox.showinfo(title='Erro', message='Campo em branco')
                    else:
                        if messagebox.askokcancel(title='Venda', message='Deseja realmente vender esse veículo?'):
                            for carro in self.controle.bd.lista_carros:
                                if self.et_placa.get() in carro.get_placa():
                                    self.controle.inserir_comprador(self.et_nome.get(), self.et_cpf.get())

                                    self.controle.inserir_nota(self.et_nome_vendedor.get(), int(self.et_matricula.get()), self.et_nome.get(),
                                                               self.et_cpf.get(), self.et_modelo.get(), self.et_placa.get(), float(self.et_preco.get()), data_atual)
                                    self.controle.excluir(self.et_placa.get())
                                    self.destroy()
                                else:
                                    messagebox.showinfo(message='Placa não encontrado')

