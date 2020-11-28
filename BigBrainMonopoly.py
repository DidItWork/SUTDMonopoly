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
# players - list of player objects
# names - list of player names
# bankruptcy - how many people are bankrupted


#to be initialised, Jade

# building_pos - position of the buildings on the respective tiles, 
# chance_pos - position of chance tiles
# jail_pos - position of jail tiles
# tax_pos - dictionary with tax tiles positions being the keys and the amount of the taxes being the values
# cont. 0-39 anticlockwise starting from bottom left, i.e. GO is 0

# building_names - list of building names (strings)
# building_cost - list of lists of the cost at each of the 3 levels for each respective building
# chance_names - a list of all the names of the chance cards, list of strings

num_of_tiles = 4
num_players = 0
bankruptcy = 0
tiles = []
players = []
names = []
pass_go = 200


building_pos = list(range(4))
building_names = ["a","b","c","d"]
building_cost = [[100,200,300],[100,200,300],[100,200,300],[100,200,300]]
chance_pos = []
jail_pos = []
tax_pos = {}
chance_names = []




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
        self.building = []

        
        self.id_no += 1
      
    
    def get_status(self):
        return self.status
    
    def update_status(self,status):
        #normal, bankrupt, jailed, frozen
        self.status = status
    
    def get_position(self):
        return self.position
    
    def update_position(self, position):
        self.position += position
        self.position = self.position%num_of_tiles
    
    def teleport(self,position):
        self.position = position
    
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

    def level_up(self):
        
        self.level +=1
    
    def set_ownership(self,player_id):
        
        self.owner = player_id

    def get_name(self):
        
        return self.name
    
    def get_cost(self, *level):
        
        cost = 0
        
        if len(level) == 0:  
            if self.level == 0:
                return self.cost[0]
            else:
                for i in range(self.level):
                    cost += self.cost[i]
                return cost
        
    def get_owner(self):
        return self.owner
    
    def get_level(self):
        return self.level
        
        
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
    
class card():
	id_no = 0
	
    # Notice how it is *cost, the * indicates that cost is an optional argument
	def __init__(self, name, effect, *cost):
		self.id = self.id_no
		self.name = name
        
        # Effect will be a tuple of objects
		self.effect = effect, *cost

		self.id_no += 1
	
	def get_name(self):
		return self.name
	
	def get_effect(self):
		return self.effect
    
#game functions
#-------------------------------------------------------------------------#

def roll(strength):
    
    #return a tuple of two integers (1-6) from dice rolls
    
    # Strength is just a pseudo code to give the illusion of choice to the user
    
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    
    return dice1, dice2

def update_board(board):
    
    #return an updated board from the old board
    
    # Tim will do this
    
    print("Printing board")
    
    pass


def display_board(board):
    
    # probably use some print function to do so
    #display board
    
    # Tim will do this
    
    print("Display board")
    
    pass


def home(player_id):
    
    # pass_go as a global variable in case we wanted to add it somewhere else too
    
    players[player_id].update_sanity(pass_go)    
    pass

def jail(player_id):
    
    players[player_id].update_status("jail")
    players[player_id].teleport(jail_pos) #add tile position of jail
    
    # Change players[player_id]'s status to "jail" and players[player_id]'s position to <insert jail position>, return nothing
    # Hint: use the .update_status(<string>) to change the player's status,
    # use .teleport(<integer>) to change the player's position
    pass

def tax(player_pos,player_id):

    val = tax_pos[player_pos]
    players[player_id].update_sanity(-val)
    
    # Subtract <insert number> sanity points from players[player_id], return nothing
    # Hint use the .update_sanity(-<insert number>) method for the player object
    
    pass
    
