#Janela para excluir um vendedor
from tkinter import *
from tkinter import messagebox

class Janela_Exluir_Vendeder(Toplevel):
    def __init__(self, parent, controle):
        super().__init__(parent)

        self.controle = controle

        self.geometry('215x320+200+200')
        self.title('Exluir Vendedor')
        self.transient(parent)
        self.grab_set()

        self.et_nome = Entry(self)
        self.lb_nome = Label(self, text='Nome:')

        self.et_nome.place(x=10, y=35)
        self.lb_nome.place(x=10, y=10)

        self.et_matricula = Entry(self)
        self.lb_matricula = Label(self, text='Matricula:')

        self.et_matricula.place(x=10, y=110)
        self.lb_matricula.place(x=10, y=85)

        self.button = Button(self, width=10, text='Excluir', command=self.btn_on_click)
        self.button.place(x=60, y=250)

    def btn_on_click(self):
        if len(self.et_nome.get()) == 0 or len(self.et_matricula.get()) == 0:
            messagebox.showinfo(message='Campo em branco!')

        else:
            for vendedor in self.controle.bd_vendedores.lista_vendedores:

                if self.et_nome.get() in vendedor.get_nome():
                    if int(self.et_matricula.get()) == vendedor.get_matricula():
                        if messagebox.askokcancel(title='Excluir', message='Deseja realmente excluir o veiculo?'):
                            self.controle.excluir_vendedor(self.et_nome.get(), self.et_matricula.get())
                            break

            else:
                messagebox.showinfo(message='Erro')

        return self.destroy()
