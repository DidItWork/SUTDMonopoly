# SUTDMonopoly

## Introduction

**SUTDMonopoly** is a multiplayer text-based game based on the board game "Monopoly". It operates on two windows — one for display, and another for taking user inputs. We adopted and modified most of the original game features (<find citation later>) and incorporated characteristics that are unique to SUTD. 

The rules in this variant are similar to "Monopoly". As with Monopoly, this game is meant to be a multiplayer game played between 2 to 5 players. For each turn, the players will roll **2** dices to move their pieces around the board. Upon landing on different tile sets, there will be different events for the users. The objective of the game still holds, which is to force opponents into bankruptcy by buying and upgrading their properties. 

### Rules

Each player will start with an initial amount of 200 sanity. Two dices will be thrown and their pieces will be moved anti-clockwise around the board from the "Home" tile according to the sum of the dice thrown. By throwing a double, the player will be entitled to throw again. A maximum of 3 doubles are allowed to balance out any RNGs. Every time player passes “Home”, he/she will receive an additional 150 sanity.

Upon landing on an unclaimed property tile, they can choose to purchase the property for a predetermined amount of "Sanity". Any subsequent players landing on this tile will have to transfer a predetermined amount of "Sanity" to the owner of the tile. In the case when the owner lands on his own property, he would be allowed to upgrade the building up to a level of 3.
 
Upon landing on a chance tile, the player will automatically draw a chance card that will have random positive or negative effects. Upon landing on a "Tax" tile, the player would be required to pay the stipulated tax associated to it. Landing on the "Go To Jail" tile will cause the player to be jailed for his next 3 turns.

The "Jail" and "Free Parking" tile has no effect other than printing a text.

The game ends when all other players, except the winner, turns “crazy for studying too hard’, i.e., lost all their ‘Sanity’

### Properties

In the original Monopoly, most of the properties are classified into sets of 3. Ownership of properties from the same set would automatically increase its base rent. 

However, due to board space constraints, we modified all the properties to be in sets of 2. For the sake of simplicity and gameplay, ownership of properties from the same set would not automatically increase its base rent. 

### Chance

In this variant of Monoply, there will be a total of 20 chance cards, with 4 primary effects such as gaining "sanity", "losing "sanity", going to jail, and losing a property. The chance cards will be drawn by deck and will not be repeated until the deck is fully depleted, which then, it will be reshuffled.

### Jail

If jailed, the player will be jailed for his next 3 turns. A player would also have the chance to break out of jail early if he manages to roll a double during his turn.

### Winning condition

As with Monopoly, pLayers are allowed to sell their properties to stay "Alive" and continue playing the game. However, the players are eliminated when they run out of currency, "Sanity" and properties to sell. The game ends when all other players, except the winner, turns “crazy for studying too hard’, i.e., lost all their ‘Sanity’. The winner will be announced in text and the terminal exits after entering 'end'.

### Dependencies:

- tkinter
- random

## How to play

1. Ensure that your python is of at least version 3.8 for tkinter to work.

2. Open power shell (Win X + A) or any of your favorite terminal or Anaconda Prompt.

   ```bash
   # Move to the project directory.
   $ cd </project/folder>
   # Run the game.
   $ python ./SUTDMonopoly.py
   ```
   
3. Upon launching the game, set the terminal to be on the right side of your screen and the tkinter window to be on the right side of the screen. The game should look something like this

![Example](https://imgur.com/a/mO9xhUw)
   
## Documentation

### 

### UI Functions
These functions help translate the game data in the program to graphics in the Tk() window.

#### avg( CoordLs: [x1,y1,x2,y2], xy: str)
> Finds the average of x or y coordinates of two extreme corners of a rectangle in the User Interface (UI) dpending on the value of xy

**Parameters**:
* **CoordLs**— a list of values corresponding to the coordinates of the top left corner (x1, y1) and bottom right corner (x2, y2) of a rectangle in the UI
* **xy**— a string containing 'x' or 'y'

**Returns:** The mean of x1 and x2, or y1 and y2, depending on whether the value **xy** passed was 'x' or 'y' respectively

#### getProperties(coord: [x1,y1,x2,y2], ori: int or str, thisId: int)
>  Returns several key coordinates and rotation angles for the components of the tile with the coordinates represented in **coord**

**Parameters**:
* **coord**— a list of values corresponding to the coordinates of the top left corner (x1, y1) and bottom right corner (x2, y2) of a rectangle in the UI representing a tile on the board
* **ori**— an index corresponding to the rotation of the tile, or a string to indicate that it is a corner
* **thisId**— the integer ID of the rectangle assigned by the tkinter.Canvas() object

**Returns:** A tuple with contents: (thisId, smolBox, centre, bottom, namePos, ownerPos, textRot)
* **thisId**— the integer ID of the rectangle assigned by the tkinter.Canvas() object
* **smolbox**— a list of values corresponding to the coordinates of the top left corner (x1, y1) and bottom right corner (x2, y2) of the small coloured rectangle located at the top of the tile for rectangluar tiles, and those of a square occupying the top right corner of the tile for corner tiles
* **centre**— a list containing the x and y value of the centre of the tile
* **namePos**— a list containing the x and y value to which the text object displaying "chance" or property name will be anchored to on a rectangular tile
* **ownerPos**— a list containing the x and y value to which the text object displaying the owner of the property will be anchored to on a property tile
* **textRot**— the angle (in degrees) at which the text objects should be rotated

#### setDice(roll: int, pips: list())
> Changes the state of the seven pips (tkinter.canvas oval objects) in one of the displayed dice on the UI to display the number rolled by the player. Setting the oval object's state to tkinter.DISABLED turns it black, causing it to "disappear" against the black background, while setting the object's state to tkinter.NORMAL causes it to turn white. 

**Parameters**:
* **roll**— the number rolled by the player
* **pips**— a list containing all the IDs assigned to each oval object in the tkinter.Canvas() object representing a pip 

**Returns:** None

#### initUI()
> Initialises the UI. Instantiates the canvas, tiles, dice, player tokens, various text objects and reflects the initial state of the board and player sanity count

**Returns:** None

#### update_UI(\*args)
> Updates the UI with the latest game information. If supplied with optional parameters, will also update player turn, dice rolls and the name of any property the active player has landed on

**Parameters:**
* **\*args**— accepts up to 3 arguments, **player_id**, **dice1** and **dice2**, and reflects the current property tile and current player's turn on the UI, and updated dice roll,  respectively

**Returns:** None

Special thanks to Tim for not sleeping and CS for raging during debugging.
