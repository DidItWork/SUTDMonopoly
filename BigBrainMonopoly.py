# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 17:54:30 2020

@author: Benjamin Luo
"""

import math
import random
import matplotlib



#Initialise parameters, building values is a list of lists
#-------------------------------------------------------------------------#

# tiles - list of tile objects making up the board
# building_pos - position of the buildings on the respective tiles
# building_names - list of building names (strings)
# building_colours - list of respective building colours
# building_values - list of lists of the three building values of each respective building
# chance_pos - position of chance tiles
# jail_pos - position of jail tiles
# tax_pos - position of tax tiles
# players - list of player objects
# board - game board layout
# bankruptcy - how many people are bankrupted

num_of_tiles = 40
num_players = 5
tiles = []
building_pos = []
building_names = []
building_colours = []
building_values = []
chance_pos = []
jail_pos = []
tax_pos = []
players = []
board = []
bankruptcy = 0



#Defining classes of objects
#-------------------------------------------------------------------------#

class player():
    
    #for functions on setting variables and getting variable values, use getters and setters
    
    def __init__(self,name):
        self.name = ""
        self.status = "normal" #normal, bankrupt, jailed
    
    def get_status(self):
        return self.status
    
    def update_status(self,status):
        self.status = status
        

class building():
    
    def __init__(self, colour, title, level, values):
        
        #values is a dictionary with the key being the building name and its value
        #being a list of three numbers with each number indicating its value at the
        #respective level
        
        self.colour = colour
        self.title = title
        self.level = level
        self.values = values

class tile():
    def __init__(self,id_no,tile_type,building):
        self.id = id_no
        self.tile_type = tile_type
        if self.tile_type == "building":
            self.building = building


#Initialising variables
#-------------------------------------------------------------------------#

for i in range(num_of_tiles):
    if i==0:
        tiles.append(tile(i,"home",""))
    elif i in building_pos:
        tiles.append(tile(i,"building",building(building_colours[i],building_names[i],0,building_values[i])))
    elif i in chance_pos:
        tiles.append(tile(i,"chance",""))
    elif i in jail_pos:
        tiles.append(tile(i,"jail",""))
    elif i in tax_pos:
        tiles.append(tile(i,"tax",""))
        
for i in range(num_players):
    players.append(player(""))


#game functions
#-------------------------------------------------------------------------#

def roll():
    
    #return a tuple of two integers (1-6) from dice rolls
    
    pass
    
def update_board(board):
    
    #return an updated board from the old board
    
    pass


def display_board(board):
    
    #display board
    
    pass


def gameround(player_id, board):
    
    #Player with player_id plays this round
    roll()
    new_board = update_board(board)
    display_board(new_board)
    
    
    return board
    pass
    

def game(num_players, bankruptcy, board):
    
    #Run the game rounds repeatedly until someone wins, if the player is bankrupt, skip the player
    while bankruptcy<num_players-1:
        counter = 0
        if player[counter].get_status() == "normal":
            board = gameround(counter, board)
        
        
        #Cycling between players
        
        counter += 1
        counter = counter%num_players
    
    pass
    
#Run the game

#game(num_players, bankruptcy, board)
    