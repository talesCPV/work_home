#!/usr/bin/env python3
	
arq = open("dates/iron_age.txt","w")

with open("dates/iron_age.chr","rb") as f:
    for line in f:
        #tratamento que quiser dar.
        arq.write(line)
        print(line)

arq.close()
