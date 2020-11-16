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

# change this into an input later
num_players = 5

# Do we need to create these empty lists? Purpose?
tiles = []
building_pos = []
building_names = []
building_cost = []
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
    
    # for functions on setting variables and getting variable values, use getters and setter
    id_no = 0
    
    def __init__(self):
        self.id = id_no
        self.status = "normal"
        self.position = 0
        
        id_no += 1
        
    
    def get_status(self):
        return self.status
    
    def update_status(self,status):
        #normal, bankrupt, jailed
        self.status = status
    
    def get_position(self):
        return self.position
    
    def update_position(self, position):
        self.position = position
    
        
class building():
    
    # Don't need colour cause can't present colours anyways
    def __init__(self, title, level, cost, values):
        
        # I don't think values should be a dictionary, should just be a list of 3 values and use "level", 0, 1, 2
        # To get the value. Else values can just be a global dictionary already
        
        # values is a dictionary with the key being the building name and its value
        # being a list of three numbers with each number indicating its value at the
        # respective level
        
        self.title = title
        self.level = level
        self.cost = cost
        self.values = values
        
class tile():
    
    id_no = 0
    
    def __init__(self, tile_type, building):
        self.id = id_no
        id_no += 1
        
        self.tile_type = tile_type
        
        if self.tile_type == "building":
            self.building = building


#Initialising variables
#-------------------------------------------------------------------------#

# Why we have the whole tiles.append() thing for ah lol

for i in range(num_of_tiles):
    if i == 0:
        tiles.append(tile("home",""))
    elif i in building_pos:
        tiles.append(tile("building", building(building_names[i], 0, building_cost[i], building_values[i])))
    elif i in chance_pos:
        tiles.append(tile("chance",""))
    elif i in jail_pos:
        tiles.append(tile("jail",""))
    elif i in tax_pos:
        tiles.append(tile("tax",""))
        
for i in range(num_players):
    
    # Do you want to add like input for player name?
    # Is players like a list?
    
    players.append(player())

for i in range(num_players):
    name = input(f"Enter Player{i}'s name")
    name = player()

#game functions
#-------------------------------------------------------------------------#

def roll():
    
    #return a tuple of two integers (1-6) from dice rolls
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    
    return dice1, dice2

def update_board(board):
    
    #return an updated board from the old board
    
    pass


def display_board(board):
    
    # probably use some print function to do so
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
    
