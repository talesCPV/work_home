#!/usr/bin/python3

from tkinter import *

palette = ['black','red','purple','green']


class CHR:
    def __init__(self,raiz):
        self.canvas = Canvas(raiz, width=320, height=320, bg='white')
        self.canvas.pack() 

        altura = 200 # Altura do canvas

        pol=self.canvas.create_polygon
        ret=self.canvas.create_rectangle
        ret(0, 0, 10, 10, fill=palette[3])


instancia=Tk()
CHR(instancia)
instancia.mainloop() 