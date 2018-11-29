#Janela para inserir vendedores
from tkinter import *
from tkinter import messagebox

class Janela_Inserir_Vendedor(Toplevel):
    def __init__(self, parent, controle):
        super().__init__(parent)

        self.controle = controle

        self.geometry('215x320+200+200')
        self.title('Inserir Vendedor')
        self.transient(parent)
        self.grab_set()

        self.et_nome = Entry(self)
        self.lb_nome = Label(self, text='Nome:')

        self.et_nome.place(x=10, y=35)
        self.lb_nome.place(x=10, y=10)


        self.et_cpf = Entry(self)
        self.lb_cpf = Label(self, text='CPF:')

        self.et_cpf.place(x=10, y=110)
        self.lb_cpf.place(x=10, y=85)

        self.et_matricula = Entry(self)
        self.lb_matricula = Label(self, text='Matrícula:')

        self.et_matricula.place(x=10, y=185)
        self.lb_matricula.place(x=10, y=160)

        self.button = Button(self, width=10, text='Inserir', command=self.btn_on_click)
        self.button.place(x=60, y=250)

    def btn_on_click(self):
        if len(self.et_nome.get()) == 0 or len(self.et_cpf.get()) == 0 or len(self.et_matricula.get()) == 0:
            messagebox.showerror(message='CAMPO EM BRANCO')

        elif len(self.et_matricula.get()) != 5:
            messagebox.showinfo(title='Erro', message='Matrícula Inválida')

        elif str(self.et_matricula.get()).isnumeric():
            self.controle.inserir_vendedor(self.et_nome.get(), self.et_cpf.get(), int(self.et_matricula.get()))
            self.destroy()

        else:
            messagebox.showerror(message='Informação incorreta!')

