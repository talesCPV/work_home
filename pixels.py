#!/usr/bin/python3

from tkinter import *
from tkinter import filedialog
import neschr as Nes

def res():
    resp = False
    x = filedialog.askopenfilename(title="Choose you CHR file", filetypes=(('CHR file','*.chr'),('all files', '*.*')))
    if x:
        resp = x

    return resp

def create_menu(root):
    menubar = Menu(root)
    def abrir():
        arq = filedialog.askopenfilename(title="Choose you CHR file", filetypes=(('CHR file', '*.chr'), ('all files', '*.*')))
        teste.abrir(arq)

    salvar = lambda: filedialog.asksaveasfilename(title="Save your file", filetypes=(('CHR file', '*.chr'), ('all files', '*.*')))
    sair = lambda: exit()
    nova = lambda: teste.new()
    root.config(menu=menubar)

    filemenu = Menu(menubar)

    menubar.add_cascade(label='File', menu=filemenu)
    filemenu.add_command(label='New', command=nova)  # command=function
    filemenu.add_command(label='Open', command=abrir)  # command=function
    filemenu.add_command(label='Save')  # command=function
    filemenu.add_command(label='Save as...', command=salvar)  # command=function
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=sair)  # command=function






root=Tk()
root.title('Open NES CHR')

create_menu(root)

teste = Nes.CHR(root)
pal = Nes.Palette(root)

#text = Text(pal)
#text.pack();
#text.insert('insert', 'Ao clicar no botão ')

teste.abrir('data/mario.chr')
pal.draw()

root.mainloop()