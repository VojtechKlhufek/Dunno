# Dunno - Code documentation

## What is this project about?

Dunno is a card game based on mau-mau and created by me and Vojtěch Novotný. This is an electronic adaptation to this game and is made to be played by one player and two bots. The rules of the game are specified in the User documentation.

## Used libraries

In this project, I tried not to rely on many libraries, so I only use a couple, mostly for some simple tasks, which would be difficult without them. Firstly my project uses random, to shuffle the cards and also pick a random color, in case the starting card is a queen. Another one is os, which is used only to determine the way to clear the terminal, since a different command is used on Windows and Linux based operating systems. Then I use time, from which I use a sleep function to make a short break after an ace effect is applied and the last one is termcolor, to change the color of the text in the terminal.

I was also hoping to use some library to make a GUI and was considering using pygame, since it seemed like the easiest way to do it, but I did not have enough time for that at the end.

## Bot algorithm

The bots are quite simple. They always have their cards in the order they drew them and try to play them in order and when they find a card, which can be played, they play it. If they play a card with an effect which needs a choice to be made, the bot has some algorithms to make these choices.

For a Jack, the bots always pick the player with less cards. In the case of both of the other players having the same amount of cards, they prefer to swap hands with the player. This may not be the best way to do it, but I thought it made it a little more interesting for the player. Another idea was to make them pick on random in this case. It also could have been nice if they were able to decide, when it is better to try to play the Jack as the last card and when to swap.

For a Jack of diamonds, they try to throw away other Jacks and then offensive cards, if they have none or have only 1, they do not throw away any other cards. I think this is a good way to do it, since as a player, it is usually the best strategy, but if throwing away two cards would mean a victory, they should also do it.

For a queen or a king, the bots always pick their shortest color. Again it would have been nice, if they only played queens when they needed.

## Modules and main data structures

The game is split into 4 modules, main.py, game_loop.py, init.py and cards_def.py. I decided to split it like this at the begining, because I thought it would make it easier to find the most important things. main.py is used to call the function deal_cards() from the init.py module, which deals cards to each player, and then main.py calls the start_game() from the game_loop.py module, which starts the game itself. The last module, called cards_def.py. In this module I defined all the cards and put them in a "deck" which I then shuffled.

Having init.py separated was especially helpful when testing the game, because it provided an easy way of changing the starting amount of cards and also give any player any card at the start.

In cards_def.py are also 2 classes, called Number and Suit. These classes are used as enums, which I did not find in python, but I wanted all the cards to be represented by a tuple consisting of a number describing the cards own number and another number describing its suit and to make it a little more readable, I used these "enums" when checking for certain conditions.

The draw_pile is represented as a list, which is used as a queue, because a queue really nicely simulates a real deck of cards, since you draw from the top and in Dunno there is a rule which makes the cards go right at the bottom of the draw pile. Each players hand is also represented as a list.

## Conclusion

I think this project might have been a bit much for such a short time, but I am quite happy with how it went. There is still a couple rules missing which are in the original game, because they would have to work quite differently, since they mostly rely on the players being human, but I think that is not a huge problem. The game is playable and the bots usually do quite sensible things for their lack of intelligence. One thing that makes it a little dull in my opinion is the lack of GUI. It does not feel as if much is happening and it is quite easy to lose track of what the bots are doing (this is the main reason there is an input before each bots turn).
