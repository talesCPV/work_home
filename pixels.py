#!/usr/bin/python3

from tkinter import *

palette = ['black','red','purple','green']
pixel_width = 5

class CHR:
    def __init__(self,raiz):
        self.canvas = Canvas(raiz, width=640, height=640, bg='white')
        self.canvas.pack(side=LEFT)

    def draw_tile(self,tile, lin=0, col=0):
        pos = [0,0]
        pos[0] = col * 8
        pos[1] = lin * 8
        ret=self.canvas.create_rectangle
        for x in range(8):
            for y in range(8):
                ret(pos[0], pos[1], pos[0]+pixel_width, pos[1]+pixel_width, fill=palette[tile[x][y]])
                pos[0] += pixel_width

            pos[0] = col * 8
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
        with open("data/mario.chr", "rb") as f:
            for line in f:
                count = 0
                tile = []
                drop_row = 0
                drop_col = 0
                tile_count = 1
                for x in line:
                    tile.append('{0:0>8} '.format(bin(x)[2:]))
                    count += 1
                    if count == 16:
                        my_tile = self.convert(tile)
                        print(my_tile)
                        tile_count += 1
                        tile = []
                        count = 0
                        self.draw_tile(my_tile,(drop_row*pixel_width),(drop_col*pixel_width))
                        drop_col +=1
                        if drop_col > 16:
                            drop_col = 0
                            drop_row += 1


                        if tile_count > 50:
                            return


class Palette:
    def __init__(self, raiz):
        self.canvas = Canvas(raiz, width=430, height=200, bg='white')
        self.canvas.pack()

    def draw(self):
        col = 0
        width = 30
        ret=self.canvas.create_rectangle
        #Col 01
        ret(col,0, col+width,width, fill="dim gray")
        ret(col,width, col+width,width*2, fill="gray")
        ret(col,width*2, col+width,width*3, fill="white smoke")
        ret(col,width*3, col+width,width*4, fill="white")
        col += width
        #Col 02
        ret(col,0, col+width,width, fill="medium blue")
        ret(col,width, col+width,width*2, fill="DodgerBlue2")
        ret(col,width*2, col+width,width*3, fill="DeepSkyBlue2")
        ret(col,width*3, col+width,width*4, fill="LightSkyBlue2")
        col += width
        #Col 03
        ret(col,0, col+width,width, fill="blue2")
        ret(col,width, col+width,width*2, fill="DodgerBlue3")
        ret(col,width*2, col+width,width*3, fill="light steel blue")
        ret(col,width*3, col+width,width*4, fill="snow3")
        col += width
        #Col 04
        ret(col,0, col+width,width, fill="MediumPurple4")
        ret(col,width, col+width,width*2, fill="SlateBlue2")
        ret(col,width*2, col+width,width*3, fill="MediumPurple1")
        ret(col,width*3, col+width,width*4, fill="thistle")
        col += width
        #Col 05
        ret(col,0, col+width,width, fill="maroon3")
        ret(col,width, col+width,width*2, fill="maroon1")
        ret(col,width*2, col+width,width*3, fill="PaleVioletRed1")
        ret(col,width*3, col+width,width*4, fill="plum1")
        col += width
        #Col 06
        ret(col,0, col+width,width, fill="red3")
        ret(col,width, col+width,width*2, fill="deep pink")
        ret(col,width*2, col+width,width*3, fill="PaleVioletRed2")
        ret(col,width*3, col+width,width*4, fill="LightPink1")
        col += width
        #Col 07
        ret(col,0, col+width,width, fill="red3")
        ret(col,width, col+width,width*2, fill="orange red")
        ret(col,width*2, col+width,width*3, fill="tomato")
        ret(col,width*3, col+width,width*4, fill="light pink")
        col += width
        #Col 08
        ret(col,0, col+width,width, fill="brown4")
        ret(col,width, col+width,width*2, fill="dark orange")
        ret(col,width*2, col+width,width*3, fill="tan1")
        ret(col,width*3, col+width,width*4, fill="wheat1")
        col += width
        #Col 09
        ret(col,0, col+width,width, fill="DarkOrange4")
        ret(col,width, col+width,width*2, fill="orange3")
        ret(col,width*2, col+width,width*3, fill="goldenrod1")
        ret(col,width*3, col+width,width*4, fill="LightGoldenrod2")
        col += width
        #Col 10
        ret(col,0, col+width,width, fill="SpringGreen4")
        ret(col,width, col+width,width*2, fill="green3")
        ret(col,width*2, col+width,width*3, fill="green yellow")
        ret(col,width*3, col+width,width*4, fill="DarkOliveGreen1")
        col += width
        #Col 11
        ret(col,0, col+width,width, fill="green4")
        ret(col,width, col+width,width*2, fill="chartreuse3")
        ret(col,width*2, col+width,width*3, fill="yellow green")
        ret(col,width*3, col+width,width*4, fill="PaleGreen1")
        col += width
        #Col 12
        ret(col,0, col+width,width, fill="dark green")
        ret(col,width, col+width,width*2, fill="aquamarine4")
        ret(col,width*2, col+width,width*3, fill="SeaGreen2")
        ret(col,width*3, col+width,width*4, fill="DarkSeaGreen1")
        col += width
        #Col 13
        ret(col,0, col+width,width, fill="DodgerBlue4")
        ret(col,width, col+width,width*2, fill="DeepSkyBlue3")
        ret(col,width*2, col+width,width*3, fill="turquoise")
        ret(col,width*3, col+width,width*4, fill="cyan")
        col += width
        #Col 14
        ret(col,0, col+width,width, fill="black")
        ret(col,width, col+width,width*2, fill="gray5")
        ret(col,width*2, col+width,width*3, fill="gray40")
        ret(col,width*3, col+width,width*4, fill="gray90")
        col += width



instancia=Tk()
teste = CHR(instancia)
pal = Palette(instancia)
teste.abrir()
pal.draw()

instancia.mainloop()