def chance(player_pos, player_id):
    
    # Need to add new def for freeze
    # Randomly choose a card from chance and return it to the player
    
    val = random.radin (0,200)
    card_names = ["You were too lazy to wear your mask to the toilet and GOT CAUGHT!", "You gamed all night yesterday and fell asleep during Physics :(""You attended fifth-row!", "You got an A for CTD Assignment!", "It's ice-cream day! You collected free ice-cream from student government!", "Yay! There's no zoom webinar for HASS this week! More sleep!", "You bought healthy soup and the uncle gave you free sides! Nomnom...", "It's finally the weekend!", "It's term-break! Finally some rest...", "Oh no! You are late for class!", "Crap! You forgot your laundary!", "Crap! You lost your room card!", "You failed Modelling and Analysis! :(", "You failed Physcial World! :(", "You failed your finals and you are now in bOOtCAMP! :(", "Oww... You bought mixed rice and got food poisoning.", "Oh no! You forgot to bring your charger to class and your laptop is dying!"]
    card_effects = [freeze, jail, update_sanity]
    temp_names = []
    
    choice = random.randin (0,len(card_names)-1)
    print(card_names[choice])
    
    if choice == 0:
        #Need to add new def for freeze help
        card_effects[0]()
    
    elif choice == 1: 
        card_effects[1](player_id)

    elif 0 < choice <= 7:
        players[player_id].card_effects[1](+val)
        print ("Congratualations! You have gained", val, "sanity.")

    elif choice >7 :
        players[player_id].card_effects[1](-val)
        print ("Aww man... You just lost", val, "sanity")


    if len(card_names) == 0:
        length = len(temp_names)
        for i in range(length):
            card_names.append(temp_names.pop())
    pass

def pay_rent(from_player, to_player, amount):
    
    print("Payer %s : " % names[from_player], players[from_player].get_sanity())
    print("Landlord %s : " % names[to_player], players[to_player].get_sanity())
    
    
    if int(players[from_player].get_sanity()) < amount:
        leftovers = int(players[from_player].get_sanity())
        
        players[to_player].update_sanity(leftovers)
        players[from_player].update_sanity(-leftovers)
        
        amount -= leftovers
        
    else:
        
        players[from_player].update_sanity(-amount)
        players[to_player].update_sanity(amount)
        amount = 0
        
    print(amount, -amount)
    print("Payer %s : " % names[from_player], players[from_player].get_sanity())
    print("Landlord %s : " % names[to_player], players[to_player].get_sanity())
    
    if players[from_player].get_sanity() == 0:
        
        sell = 0
        sell_building = []
        owned_building = []
        sell_cost = 0
        total_cost = 0
        
        for i in building_pos:
            if tiles[i].get_building().get_owner() == from_player:
                owned_building.append(i)
                owned_building.append(tiles[i].get_building().get_name())
                owned_building.append(tiles[i].get_building().get_cost())
                
                sell_building.append(owned_building[:])
                
                owned_building = []
                
                total_cost += tiles[i].get_building().get_cost()
                
        if len(sell_building) == 0:
            print("bAnKrUpT g3t g00d n00b")
            players[from_player].update_status("Bankrupt")
        elif total_cost < amount:
            for i in range(len(sell_building)):
                tiles[sell_building[i][0]].get_building().set_ownership(to_player)
                
            print("bAnKrUpT g3t g00d n00b")
            players[from_player].update_status("Bankrupt")
            
        else:
            while amount > 0:
                print("Index", "Name", "Value")
                for index, value in enumerate(sell_building):
                    print(index + 1, value[1], value[2])
              
                while sell < 1 or sell > len(sell_building) + 1:
                    sell = int(input("Choose building index to sell 1 to %s: " % len(sell_building)))
                
                sell -= 1
                
                amount -= sell_building[sell][2]
                tiles[sell_building[sell][0]].get_building().set_ownership(to_player)
                print(tiles[sell_building[sell][0]].get_building().get_owner())
                
                sell_building.pop(sell)
                
                if amount == 0:
                    return
               
                if len(sell_building) == 0:
                    print("bAnKrUpT g3t g00d n00b")
                    players[from_player].update_status("Bankrupt")
                    return

