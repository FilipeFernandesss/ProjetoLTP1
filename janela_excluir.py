from tkinter import *

class Janela_Excluir(Toplevel):
    def __init__(self, parent, controle):
        super().__init__(parent)

        self.controle = controle #Setando a classe de controle

        #Atributos da janela 'TopLevel'
        self.geometry('250x250+250+250')
        self.title('Exluir')
        self.transient(parent)
        self.grab_set()


        #Widgets e places
        self.ed = Entry(self)
        self.ed.place(x=50, y=100)

        self.lb = Label(self,text='Placa do carro que será excluido:')
        self.lb.place(x=45,y=75)

        self.btn = Button(self, width= 10, text='OK', command=self.btn_on_click)
        self.btn.place(x=50,y=135)

    #Método que será acionado ao clicar em OK.
    def btn_on_click(self):
        self.controle.excluir(self.ed.get()) #Chama a função excluir do controle e passa o get do entry(a placa) como parâmetro.
        return self.ed.get(), self.destroy()
