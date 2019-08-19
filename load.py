#!/usr/bin/env python3

arq_op = open('dates/CLIENTE.txt', encoding='utf8')
arq_sv = open('dates/saida.txt','w', encoding='utf8')

print('{0:^80}{1:^30}{2:^20}'.format('CLIENTE','RUA','CIDADE'))
print('-'*130)

for x in arq_op:
    line = x.split('|')
    if len(line)> 2:
        print('{0:<80} {1:<30} {2:<20}'.format(line[3],line[6],line[7]))