def gameround(player_id):
    dice1 = None
    dice2 = None
    step = 0
    player = players[player_id]
    
    #Player with player_id plays this round
    print("It's %s 's turn." % (player.get_name()))

     
        
    while dice1==dice2:
        
        #check if player goes bankrupt
        
        buy = "z"
        strength = 0
        
        
        while strength < 1 or strength >5:
            strength = int(input("Roll Strength (1-5): "))
        dice1, dice2 = roll(strength)
        print("Roll 1:", dice1)
        print("Roll 2:", dice2)
        step = dice1+dice2
        player.update_position(step)
        player_pos = player.get_position()
        print("Player position:",player.get_position())
        
        if tiles[player_pos].get_type()=="building":
            
            active_building = tiles[player_pos].get_building()
            
            if active_building.get_owner()==None and active_building.get_cost()<=player.get_sanity():
                while buy[0] not in "yYnN":
                    buy = input(("Do you want to buy %s, cost: %s sanity [y/n]? " % (active_building.get_name(), active_building.get_cost())))
                    
                if buy[0] in "yY":
                    active_building.set_ownership(player_id)
                    player.update_sanity(-active_building.get_cost())
                    print(player.get_sanity())
                    print("Building owned by:",names[active_building.get_owner()])
            
            elif active_building.get_owner()!=None and active_building.get_owner() != player_id:
                
                #Implement rent payment
                print("Rent time")
                
                pay_rent(player_id,active_building.get_owner(), active_building.get_rent())
                print(active_building.get_rent())
                if player.get_status() == "Bankrupt":
                    break
                
            elif active_building.get_owner()!=None and active_building.get_owner() == player_id:
                
                if active_building.get_cost()>player.get_sanity() or active_building.get_level()>2:
                    print("Sorry, you do not have enough sanity to upgrade this building")
                else:
                    while buy[0] not in "yYnN":
                        buy = input(("Do you want to upgrade %s to Level %s , cost: %s sanity [y/n]? " 
                                     % (active_building.get_name(), 
                                        active_building.get_level()+2, 
                                        active_building.get_cost(active_building.get_level()+1))))
                        
                    if buy[0] in "yY":
                        active_building.level_up()
                        player.update_sanity(-active_building.get_cost())
                        print(player.get_sanity())
                        print("Building owned by:",names[active_building.get_owner()])
            else:
                print("Ha sorry you broke")
                
        elif tiles[player_pos].get_type()=="chance":
            
            chance()
        
        elif tiles[player_pos].get_type()=="tax":
            
            tax(player_pos,player_id)
        
        elif tiles[player_pos].get_type()=="jail":
            
            jail(player_id)
        
        elif tiles[player_pos].get_type()=="home":
            
            home()
        
        else:
            print("Some error occurred")


        # new_board = update_board(board)
        # display_board(new_board)
    wait = input("Waiting...")
    
    # return board
    pass


#Initialising variables
#-------------------------------------------------------------------------#
def render_game():
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
        
    # Render chance cards here

def game(num_players, bankruptcy):
    
    #game initialisation
    while num_players < 2 or num_players > 5:
        num_players = int(input("Number of players (2-5): "))
        
    for i in range(1, num_players+1):
        while True:
            name = input(f"Enter Player {i}'s name: ")
            if name not in names:
                players.append(player(name))
                names.append(name)
                break
            else:
                print("Name already exist! Please Reenter name")
                
    #Initialising variables
    render_game()
        
    counter = 0
    #Run the game rounds repeatedly until someone wins, if the player is bankrupt, skip the player
    while bankruptcy<num_players-1:
        if players[counter].get_status() == "normal":
           gameround(counter)
        
        
        #Cycling between players
        counter += 1
        counter = counter%num_players
    
    pass
    
#Run the game
game(num_players, bankruptcy)
   
