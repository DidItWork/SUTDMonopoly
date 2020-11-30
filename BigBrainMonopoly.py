# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 17:54:30 2020

@author: Benjamin Luo
"""

import math
import random

#Initialise parameters, building values is a list of lists
#-------------------------------------------------------------------------#
# num_players - keep track of how players that are still "alive"
# tiles - list of tile objects making up the board
# players - list of player objects
# names - list of player names

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
tiles = []
players = []
names = []
pass_go = 200
cards = []

building_pos = list(range(4))
building_names = ["a","b","c","d"]
building_cost = [[100,200,300],[100,200,300],[100,200,300],[100,200,300]]
# building_cost = [[500,200,300],[500,200,300],[500,200,300],[500,200,300]]
chance_pos = []
jail_pos = 7
tax_pos = {}
chance_names = []

# Defining classes of objects
#-------------------------------------------------------------------------#
class player():
    
    # for functions on setting variables and getting variable values, use getters and setter
    id_no = 0
    
    def __init__(self, name):
        self.__id = self.id_no
        self.__status = "Normal"
        self.__position = 0
        self.__name = name
        self.__sanity = 500 
        self.__building = []

        self.id_no += 1
      
    def get_status(self):
        return self.__status
    
    def update_status(self,status):
        #Normal, Bankrupt, Jailed, Frozen
        self.__status = status
        
        if status == "Bankrupt":
            global num_players
            num_players -= 1
            print("Numplayers: ", num_players)
        
    
    def get_position(self):
        return self.__position
    
    def update_position(self, position):
        self.__position += position
        self.__position = self.__position%num_of_tiles
    
    def teleport(self,position):
        self.__position = position
    
    def get_name(self):
        return self.__name
    
    def get_sanity(self):
        return self.__sanity
    
    def update_sanity(self,sanity):
        self.__sanity += sanity

class building():
    
    # Don't need colour cause can't present colours anyways
    def __init__(self, name, cost):
        
        # I don't think values should be a dictionary, should just be a list of 3 values and use "level", 0, 1, 2
        # To get the value. Else values can just be a global dictionary already
        
        # values is a dictionary with the key being the building name and its value
        # being a list of three numbers with each number indicating its value at the
        # respective level
        
        self.__level = 0
        self.__owner = None
        self.__cost = cost #list of three integers indicating the costs of the building
        self.__name = name
        
    
    def get_rent(self):
        # rent of building calculated from cost and level 
        return self.__cost[self.__level]*1.5

    def level_up(self):
        self.__level +=1
    
    def set_ownership(self, player_id):
        self.__owner = player_id

    def get_name(self):
        return self.__name
    
    def get_cost(self, *level):
        cost = 0
    
        if len(level) == 0:  
            if self.__level == 0:
                return self.__cost[0]
            else:
                for i in range(self.__level):
                    cost += self.__cost[i]
                return cost
        else:
            return self.__cost[level[0]]
        
    def get_owner(self):
        return self.__owner
    
    def get_level(self):
        return self.__level
        
class tile():
    id_no = 0
    
    def __init__(self, tile_type, building):
        self.__id = self.id_no
        self.id_no += 1
        
        self.__tile_type = tile_type
        
        if self.__tile_type == "building":
            self.__building = building
    
    def get_type(self):
        return self.__tile_type
    
    def get_building(self):
        return self.__building
    
class card():
	id_no = 0
	
    # Notice how it is *cost, the * indicates that cost is an optional argument
	def __init__(self, name, effect, *cost):
		self.__id = self.id_no
		self.__name = name
        
        # Effect will be a tuple of objects
		self.__effect = effect, *cost

		self.id_no += 1
	
	def get_name(self):
		return self.__name
	
	def get_effect(self):
		return self.__effect
    
# Game functions
#-------------------------------------------------------------------------#
def roll():
    #return a tuple of two integers (1-6) from dice rolls
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    
    return dice1, dice2

def home(player_id):
    players[player_id].update_sanity(pass_go)    
    pass

def jail(player_id):
    players[player_id].update_status("jail")
    players[player_id].teleport(jail_pos)
    pass

def tax(player_pos,player_id):
    val = tax_pos[player_pos]
    players[player_id].update_sanity(-val)
    pass
    
def chance(player_id):
    carded = list(range(0, len(cards)))
    # Wouldn't this line make it not possible to remove the card from deck permanently?
    # Everytime the chance() is executed this line would erase previous' carded list?
    temp_carded = []
    randomz = random.choice(carded)
    carded.remove(randomz)
    temp_carded.append(randomz)
    if len(carded) == 0:
        for i in range(len(temp_carded)):
            carded.append(temp_carded.pop())


    print (cards[randomz].get_name())

    if cards[randomz].get_effect()[0] == "update sanity":
        if cards[randomz].get_effect()[1] < 0:
            print ("Your sanity decreased by", cards[randomz].get_effect()[1], "sanity")
            players[player_id].update_sanity(cards[randomz].get_effect()[1])
        elif cards[randomz].get_effect()[1] > 0:
            print ("Your sanity increased by", cards[randomz].get_effect()[1], "sanity")
            players[player_id].update_sanity(cards[randomz].get_effect()[1])

    elif cards[randomz].get_effect()[0] == "sanity for all":
        for i in range(len(players)):
            players[i].update_sanity(cards[randomz].get_effect()[1])
        players[player_id].update_sanity(cards[randomz].get_effect()[1])

    elif cards[randomz].get_effect()[0] == "birthday":
        for i in range(len(players)):
                players[i].update_sanity(-cards[randomz].get_effect()[1])
        player_id.update_sanity(2*cards[randomz].get_effect()[1])

    elif cards[randomz].get_effect()[0] == "go to jail":
        jail(player_id)

    elif cards[randomz].get_effect()[0] == "roll double":
        # ????
        pass

    elif cards[randomz].get_effect()[0] == "lose a property":
        #property list is under other functions
        pass
    
def pay_rent(from_player, to_player, amount):
    
    print("Rent time")
    
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
                    sell = input("Choose building index to sell 1 to %s: " % len(sell_building))
                    try:
                        sell = int(sell)
                    except:
                        sell = 0
                
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
    pass

def upgrade_building(active_building, player):
    buy = "z"
    print(type(active_building.get_level() + 1))
    while buy[0] not in "yYnN":
        buy = input("Do you want to upgrade %s to Level %s , cost: %s sanity [y/n]? " 
                     % (active_building.get_name(), 
                        active_building.get_level() + 2, 
                        active_building.get_cost(active_building.get_level() + 1)))
        if buy == "":
            buy = "z"
        
    if buy[0] in "yY":
        active_building.level_up()
        player.update_sanity(-active_building.get_cost())
        print(player.get_sanity())
        print("Building owned by:",names[active_building.get_owner()])
    pass

def buy_building(player, player_id, active_building):
    buy = "z"
    while buy[0] not in "yYnN":
        buy = input(("Do you want to buy %s, cost: %s sanity [y/n]? " % (active_building.get_name(), active_building.get_cost())))
        if buy == "":
            buy = "z"
        
    if buy[0] in "yY":
        active_building.set_ownership(player_id)
        player.update_sanity(-active_building.get_cost())
        print(player.get_sanity())
        print("Building owned by:",names[active_building.get_owner()])
    pass

# Game
#-------------------------------------------------------------------------#
def gameround(player_id):
    dice1 = None
    dice2 = None
    step = 0
    player = players[player_id]
    
    doubles = 0
    
    #Player with player_id plays this round
    print("It's %s 's turn." % (player.get_name()))
        
    while dice1==dice2:
        # Pseudo code to give the impression of control
        input("Press 'Enter' to roll.")
        
        dice1, dice2 = roll()
        print("Roll 1:", dice1)
        print("Roll 2:", dice2)
        step = dice1 + dice2
        
        # Counter for doubles, maximum of 3 doubles in a row
        if dice1 == dice2:
            doubles += 1
            
        if doubles == 3:
            jail(player_id)
        
        player.update_position(step)
        player_pos = player.get_position()
        print("Player position:", player.get_position())
        
        if tiles[player_pos].get_type()=="building":
            active_building = tiles[player_pos].get_building()
            
            # If tile is empty and can afford
            if active_building.get_owner() == None and active_building.get_cost()<=player.get_sanity():
                buy_building(player, player_id, active_building)
            
            # If landed on an owned tile
            elif active_building.get_owner()!=None and active_building.get_owner() != player_id:
                pay_rent(player_id,active_building.get_owner(), active_building.get_rent())
                
                # Break if player goes bankrupt here
                if player.get_status() == "Bankrupt":
                    break
            
            # If landed on own building, upgrade if possible
            elif active_building.get_owner() == player_id:
                if active_building.get_level() > 2:
                    print("Building at max level!")
                elif active_building.get_cost() > player.get_sanity():
                    print("Sorry, you do not have enough sanity to upgrade this building.")
                else:
                    upgrade_building(active_building, player)
                    
            # If not enough money to buy building
            else:
                print("Ha sorry you broke.")
                
        # Other tiles
        elif tiles[player_pos].get_type()=="chance":
            chance()
        elif tiles[player_pos].get_type()=="tax":
            tax(player_pos,player_id)
        elif tiles[player_pos].get_type()=="jail":
            jail(player_id)
        elif tiles[player_pos].get_type()=="home":
            home()
        else:
            print("Some error occurred.")
            
        update_board()
        display_board()
    
    # return board
    pass

# Init game and get players
#-------------------------------------------------------------------------#
def game():
    # Initialising variables
    render_game()
    
    # Get number of 
    global num_players
    
    while num_players < 2 or num_players > 5:
        num_players = input("Number of players (2-5): ")
        try:
            num_players = int(num_players)
        except:
            num_players = 0
    
    # Get names of players
    for i in range(1, num_players + 1):
        while True:
            name = input(f"Enter Player {i}'s name (1 to 6 characters): ")
            if len(name) < 1 or len(name) > 6:
                print("Name must be from 1 to 6 characters.")
            elif name not in names:
                players.append(player(name))
                names.append(name)
                break
            else:
                print("Name already exist! Please Reenter name.")
        
    #Run the game rounds repeatedly until someone wins, if the player is bankrupt, skip the player
    counter = 0
    while num_players != 1:
        if players[counter].get_status() == "Normal":
           gameround(counter)
        
        #Cycling between players
        counter += 1
        counter = counter % num_players
        
    winner = ""
        
    for play in players:
        if play.get_status() == "Normal":
            winner = play.get_name()
            break
            
    print("\nWinner: " + winner + "!")
    pass

# Initialising variables
#-------------------------------------------------------------------------#
def render_game():
    for i in range(num_of_tiles):
        if i == 0:
            tiles.append(tile("home",""))
        elif i in building_pos:
            tiles.append(tile("building", building(building_names[i], building_cost[i])))
        elif i in chance_pos:
            tiles.append(tile("chance",""))
        elif i in jail_pos:
            tiles.append(tile("jail",""))
        elif i in tax_pos:
            tiles.append(tile("tax",""))
            
    cards.append(card("You got accepted for scholarship!", "update sanity", 50))
    cards.append(card("You got an A for CTD Assignment!", "update sanity", 50))
    cards.append(card("You got an A for HASS Assignment!", "update sanity", 50))
    cards.append(card("You got an A for Physics Finals!", "update sanity", 50))
    cards.append(card("You got an A for Math Finals!", "update sanity", 50))
    cards.append(card("You passed Freshmore Term 1!", "update sanity", 30))
    cards.append(card("You attended fifth-row!", "update sanity", 30))
    cards.append(card("Yay! There's no zoom webinar for HASS this week! More sleep!", "update sanity", 10))
    cards.append(card("It's term-break! Finally some rest...", "update sanity", 10))

    cards.append(card("Oh no! You are late for class!", "update sanity", -10))
    cards.append(card("You gamed all night yesterday and fell asleep during class!", "update sanity", -10))
    cards.append(card("You became the hard carry of your group", "update sanity", -20))
    cards.append(card("Crap! You forgot your laundry!", "update sanity", -20))
    cards.append(card("You deleted Rhino after CTD, now you have to re-download it for 2D", "update sanity", -30))
    cards.append(card("You lost your room card!", "update sanity", -30))

    cards.append(card("It's ice-cream day! You collected free ice-cream from student government! Everyone gets 20 sanity", "sanity for all",20))
    cards.append(card("It's your birthday! Receive 20 sanity from all players!", "birthday", 20))
    cards.append(card("You failed your finals and you are now in bOOtCAMP!", "lose a property"))    
    cards.append(card("You were too lazy to wear your mask to the toilet and GOT CAUGHT! You are going to jail!", "go to jail"))
    cards.append(card("You are now buying from mixed rice stall! Roll double in order to enjoy your meal!", "roll double", 50))

    # Render chance card under here
    
# GUI/Board functions
#-------------------------------------------------------------------------#
def update_board():
    
    #return an updated board from the old board
    
    # Tim will do this
    print("Updating")
    return
    pass

def display_board():
    
    # probably use some print function to do so
    #display board
    
    # Tim will do this
    
    print("Display board")
    return
    pass

#Run the game
game()
