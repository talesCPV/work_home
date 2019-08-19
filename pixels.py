#!/usr/bin/python3

from tkinter import *

class CHR:
    def __init__(self,raiz):
        self.canvas = Canvas(raiz, width=320, height=320, bg='dodgerblue')
        self.canvas.pack() 

        altura = 200 # Altura do canvas

        pol=self.canvas.create_polygon
        ret=self.canvas.create_rectangle
        ret(0, 0, 160, 20, fill='blue')


instancia=Tk()
CHR(instancia)
instancia.mainloop() 