#!/usr/bin/env python3

import os,sys

# git init
# git add exercicio_1_1.py
# git commit -m "first commit"
# remote add origin https://github.com/talesCPV/Livro---Programa-o-em-Python3.git 
# git push -u origin master

if len(sys.argv) > 1:
 rep = sys.argv[1]
else:
	rep = 'python3'

os.system('git init')
for x in os.listdir('.'):
    if x.endswith(".py"):
        os.system('git add ' + x)      
os.system('git commit -m ' + rep)
os.system('remote add origin https://github.com/talesCPV/Livro---Programa-o-em-Python3.git')
os.system('git push -u origin master')

#os.system('ls')