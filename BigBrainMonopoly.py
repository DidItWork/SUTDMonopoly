# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 17:54:30 2020

@author: Benjamin Luo
"""

import tkinter
import random

#Initialise parameters, building values is a list of lists
#-------------------------------------------------------------------------#
# num_of_tiles - global number of tiles
# tiles - list of tile objects making up the board

# num_players - keep track of how players that are still "alive"
# players - list of player objects
# names - list of player names

# pass_go - amount added for passing go
# jail_pos - position of jail tiles
# tax_pos - dictionary with tax tiles positions being the keys and the amount of the taxes being the values
# chance_pos - position of chance tiles
# cards - list of chance cards avaliable
# carded - list of cards that are not drawn

# building_pos - position of the buildings on the respective tiles, 
# cont. 0-39 anticlockwise starting from bottom left, i.e. GO is 0

# building_info - nested list of building information
# cont. building_info[x] are building names
# cont. building_info[x][y] are building costs (if applicable)

num_of_tiles = 24
tiles = []

num_players = 0
players = []
names = []

pass_go = 200
cards = []
carded = []

tax_name = "tax"
go_name = "Pass go"

go_pos = 0
jail_pos = 6
tax_pos = {9: 100, 21: 50}
chance_pos = [3, 15]
freeParking_pos = 12
goToJail_pos = 18
building_pos = [1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23]

building_info = ["home",
                ["Smith’s invisible hand", "Smith", [120, 150, 210]],
                ["Geertz’s fighting cocks", "Geertz", [120, 150, 210]],
                "chance",
                ["L’Hopital’s Glue", "L’Hopital", [80, 100, 140]],
                ["Riemann’s Sun", "Riemann", [120, 150, 210]],
                "jail",
                ["Baked Rhino", "Rhino", [60, 80, 120]],
                ["Flattened Grasshopper", "Grasshopper", [60, 80, 120]],
                "tax",
                ["Hooke’s Hook", "Hooke", [80, 100, 140]],
                ["Newton’s Apple", "Newton", [120, 150, 210]],
                "free parking",
                ["Vocareum", "Vocareum", [80, 100, 140]],
                ["Jupyter", "Jupyter", [80, 100, 140]],
                "chance",
                ["IMU Device", "IMU Device", [120, 150, 210]],
                ["Parachute", "Parachute", [80, 100, 140]],
                "go to jail",
                ["Piazza", "Piazza", [100, 120, 180]],
                ["Edimension", "Edimension", [120, 150, 210]],
                "tax",
                ["Fairprice Xtra", "Fairprice", [50, 70, 100]],
                ["Pick n’ Go", "Pick n’ Go", [160, 200, 280]]]

#Initialise parameters for the GUI
#-------------------------------------------------------------------------#
boxLength = 100
boxHeight = 130
smolBoxHt = 90
rot = [270, 180, 90, 0]
priceIDs = {}
ownedIDs = {}
playerIDs = {}
sanCounter = []
guideBoxes = []

dicePips1 = []
dicePips2 = []

cornerPos = num_of_tiles/4
cornerXYs = [[boxHeight+5*boxLength, boxHeight+5*boxLength, 2*boxHeight+ 5*boxLength, 2*boxHeight+ 5*boxLength], 
             [0, boxHeight+5*boxLength, boxHeight, 2*boxHeight+5*boxLength],
             [0,0,boxHeight,boxHeight],
             [boxHeight+5*boxLength,0,2*boxHeight+5*boxLength,boxHeight]] #hardcoded corners
centreGo = [(cornerXYs[0][0]+cornerXYs[0][2])/2 + 7.5, (cornerXYs[0][1]+cornerXYs[0][3])/2 + 7.5]
boardDimensionY = 2*(boxHeight) + (7-2)*(boxLength)

diceMaps = [[0,0,0,1,0,0,0],
            [1,0,0,0,0,0,1],
            [1,0,0,1,0,0,1],
            [1,1,0,0,0,1,1],
            [1,1,0,1,0,1,1],
            [1,1,1,0,1,1,1]]

playerCols = ['green', 'blue', 'red', "magenta", "cyan"]
playerPos = [centreGo, 
             [centreGo[0]+20, centreGo[1]+20],
             [centreGo[0]-20, centreGo[1]+20],
             [centreGo[0]+20, centreGo[1]-20],
             [centreGo[0]-20, centreGo[1]-20]]
inJail = []
justVisiting = []

top = tkinter.Tk()
widg = tkinter.Canvas(top, bg = "black", height = boardDimensionY, width = boardDimensionY)

# Defining classes of objects
#-------------------------------------------------------------------------#
class player():
    id_no = 0
    
    def __init__(self, name):
        self.__id = self.id_no
        self.__status = "Normal"
        self.__position = 0
        self.__name = name
        self.__sanity = 500 
        self.__building = []
        self.__jail = 0

        self.id_no += 1
      
    def get_status(self):
        return self.__status
    
    def update_status(self,status):
        #Normal, Bankrupt, Jailed, Frozen
        self.__status = status
        
        if status == "Bankrupt":
            global num_players
            num_players -= 1
        
        if status == "Jail":
            self.__jail = 3
            pass
    
    def get_position(self):
        return self.__position
    
    def update_position(self, position):
        self.__position += position
        self.__position = self.__position % num_of_tiles
    
    def teleport(self,position):
        self.__position = position
    
    def get_name(self):
        return self.__name
    
    def get_sanity(self):
        return self.__sanity
    
    def update_sanity(self, sanity):
        self.__sanity += sanity
    
    def get_jailCount(self):
        return self.__jail
    
    def update_jailCount(self):
        self.__jail -= 1
        
        if self.__jail == 0:
            self.__status = "Normal"
    
class building():

    def __init__(self, name, truncated, cost):
        
        self.__level = 0
        self.__owner = None
        self.__cost = cost
        self.__name = name
        self.__truncated = truncated
    
    def get_rent(self):
        # rent of building calculated from cost and level 
        return self.__cost[self.__level]*1.5

    def level_up(self):
        self.__level +=1
    
    def set_ownership(self, player_id):
        self.__owner = player_id

    def get_name(self):
        return self.__name

    def get_truncated(self):
        return self.__truncated
    
    def get_cost(self, *level):
        cost = 0

        if len(level) == 0:
            for i in range(self.__level + 1):
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
    
    def __init__(self, tile_type, *building):
        self.__id = self.id_no
        self.id_no += 1
        
        self.__tile_type = tile_type
        
        if self.__tile_type == "building":
            self.__building = building[0]
    
    def get_type(self):
        return self.__tile_type
    
    def get_building(self):
        return self.__building

class card():
    id_no = 0
    
    def __init__(self, name, effect, *cost):
        self.__id = self.id_no
        self.__name = name
        
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
    print("Roll 1:", dice1)
    print("Roll 2:", dice2)
    print("\n")
    
    return dice1, dice2

def home(player_id):
    print(f"{go_name}, regain {pass_go} sanity!")
    players[player_id].update_sanity(pass_go)
    pass

def jail(player_id):
    print("You landed in jail!")
    players[player_id].update_status("Jail")
    players[player_id].teleport(jail_pos)
    pass

def tax(player_pos,player_id):
    val = tax_pos[player_pos]
    print(f"Opps, you landed on {tax_name} and lost {val} sanity.")
    players[player_id].update_sanity(-val)
    pass

def free_parking():
    print("Free parking, take a break!")
    
def chance(player_id):
    
    global carded
    
    # Re-init carded if its empty
    if len(carded) == 0:
        carded = list(range(len(cards)))
    
    # Randomly chosing a card
    chosen = random.choice(carded)
    carded.remove(chosen)

    print(cards[chosen].get_name())

    # If "update sanity"
    if cards[chosen].get_effect()[0] == "update sanity":
        
        # If card chosen decreases sanity
        if cards[chosen].get_effect()[1] < 0:
            
            # If player does not have enough sanity to lose
            if players[player_id].get_sanity() < -cards[chosen].get_effect()[1]:
                bankrupt(-cards[chosen].get_effect()[1], player_id, None)
            else:
                players[player_id].update_sanity(cards[chosen].get_effect()[1])
                print ("Your sanity decreased by", -cards[chosen].get_effect()[1], "sanity.")

        # If card chosen increases sanity
        elif cards[chosen].get_effect()[1] > 0:
            players[player_id].update_sanity(cards[chosen].get_effect()[1])
            print ("Your sanity increased by", cards[chosen].get_effect()[1], "sanity.")

    # If "sanity for all"
    elif cards[chosen].get_effect()[0] == "sanity for all":
        for i in range(len(players)):
            players[i].update_sanity(cards[chosen].get_effect()[1])
    
    # If "birthday"
    elif cards[chosen].get_effect()[0] == "birthday":
        for i in range(len(players)):
            
            if i == player_id:
                continue
            
            # If player does not have enough sanity to lose
            elif players[i].get_sanity() < cards[chosen].get_effect()[1]:
                bankrupt(cards[chosen].get_effect()[1], i, player_id)

            else:
                players[player_id].update_sanity(cards[chosen].get_effect()[1])
                players[i].update_sanity(-cards[chosen].get_effect()[1])
        
    # If "jail"
    elif cards[chosen].get_effect()[0] == "go to jail":
        jail(player_id)
        
    # If "roll"
    elif cards[chosen].get_effect()[0] == "roll double":
        input("Press 'Enter' to roll.")
        
        dice1, dice2 = roll()
        
        if dice1 == dice2:
            players[player_id].update_sanity(cards[chosen].get_effect()[1])
            print ("You gobbled down your caifan like a vaccum cleaner...\n...\nbut you are fine!")
            print ("Your sanity increased by", cards[chosen].get_effect()[1], "sanity.")
        
        else:
            
            # If player does not have enough sanity to lose
            if players[player_id].get_sanity() < cards[chosen].get_effect()[1]:
                bankrupt(cards[chosen].get_effect()[1], player_id, None)
            else:                     
                players[player_id].update_sanity(-cards[chosen].get_effect()[1])
                print ("You gobbled down your caifan like a vaccum cleaner...\n...\nand got food poisoning!")
                print ("Your sanity decreased by", cards[chosen].get_effect()[1], "sanity.")
    
    # If "lose property"
    elif cards[chosen].get_effect()[0] == "lose a property":
        
        owned_building = []
        lose_building = []
        lose = 0
        
        for i in building_pos:
            if tiles[i].get_building().get_owner() == players[player_id]:
                owned_building.append(i)
                owned_building.append(tiles[i].get_building().get_name())
                owned_building.append(tiles[i].get_building().get_cost())
                
                lose_building.append(owned_building[:])
                owned_building = []
            
         # If player owns no building, teleport them to jail
        if len(lose_building) == 0:
            print("You have no property to lose. You are going to JAIL!!")
            jail(player_id)
            
        # If player owns building, give an option to choose a building to sell
        else: 
            print("Index", "Name", "Value", "\n")
            for index, value in enumerate(lose_building):
                print(index + 1, value[1], value[2])

            while lose < 1 or lose > len(lose_building) + 1:
                  lose = int(input("Choose building index to lose: 1 to %s: " % len(lose_building)))
                  try:
                      lose = int(lose)
                  except:
                      lose = 0

            tiles[lose_building[lose - 1][0]].get_building().set_ownership(None)
            print("Your have lost ownership of", lose_building[lose - 1][1])
        pass
    
def pay_rent(from_player, to_player, amount):
    print("\nRent time!")
    print(f"Pay {amount} sanity to {names[to_player]}.")
    
    # Check if there's enough sanity to transfer
    if int(players[from_player].get_sanity()) < amount:
        leftovers = int(players[from_player].get_sanity())
        
        players[to_player].update_sanity(leftovers)
        players[from_player].update_sanity(-leftovers)
        
        amount -= leftovers
    else:
        players[from_player].update_sanity(-amount)
        players[to_player].update_sanity(amount)
        return
    
    bankrupt(amount, from_player, to_player)
    pass

def upgrade_building(active_building, player):
    buy = "y"
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
    pass

def buy_building(player, player_id, active_building):
    buy = "y"
    while buy[0] not in "yYnN":
        buy = input(("Do you want to buy %s, cost: %s sanity [y/n]? " % (active_building.get_name(), active_building.get_cost())))
        if buy == "":
            buy = "z"
        
    if buy[0] in "yY":
        active_building.set_ownership(player_id)
        player.update_sanity(-active_building.get_cost())
        print(f"{active_building.get_name()} is now owned by: {names[active_building.get_owner()]}")
    pass

def bankrupt(amount, from_player, to_player):
    print(f"{names[from_player]} is out of sanity!")
    
    # Initialize some local variables for later
    sell = 1
    total_cost = 0
    sell_building = []
    owned_building = []
    
    # Check if the player owns any buildings
    for i in building_pos:
        if tiles[i].get_building().get_owner() == from_player:
            owned_building.append(i)
            owned_building.append(tiles[i].get_building().get_name())
            owned_building.append(tiles[i].get_building().get_cost())
            
            sell_building.append(owned_building[:])
            
            owned_building = []
            
            total_cost += tiles[i].get_building().get_cost()
            
    # If owner owns no building, bankrupt them
    if len(sell_building) == 0:
        print("bAnKrUpT g3t g00d n00b")
        players[from_player].update_status("Bankrupt")
    
    # If owner building does not cover up rent, bankrupt them and transfer all property
    elif total_cost < amount:
        for i in range(len(sell_building)):
            tiles[sell_building[i][0]].get_building().set_ownership(to_player)
            
        print("bAnKrUpT g3t g00d n00b")
        players[from_player].update_status("Bankrupt")
        
    # If owner owns building, give an option to liquidate assets until amount == 0
    else:
        while amount > 0:
            print(f"\nYou still owe {int(amount)} sanity.\n")
            print("Index", "Name", "Value")
            for index, value in enumerate(sell_building):
                print(index + 1, value[1], value[2])

            while sell < 1 or sell > len(sell_building):
                sell = input("Choose building index to sell 1 to %s: " % len(sell_building))
                try:
                    sell = int(sell)
                except:
                    sell = 0
            
            sell -= 1
            
            # Update amount according to the buildings sold
            amount -= sell_building[sell][2]
            tiles[sell_building[sell][0]].get_building().set_ownership(to_player)
            
            sell_building.pop(sell)
            
            if amount <= 0:
                return
           
            if len(sell_building) == 0:
                print("bAnKrUpT g3t g00d n00b")
                players[from_player].update_status("Bankrupt")
                return
    pass

def jail_turn(player_id):
    if players[player_id].get_jailCount() > 1:
        input("Roll a double to break out of jail! Press 'Enter' to roll.")
        dice1, dice2 = roll()
        
        if dice1 == dice2:
            players[player_id].update_status("Normal")
            print("PRISON BREAK!!!")
        else:
            players[player_id].update_jailCount()
            print(f"You're still in jail! Turns till freedom: {players[player_id].get_jailCount()}.")
    else:
        players[player_id].update_jailCount()
    pass

# Gameround
#-------------------------------------------------------------------------#
def gameround(player_id):
    dice1 = None
    dice2 = None
    step = 0
    player = players[player_id]
    
    doubles = 0

    while dice1==dice2:
        # Pseudo code to give the impression of control
        input("\nPress 'Enter' to roll.")
        
        dice1, dice2 = roll()
        
        step = dice1 + dice2
        
        # Counter for doubles, maximum of 3 doubles in a row
        if dice1 == dice2:
            doubles += 1
            
        if doubles == 3:
            print("You rolled a double 3 times a row! You're going to JAIL for being a CHEATER!")
            jail(player_id)
            return
            
        player_pos = player.get_position()
        if player_pos + step > num_of_tiles:
            home(player_id)
        
        player.update_position(step)
        
        update_board(player_id, dice1, dice2)
        
        player_pos = player.get_position()
        # print("Player position:", player_pos, "\n")

        if tiles[player_pos].get_type()=="building":
            active_building = tiles[player_pos].get_building()
            
            print(f"You landed on {tiles[player_pos].get_building().get_name()}.")
        
            # If tile is empty and can afford
            if active_building.get_owner() == None and active_building.get_cost() <= player.get_sanity():
                buy_building(player, player_id, active_building)
            
            # If landed on an owned tile
            elif active_building.get_owner()!=None and active_building.get_owner() != player_id:
                pay_rent(player_id,active_building.get_owner(), active_building.get_rent())
                
                # Break if player goes bankrupt here
                if player.get_status() == "Bankrupt":
                    return
            
            # If landed on own building, upgrade if possible
            elif active_building.get_owner() == player_id:
                if active_building.get_level() >= 2:
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
            chance(player_id)
        elif tiles[player_pos].get_type()=="tax":
            tax(player_pos,player_id)
        elif tiles[player_pos].get_type()=="jail":
            print("Wave to those suckers in jail!")
        elif tiles[player_pos].get_type()=="home":
            home(player_id)
        elif tiles[player_pos].get_type() == "freeParking":
            free_parking()
        elif tiles[player_pos].get_type() == "goToJail":
            jail(player_id)
            return
        else:
            print("Some error occurred.")
        
        update_board(player_id, dice1, dice2)
        
    pass

# Initialize variables and players
#-------------------------------------------------------------------------#
def game():    
    # Get number of players
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
                
    # Initialising variables
    render_game()
    
    """
    There's a bug here, where the tracking of the players and turns isn't perfect
    when there is more than 2 players
    """
    
    counter = 0
    while num_players > 1:
        print("\nIt's %s's turn." % (players[counter].get_name()))
                
        if players[counter].get_status() == "Jail":
            jail_turn(counter)
        
        if players[counter].get_status() == "Normal":
            gameround(counter) 
        
        #Cycling between players
        counter += 1
        counter = counter % num_players
    
    # When there's only 1 player left, announce winner of the game
    winner = ""
    for play in players:
        if play.get_status() == "Normal":
            winner = play.get_name()
            
    print(f"\nCongrats to {winner}!\nWinner: {winner}!")
    
    end_key = ""
    while end_key != "end":
        end_key = input("Enter 'end' to close window. ")
        end_key = end_key.lower()
    pass

def render_game():

    # Initialize the tiles accordingly
    for i in range(num_of_tiles):
        if i in building_pos:
            tiles.append(tile("building", building(building_info[i][0], 
                                                   building_info[i][1],
                                                   building_info[i][2])))
        elif i in chance_pos:
            tiles.append(tile("chance",""))
        elif i in tax_pos:
            tiles.append(tile("tax",""))
        elif i == go_pos:
            tiles.append(tile("home", ""))
        elif i == jail_pos:
            tiles.append(tile("jail",""))
        elif i == goToJail_pos:
            tiles.append(tile("goToJail", ""))
        elif i == freeParking_pos:
            tiles.append(tile("freeParking", ""))

    # Initialising chance cards            
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
    
    # Change carded on the global scale
    global carded
    carded = list(range(len(cards)))
    
    initUI()
    
# GUI/Board functions
#-------------------------------------------------------------------------#

def initUI():    
    
    top.title("SUTD-opoly")
    
    funkyBoxThings = {}
    x_i = 0
    y_i = 0
    for i in range(num_of_tiles):
        if i == 0 or i % (cornerPos) == 0:
            coords = cornerXYs[int(i//cornerPos)]
            x_i = coords[0]
            y_i = coords[1]
            if(i//cornerPos == 2):
                x_i += boxHeight
            if(i//cornerPos == 3):
                y_i += boxHeight
            myid = widg.create_rectangle(coords, fill = 'white', outline = 'black')
            funkyBoxThings[i] = getProperties(coords, 'c', myid) #corners
        elif i > 0 and i < cornerPos:
            x_i -= boxLength
            coords = [x_i, y_i, x_i+boxLength, y_i+boxHeight]
            myid = widg.create_rectangle(coords, fill = 'white', outline = 'black')
            funkyBoxThings[i] = getProperties(coords, -1, myid) #bottom row
        elif i > cornerPos and i < 2*cornerPos:
            y_i -= boxLength
            coords = [x_i, y_i, x_i+boxHeight, y_i+boxLength]
            myid = widg.create_rectangle(coords, fill = 'white', outline = 'black')
            funkyBoxThings[i] = getProperties(coords, 0, myid) #left row
        elif i > 2*cornerPos and i < 3*cornerPos:
            coords = [x_i, y_i, x_i+boxLength, y_i+boxHeight]
            x_i += boxLength
            myid = widg.create_rectangle(coords, fill = 'white', outline = 'black')
            funkyBoxThings[i] = getProperties(coords, 1, myid) #top row
            
        elif i > 3*cornerPos:
            coords = [x_i, y_i, x_i+boxHeight, y_i+boxLength]
            y_i += boxLength
            myid = widg.create_rectangle(coords, fill = 'white', outline = 'black')
            funkyBoxThings[i] = getProperties(coords, -2, myid) #right row
            
    n = False
    c = 0        
    colours = ["#CBAACB", "#F0F8FF", "#FEE1E8", "#FFD8BE", "#FF968A", "#FFFFB5", "#CCE2CB","#ABDEE6"]
    for i in range(24):
        decor = funkyBoxThings[i]
        if i in building_pos:
            
            myid = widg.create_rectangle(decor[1], outline = 'black', fill = colours[c]) #small rectangle colour setting
            if not n:
                n = True
            else:
                c+=1
                n=False
            
            owner = tiles[i].get_building().get_owner()
            if owner == None:
                owner = "---"
            
            widg.create_text(decor[4], text = tiles[i].get_building().get_truncated(), angle = decor[6])
            priceIDs[i] = widg.create_text(decor[3], text = int(tiles[i].get_building().get_rent()), angle = decor[6])
            ownedIDs[i] = widg.create_text(decor[5], text = owner, angle = decor[6])
            
        elif i == go_pos:
            widg.create_text(decor[2], text = 'GO!', angle = 45) 
        elif i == jail_pos:
            widg.create_rectangle(decor[1], outline = 'black', fill = '#FFA700')
            centre = [avg(decor[1], 'x'), avg(decor[1], 'y')]
            widg.create_text(centre, text = "JAIL", angle = 315)
            niceCorner = [centre[0]-65, centre[1]+65]
            for i in range(0, 9, 2):
                if i == 0:
                    inJail.append(centre)
                    justVisiting.append(niceCorner)
                else:
                    jailSpaceX = centre[0] - ((-1)**(not i%3 == 2))*17.5
                    jailSpaceY = centre[1] - ((-1)**(i > 5))*17.5
                    inJail.append([jailSpaceX, jailSpaceY])
                    visitSpaceX = niceCorner[0] + (i > 5)*(2**(i > 7))*30
                    visitSpaceY = niceCorner[1] - (i < 5)*(2**(i > 3))*30
                    justVisiting.append([visitSpaceX, visitSpaceY])
            
        elif i in tax_pos:
            widg.create_text(decor[2], text = "TAX\n \n{:d} \nSANITY".format(tax_pos[i]), angle = decor[6], justify = tkinter.CENTER) 
        elif i in chance_pos:
            widg.create_text(decor[2], text = "?", angle = decor[6])
            widg.create_text(decor[4], text = "CHANCE", angle = decor[6])
        elif i == freeParking_pos:
            widg.create_text(decor[2], text = "FREE\nPARKING", angle = 225, justify = tkinter.CENTER)
        elif i == goToJail_pos:
            widg.create_text(decor[2], text = "GO TO\nJAIL", angle = 135, justify = tkinter.CENTER)
            
    #create guiding boxes for legend
    for i in range(2): 
        for r in range(3):
            boxRI = [(boxHeight+10)+160*r, (boardDimensionY/2 + 50*(i+1)), (boxHeight+10)+160*(r+1), (boardDimensionY/2) + 50*(i+2)]
            guideBoxes.append(boxRI)
    tileTitleGuide = [boxHeight+boxLength, boxHeight+(boxLength/4)]
    tileGuide = [boxHeight+boxLength-40, boxHeight+(boxLength/4) + 10]
    
    #initialise DICE 
    diceMid = []
    dice = []
    pips1 = []
    pips2 = []
    for i in range(2):
        diceMid.append([boxHeight+(3.5+i)*boxLength, boxHeight+(0.5+i)*boxLength])
    for i in diceMid:
        dice.append([i[0]-45, i[1]-45, i[0]+45, i[1]+45])
    for i in range(len(dice)):
        widg.create_rectangle(dice[i], outline = "white")
        if i == 0:
            pips = pips1
        else:
            pips = pips2
        for r in range(3):
            for n in range(3):
                x0 = dice[i][0]+ 13.5*(n+1) + 12*n
                y0 = dice[i][1]+ 13.5*(r+1) + 12*r
                pips.append([x0, y0, x0+12, y0+12])
        pips.pop(1)
        pips.pop(6)
        
    #initialise pips of first and second dice
    for i in pips1:
        dicePips1.append(widg.create_oval(i, fill = 'white', disabledfill = 'black', state = tkinter.DISABLED))
    
    for i in pips2:
        dicePips2.append(widg.create_oval(i, fill = 'white', disabledfill = 'black', state = tkinter.DISABLED))
    
    #initialise tokens and player guide
    for i in range(num_players): 
        playerIDs[i] = makeToken(playerPos[i], playerCols[i])
        nama = players[i].get_name()
        startingCash = players[i].get_sanity()
        
        legend = guideBoxes[i][0:2]
        for r in range(2):
            legend[r] += 10
            legend.append(legend[r]+30)
            
        widg.create_rectangle(legend, fill = playerCols[i])
        widg.create_text(legend[2]+3, legend[1], text = "{:6s}".format(nama), anchor = tkinter.NW, fill = "white")
        sanCounter.append(widg.create_text(legend[2]+3, legend[3], text = "Sanity: {:d}".format(startingCash), anchor = tkinter.SW, fill = "white"))
        
    #current tile checker initialisation
    widg.create_text(tileTitleGuide, text="Current Tile", fill = 'white')
    global guide
    guide = widg.create_text(tileGuide, text = "Name:\nOwner:\nLevel:\nRent:", anchor = tkinter.NW, fill = 'white')
        
    widg.pack() #Geometry setter

def update_board(myTurn, d1, d2):
    for key in priceIDs:
        owner = tiles[key].get_building().get_owner()
        if owner == None:
            owner = "---"
        else:
            owner = players[owner].get_name()
        widg.itemconfigure(priceIDs[key], text = int(tiles[key].get_building().get_rent()))
        widg.itemconfigure(ownedIDs[key], text = owner)
    for key in playerIDs:
        position = players[key].get_position()
        status = players[key].get_status()
        pos = playerPos[key].copy()
        san = int(players[key].get_sanity())
        if status == 'Bankrupt':
            widg.delete(playerIDs[key])
            playerIDs.pop(key)
            san = "BANKRUPT!"
        elif status == 'Jail':
            pos = inJail[key].copy()
            widg.moveto(playerIDs[key], pos[0]-10, pos[1]-10)
        else:
            if position == 0:
                pass
            elif position > 0 and position < 6:
                pos[0] -= (position-1)*boxLength + boxHeight + 7.5
            elif position == 6:
                pos = justVisiting[key].copy() #placeholder for jail
            elif position > 6 and position <= 12:
                pos[0] -= 5*boxLength + boxHeight + 30
                pos[1] -= (position-7)*boxLength + boxHeight -7.5
            elif position > 12 and position < 18:
                pos[0] -= (17 - position)*boxLength + boxHeight
                pos[1] -= 5*boxLength + boxHeight + 30
            elif position == 18:
                pos = inJail[key].copy() #placeholder for Jail
            elif position > 18:
                pos[1] -= (23 - position)*boxLength + boxHeight + 15
            widg.moveto(playerIDs[key], pos[0]-10, pos[1]-10)
        
        widg.itemconfigure(sanCounter[key], text = "Sanity: {}".format(san))
        building_of_note = players[myTurn].get_position()
        if building_of_note in building_pos:
            b = tiles[building_of_note].get_building()
            own = b.get_owner()
            if own == None:
                own = "---"
            else:
                own = players[own].get_name()   
            tileData = "Name: {}\nOwner: {}\nLevel: {}\nRent: {}".format(b.get_name(), own, b.get_level(), b.get_rent())
        else:
            tileData = "Name:\nOwner:\nLevel:\nRent:"
        widg.itemconfigure(guide, text = tileData)
        
        #display dice roll
        setDice(d1, dicePips1)
        setDice(d2, dicePips2)
    return
    pass

def avg(coordLs, xy):
    if xy == "x":
        mean = (coordLs[0]+coordLs[2])/2
    elif xy == 'y':
        mean = (coordLs[1]+coordLs[3])/2
    else:
        return None
    return mean

def makeToken(startPos, colour):
    coords = [startPos[0]+10, startPos[1]+10, startPos[0]-10, startPos[1]-10]
    token = widg.create_rectangle(coords, fill=colour, outline = colour)
    return token    

def getProperties(coord, ori, thisId):
    
    centre = [avg(coord, 'x'), avg(coord, 'y')]
    smolBox = coord.copy()
    if(type(ori) is int): #Normal tile (not corner)
        smolBox[ori] += ((-1)**(ori < 0))*smolBoxHt
        namePos = [avg(smolBox, 'x') , avg(smolBox, 'y')]
        textRot = rot[ori]
        
        if (ori%2 == 0):
            bottom = [((-1)**(ori < 0))*10+coord[ori], avg(coord, 'y')]
            ownerPos = [((-1)**(ori >= 0))*30+namePos[0], namePos[1]]
        else:
            bottom = [avg(coord, 'x'), ((-1)**(ori < 0))*10+coord[ori]]
            ownerPos = [namePos[0], ((-1)**(ori >= 0))*30+namePos[1]]
    else: #If it's a corner
        smolBox[-1] -= boxHeight-smolBoxHt
        smolBox[0] += boxHeight-smolBoxHt
        bottom = None
        textRot = None
        namePos = [avg(smolBox, 'x') , avg(smolBox, 'y')]
        ownerPos = None
    return (thisId, smolBox, centre, bottom, namePos, ownerPos, textRot) 

def setDice(roll, pips):
    dMap = diceMaps[roll-1]
    for pip in range(len(dMap)):
        if dMap[pip] == 1:
            widg.itemconfigure(pips[pip], state = tkinter.NORMAL)
        else:
            widg.itemconfigure(pips[pip], state = tkinter.DISABLED)
#Run the game
game()
