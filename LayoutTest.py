# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 10:34:57 2020

@author: Benjamin Luo
"""

tile_rows = 5

#vertical

# for i in range(100):
#     print(i)
    
#horizontal
input_string = "abc"
tile = [" ---------","|{:9s}".format(input_string)," ---------","|         ","|         "]
empty_tile = ["          ","          ","          ","          ","          "]
tile_display = ["","","","",""]
middle_rows = ["","","","",""]
last_row = ""

# for i in range(170):
#     print("-",end="")
for i in range(17):
    for j in range(len(tile)):
        tile_display[j]+=tile[j]
        
for l in range(17):
    if l not in range(1,16):
        for j in range(len(tile)):
            middle_rows[j]+=tile[j]
    else:
        for k in range(len(empty_tile)):
            middle_rows[k]+=empty_tile[k]
        
print(len(tile_display[0]))

for i in (1,3,4):
    tile_display[i]+="|"
    middle_rows[i]+="|"
    
for i in (0,2):
    tile_display[i]+=" "
    middle_rows[i]+=" "

for i in range(17):
    last_row+=" ---------"
    
for b in range(5):
    if b in (0,4):
        for a in tile_display:
            print(a)
    else:
        for c in middle_rows:
            print(c)
print(last_row)
            
        
