#!/usr/bin/python3

from tkinter import *

palette = ['black','red','purple','green']

pos = [0,0]

class CHR:
    def __init__(self,raiz):
        self.canvas = Canvas(raiz, width=320, height=320, bg='white')
        self.canvas.pack() 

        ret=self.canvas.create_rectangle
        cor = 0

        for x in range(32):
            for y in range(32):
                ret(pos[0], pos[1], pos[0]+10, pos[1]+10, fill=palette[cor])
                pos[0] += 10
                cor += 1
                if cor == 4:
                    cor = 0

            pos[0] = 0
            pos[1] += 10


instancia=Tk()
CHR(instancia)
instancia.mainloop() 