#!/usr/bin/env python3

import sys
# Criando um objeto do tipo file
temp = open('temp.txt','w')

# Escrevendo no arquivo
for i in range(100):
    temp.write('%03d\n'%i)

# Fechando
temp.close()
temp=open('temp.txt')

# Escrevendo no terminal
for x in temp:
    sys.stdout.write(x)
    
#Escrever em sys.stdout envia o texto para a saída padrão

temp.close()