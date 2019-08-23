#!/usr/bin/python3

from tkinter import *
from tkinter import filedialog

buffer = bytearray()
chr_file = ''
page = 0
palette_width = 30

colors = ("dim gray", "gray", "white smoke", "white", "medium blue", "DodgerBlue2", "DeepSkyBlue2", "LightSkyBlue2", "blue2",
        "DodgerBlue3", "light steel blue", "snow3", "MediumPurple4", "SlateBlue2", "MediumPurple1", "thistle",
        "maroon3", "maroon1", "PaleVioletRed1", "plum1", "red3", "deep pink", "PaleVioletRed2", "LightPink1", "red3",
        "orange red", "tomato", "light pink", "brown4", "dark orange", "tan1", "wheat1", "DarkOrange4", "orange3",
        "goldenrod1", "LightGoldenrod2", "SpringGreen4", "green3", "green yellow", "DarkOliveGreen1", "green4", "chartreuse3",
        "yellow green", "PaleGreen1", "dark green", "aquamarine4", "SeaGreen2", "DarkSeaGreen1", "DodgerBlue4",
        "DeepSkyBlue3", "turquoise", "cyan", "black", "gray5", "gray40", "gray90")


class CHR:
    def __init__(self,raiz):
        self.canvas = Canvas(raiz, width=640, height=640, bg='white')
        self.canvas.pack(side=LEFT)

    def draw_tile(self,tile, lin=0, col=0, pixel_width = 5, palette = ['black','red','purple','green']):
        pos = [col * 8,lin * 8]

        ret=self.canvas.create_rectangle
        for x in range(8):
            for y in range(8):
                ret(pos[0], pos[1], pos[0]+pixel_width, pos[1]+pixel_width, fill=palette[tile[x][y]])
                pos[0] += pixel_width

            pos[0] = col * 8
            pos[1] += pixel_width

    def grid(self,show=True,size=5,color='white'):
        if show:
            x = size * 8
            for i in range(16):
                self.canvas.create_line(x,0, x, size*128, fill=color, tag='linha')
                x += (size*8)
            y = size * 8
            for i in range(16):
                self.canvas.create_line(0,y, size*128, y, fill=color, tag='coluna')
                y += (size*8)

    def convert(self,tile):
        col = []
        for x in range(8):
            row = []
            for y in range(8):
                a = int(tile[x][y])
                b = int(tile[x + 8][y])
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

    def abrir(self,chr_file):
        buffer.clear()
        with open(chr_file, "rb") as f:
            for line in f:
                tile = []
                for x in line:
                    buffer.append(x)
                    tile.append('{0:0>8} '.format(bin(x)[2:]))
        self.load(buffer, grid=False)

    def load(self,buff, pixel_width = 5, grid=False):
        tile = []
        count = 0
        drop_row = 0
        drop_col = 0
        tile_count = 1
        for x in buff:
            tile.append('{0:0>8} '.format(bin(x)[2:]))
            count += 1
            if count == 16:
                my_tile = self.convert(tile)
                tile_count += 1
                tile = []
                count = 0
                self.draw_tile(my_tile, (drop_row * pixel_width), (drop_col * pixel_width))
                drop_col += 1
                if drop_col > 15:
                    drop_col = 0
                    drop_row += 1
        if grid:
            self.grid(color="yellow")


    def new(self):
        try:
            chr_mem = bytearray()
            chr_mem += b'\x00' * 16 # 1 tile
            new_chr = open("data/new.chr", "w+b")
            new_chr.write(chr_mem*271)
            new_chr.close()
            self.load(chr_mem*256)
        except IOError:
            print('erro!!!')

    def save(self,chr_file):
        print(chr_file)
        if chr_file:
            print('entrou')
            try:
                new_chr = open(chr_file, "w+b")
                new_chr.write(Nes.buffer)
                new_chr.close()
            except IOError:
                print('erro!!!!')

    def save_as(self):
        chr_file = filedialog.asksaveasfilename(title="Save your file", filetypes=(('CHR file', '*.chr'), ('all files', '*.*')))
        save(chr_file)




class Palette:
    def __init__(self, raiz):
        self.canvas = Canvas(raiz, width=430, height=120, bg='white')
        self.canvas.pack()

    def draw(self):
        col = 5
        width = palette_width # Largura e altura do quadrado da cor
        multiply = 0
        ret=self.canvas.create_rectangle
        for i in range(56):
            ret(col, multiply*width, col + width, (multiply+1)*width,  fill=colors[i])
            multiply += 1
            if multiply >3:
                multiply = 0
                col += width