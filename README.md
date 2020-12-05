# SUTDMonopoly

## Introduction

**SUTDMonopoly** is a multiplayer text-based game based on the board game "Monopoly". In this variant, the names of property, currency, and cards have been renamed to be SUTD related. The rules in this variant are similar to "Monopoly". As with Monopoly, players will roll **2** dices to move their pieces around the board from the Start, or "Go" tile. Upon landing on different tile sets, there will be different events for the user. The layout of the tile set will be of a 7x7 grid. This game has to be played between 2 and 5 players.

### Properties

Upon landing on an unclaimed property tile, the player can choose to purchase the property for a predetermined amount of "Sanity". Any subsequent players landing on this tile will have to transfer a predetermined amount of "Sanity" to the owner of the tile.

In the case when the owner lands on his own property, he would be allowed to upgrade the building up to a level of 3.

### Chance

Upon landing on the chance tile, the game will draw a card from the current deck that will have random effects ranging from gaining currency, losing currency, and jail. The drawn chance card will not be repeated until the deck is fully depleted, and then it will be reshuffled.

### Tax and Jail

Upon landing on the "Tax" Tile, the player would be required to pay the stipulated tax associated to it. 

Jail time has been set at 3 turns and players are allowed to roll a double to break out of jail.

### Winning condition

As with Monopoly, pLayers are allowed to sell their properties to stay "Alive" and continue playing the game. However, the players are eliminated when they run out of currency, "Sanity" and properties to sell. The game will carry on until there is only one player left, and the winner of the game will be announced.

### Dependencies:

- tkinter
- random

## How to play

1. Ensure that your python is of at least version 3.7 for tkinter to work.

2. Open power shell (Win X + A) or any of your favorite terminal or Anaconda Prompt.

   ```bash
   # Move to the project directory.
   $ cd </project/folder>
   # Run the game.
   $ python ./SUTDMonopoly.py
   ```
   
3. Upon launching the game, set the terminal to be on the right side of your screen and the tkinter window to be on the right side of the screen. The game should look somethign like this

<insert image>
   
## Documentation





Special thanks to Tim for not sleeping and CS for raging during debugging.
