# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 17:54:30 2020

@author: Benjamin Luo
"""

import math
import random



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

num_of_tiles = 4

# change this into an input later
num_players = 0

# Do we need to create these empty lists? Purpose?
tiles = []
building_pos = list(range(4))
building_names = ["a","b","c","d"]
building_cost = [[1,2,3],[1,2,3],[1,2,3],[1,2,3]]
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
    
    def __init__(self, name):
        self.id = self.id_no
        self.status = "normal"
        self.position = 0
        self.name = name
        self.sanity = 500 

        
        self.id_no += 1
      
    
    def get_status(self):
        return self.status
    
    def update_status(self,status):
        #normal, bankrupt, jailed
        self.status = status
    
    def get_position(self):
        return self.position
    
    def update_position(self, position):
        self.position += position
        self.position = self.position%num_of_tiles
    
    def get_name(self):
        return self.name
    
    
    def get_sanity(self):
        return self.sanity
    
    def update_sanity(self,sanity):
        self.sanity += sanity
    
        
class building():
    
    # Don't need colour cause can't present colours anyways
    def __init__(self, name, cost):
        
        # I don't think values should be a dictionary, should just be a list of 3 values and use "level", 0, 1, 2
        # To get the value. Else values can just be a global dictionary already
        
        # values is a dictionary with the key being the building name and its value
        # being a list of three numbers with each number indicating its value at the
        # respective level
        
        self.level = 0
        self.owner = None
        self.cost = cost #list of three integers indicating the costs of the building
        self.name = name
        
    
    def get_rent(self):
        
        # rent of building calculated from cost and level 
    
        return self.cost[self.level]*1.5

    def set_level(self,level):
        
        self.level = level
    
    def set_ownership(self,player_id):
        
        self.owner = player_id

    def get_name(self):
        
        return self.name
    
    def get_cost(self):
        
        return self.cost[self.level]
    
    def get_owner(self):
        return self.owner
        
        
class tile():
    
    id_no = 0
    
    def __init__(self, tile_type, building):
        self.id = self.id_no
        self.id_no += 1
        
        self.tile_type = tile_type
        
        if self.tile_type == "building":
            print("ok")
            self.building = building
    
    def get_type(self):
        return self.tile_type
    
    def get_building(self):
        return self.building
    
#game functions
#-------------------------------------------------------------------------#

def roll(strength):
    
    #return a tuple of two integers (1-6) from dice rolls
    #implement strength of roll
    
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    
    return dice1, dice2

def update_board(board):
    
    #return an updated board from the old board
    
    print("Printing board")
    
    pass


def display_board(board):
    
    # probably use some print function to do so
    #display board
    
    print("Display board")
    
    pass


def gameround(player_id, board):
    dice1 = None
    dice2 = None
    step = 0
    
    #Player with player_id plays this round
    print("It's %s 's turn." % (players[player_id].get_name()))

        
        
    while True:
        buy = "z"
        strength = 0
        while strength < 1 or strength >5:
            strength = int(input("Roll Strength (1-5): "))
        dice1, dice2 = roll(strength)
        print(dice1,dice2)
        step = dice1+dice2
        players[player_id].update_position(step)
        player_pos = players[player_id].get_position()
        print(players[player_id].get_position())
        
        if tiles[player_pos].get_type()=="building" and tiles[player_pos].get_building().get_owner()==None:
            while buy[0] not in "yYnN":
                
                buy = input(("Do you want to buy %s [y/n]? " % (tiles[player_pos].get_building().get_name())))
                
                if buy[0] in "yY" and players[player_id].get_sanity()>=tiles[player_pos].get_building().get_cost():
                    tiles[player_pos].get_building().set_ownership(player_id)
                    players[player_id].update_sanity(-tiles[player_pos].get_building().get_cost())
                
        print(tiles[player_pos].get_building().get_owner())
        new_board = update_board(board)
        display_board(new_board)
    wait = input("Waiting...")
    
    return board
    pass
    

def game(num_players, bankruptcy, board):
    
    #game initialisation
    while num_players < 2 or num_players > 5:
        num_players = int(input("Number of players (2-5): "))
        
    for i in range(1, num_players+1):
        name = input(f"Enter Player {i}'s name: ")
        players.append(name, player())
    
    #Initialising variables
    #-------------------------------------------------------------------------#
    
    # Why we have the whole tiles.append() thing for ah lol
    
    for i in range(num_of_tiles):
        if i == 5000:
            tiles.append(tile("home",""))
        elif i in building_pos:
            tiles.append(tile("building", building(building_names[i], building_cost[i])))
        elif i in chance_pos:
            tiles.append(tile("chance",""))
        elif i in jail_pos:
            tiles.append(tile("jail",""))
        elif i in tax_pos:
            tiles.append(tile("tax",""))
    print(tiles)
        
    counter = 0
    #Run the game rounds repeatedly until someone wins, if the player is bankrupt, skip the player
    while bankruptcy<num_players-1:
         if players[counter][1].get_status() == "normal":
            board = gameround(counter, board)
        
        
        #Cycling between players
        
        counter += 1
        counter = counter%num_players
    
    pass
    
#Run the game

game(num_players, bankruptcy, board)
    
