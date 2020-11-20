# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 18:11:39 2020

@author: ngwei
"""

import tkinter
#--------alter the values below to produce desired board-------#
boxLength = 70 
boxHeight = 100

boardLength = 10
boardHeight = 10

def generateVertices(x, y, ht, wdth):
    ls = []
    ls.append(x) #x1
    ls.append(y) #y1
    ls.append(x + wdth) #x2
    ls.append(y) #y2
    ls.append(x + wdth) #x3
    ls.append(y + ht) #y3
    ls.append(x) #x4
    ls.append(y + ht) #y4
    return ls


top = tkinter.Tk()
widg = tkinter.Canvas(top, bg = "green", height = boardHeight*boxHeight, width = boardLength*boxHeight, relief = "groove")


verticeSets= []
for i in range(boardLength):
    for r in range(boardHeight):
        if not (i in range(1, boardLength-1) and (r in range(1, boardHeight - 1))):
            relXPos = boxHeight + (i-1)*boxLength 
            relYPos = boxHeight + (r-1)*boxLength
            if not (i in range(1, boardLength-1) or (r in range(1, boardHeight-1))):
                relXPos = boxLength*(i)+(int(not i == 0))*(boxHeight)-(int(not i==0))*(boxLength)
                relYPos = boxLength*(r)+(int(not r == 0))*(boxHeight)-(int(not r==0))*(boxLength)
                verticeSets.append(generateVertices(relXPos, relYPos, boxHeight, boxHeight))
            elif (i == 0 and r in range(1, boardHeight-1)):
                relXPos = 0
                verticeSets.append(generateVertices(relXPos, relYPos, boxLength, boxHeight))
            elif (not i in range(1, boardLength-1) and r in range(1, boardHeight-1)):
                verticeSets.append(generateVertices(relXPos, relYPos, boxLength, boxHeight))
            elif(r == 0 and i in range(1, boardLength-1)):
                relYPos = 0
                verticeSets.append(generateVertices(relXPos, relYPos, boxHeight, boxLength))
            else:
                verticeSets.append(generateVertices(relXPos, relYPos, boxHeight, boxLength))

# coords =  120 , 60, 120, 0, 60, 0, 60, 60 
# coords2 =  120+60 , 60, 120+60, 0, 60+60, 0, 60+60, 60 
for i in verticeSets:
    widg.create_polygon(i , fill="red", outline="black")

widg.pack()
top.mainloop()
