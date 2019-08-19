#!/usr/bin/python3

from tkinter import *


class Form:
    def __init__(self):
        main_window = Tk()
        main_window.geometry("600x300")
  
        main_window.mainloop()

class Botao:
    def __init__(self,toplevel):
        self.fr1 = Frame(toplevel)
        self.fr1.pack()
        self.botao = Button(self.fr1, text='Oi!', bg='red')
        self.botao.pack() 

#form = Form()

raiz=Tk()
Botao(raiz)
raiz.mainloop()
