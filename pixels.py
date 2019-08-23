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
        try:
            chr_file = filedialog.askopenfilename(title="Choose you CHR file", filetypes=(('CHR file', '*.chr'), ('all files', '*.*')))
            screen.abrir(chr_file)
            root.title('Open NES CHR - ' + chr_file)
        except:
            print('Canceled by user!')
            
    def save_as():
        chr_file = filedialog.asksaveasfilename(title="Save your file", filetypes=(('CHR file', '*.chr'), ('all files', '*.*')))
        save()
        root.title('Open NES CHR - ' + chr_file)

    def save():
        print(chr_file)
        if chr_file:
            print('entrou')
            try:
                new_chr = open(chr_file, "w+b")
                new_chr.write(Nes.buffer)
                new_chr.close()
            except IOError:
                print('erro!!!!')

    sair = lambda: exit()
    nova = lambda: screen.new()
    root.config(menu=menubar)

    filemenu = Menu(menubar)

    menubar.add_cascade(label='File', menu=filemenu)
    filemenu.add_command(label='New', command=nova)
    filemenu.add_command(label='Open', command=abrir)
    filemenu.add_command(label='Save', command=save)
    filemenu.add_command(label='Save as...', command=save_as)
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=sair)






root=Tk()
root.title('Open NES CHR')
create_menu(root)
chr_file = ''

screen = Nes.CHR(root)
pal = Nes.Palette(root)

text = pal.canvas.create_text(50,130, text='teste')
#text.pack();


#teste.abrir('data/mario.chr')
pal.draw()

root.mainloop()