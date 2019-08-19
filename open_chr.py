#!/usr/bin/env python3

with open("data/2.chr","rb") as f:
    for line in f:
        count = 0
        row = ''
        for x in line:
            row += str(x) + ' '
            count += 1
            if count == 16:
                print(row)
                row = ''
                count = 0