#!/usr/bin/env python3

tile = b'\x00'*2000

arr = bytearray(tile)

print(arr)



try:
    new_chr = open("data/test.chr", "w+b")
    new_chr.seek(0, 2)
    new_chr.write(tile)  # each tile has 8 lines with 2 bytes -> 16 tiles is the first line
    tamanho = new_chr.tell()
    print('tamanho:',tamanho)
    new_chr.seek(0)
    buffer = new_chr.read(tamanho)
#    for row in range(1):
#        new_chr.write(tile) #  each tile has 8 lines with 2 bytes -> 16 tiles is the first line

    new_chr.close()
except IOError:
    print('erro!!!')
