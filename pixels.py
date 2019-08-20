#!/usr/bin/python3

from tkinter import *

palette = ['black','red','purple','green']
pixel_width = 5

class CHR:
    def __init__(self,raiz):
        self.canvas = Canvas(raiz, width=640, height=640, bg='white')
        self.canvas.pack()

    def draw_tile(self,tile, lin=0, col=0):
        pos = [0,0]
        pos[0] = col * 8
        pos[1] = lin * 8
        ret=self.canvas.create_rectangle
        for x in range(8):
            for y in range(8):
                ret(pos[0], pos[1], pos[0]+pixel_width, pos[1]+pixel_width, fill=palette[tile[x][y]])
                pos[0] += pixel_width

            pos[0] = 0
            pos[1] += pixel_width

    def convert(self,tile):
        col = []
        for x in range(8):
            row = []
            for y in range(8):
                a = int(tile[x][y])
                b = int(tile[x+8][y])
                if a:
                    if b:
                        cor = 3
                    else:
                        cor = 1
                else:
                    if b:
                        cor = 2
                    else:
                        cor = 0
                row.append(cor)
            col.append(row)
        return col



    def abrir(self):
        with open("data/2.chr", "rb") as f:
            for line in f:
                count = 0
                tile = []
                drop_row = 0
                drop_col = 0
                for x in line:
                    tile.append('{0:0>8} '.format(bin(x)[2:]))
                    count += 1
                    if count == 16:
                        my_tile = self.convert(tile)
                        print(my_tile)
#                        print(tile)
                        tile = []
                        count = 0
                        self.draw_tile(my_tile,(drop_row*pixel_width),(drop_col*pixel_width))
                        drop_col +=1
                        if drop_col > 15:
                            drop_col = 0

                            return



instancia=Tk()
teste = CHR(instancia)
teste.abrir()

instancia.mainloop()