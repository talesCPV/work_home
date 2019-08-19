#!/usr/bin/env python3

import os,sys


if len(sys.argv) < 2:
    print('Example: $ ./folder.py avi  ')
else:
    ext = '.'+ sys.argv[1]

    for x in os.listdir('.'):
        if x.endswith(ext):
            name = x.split('.')[0]
            print(name)
        
    #        os.system('mkdir ' + name)
            os.system('rm -r ' + name)
    #        os.system('cp {0} ./{1} '.format(x, name))

