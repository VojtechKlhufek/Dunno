#Dunno - Rules of the game

##What is Dunno?

Dunno is a card game based on mau-mau. It is played with a 54-card deck (standard 52 cards + 2 Jokers).

##UI

*mandatory draw value* - The value, the current player has to draw, unless they have a card, which can defend them.

*direction* - The direction in which the game goes. For *Clockwise* the game goes *Player -> Bot1 -> Bot2 -> Player*, for *Counter-clockwise* *Player -> Bot2 -> Bot1 -> Player*

*Card counts* - Shows the number of cards in each players hand.

*Player hand* - On the next line are shown cards in the players hand, and under each card is a guiding number, which makes it easier to choose cards to play.

*... turn!* - Says whose ture it is.

*last card* - Shows the last played card.

The last line is a hint, that says, what the player has to do now.

##The course of the game

The game always starts with the user-controlled players turn. At the begining, the direction is *closkwise*. The player can play multiple cards at once, if the cards have the same number (with the exception of Jacks), and the first chosen card has to match the number or the suit of the last played card (if both of them actually have a suit). Suitless cards are considered Jokers and Queens, though Queens are only considered suitless, while in a players hand. The last chosen card will be the future last played card for the next players turn.
During a bots turn, the user is required to press Enter key to progress. This is so it is easier to keep up with the game.

##Controlls

The player chooses cards to play by typing the position of the desired card in the terminal. To make this easier, under each card is a guiding number, which shows the position of the card above. They can select multiple cards to play by typing a sequence of these numbers. The numbers in this sequence are separated by a space and every input has to be confirmed by pressing Enter. If the player has no cards, that can be played or they do not wish to play any card, they can also type "0" to draw a card (or multiple cards, if the mandatory draw value is greater than 1).
For example, if the player wanted to play cards on positions  1, 2 and 3, so that 1 is the card with the same suit as the last played card and 3 is the card, which is to be considered the future last played card, the input would look like this: 1 2 3 *Enter*

##End of the game

The winner is the player, that has no cards in their hand, when their turn starts, and at the same time does not have to draw any cards.

##Special card effects

The effects of offensive cards stack. That means, if one were to play for example 3 sevens at once, the following player would have to draw 6 cards. Also offensive cards can always be defended against. That means one can play an offensive or defensive card of the same number or suit. In case of a defensive card, mandatory draw value is set to 0 and no-one has to draw anything. In case of an offensive card, the following player has to draw the sum of all offensive cards, which were played.

###Ace

If one plays an Ace, the next player does not play for one turn. This effect does not stack and cannot be defended against by playing another Ace.

###Two of clubs (offensive card)

The next player draws 1 card

###Threes (offensive card)

If the played has to draw, they can play a three of the last cards suit. (This is not the case for Jokers!). This card adds no mandatory draw value, but it shifts the obligation to draw to the next player.

###Sevens (offensive card)

The next player draws 2 cards.

###Jacks

If one plays a Jack, they have to swap their hands with a player of their choice. Both of the players swapping their hands have to have at least 1 card. If the Jack was the players last card or all other players have no cards, they cannot swap their hand with anyone. This card can only be played alone (this means that you cannot play multiple Jacks at once). 

###Jack of diamonds

When playing this card, the player can choose to get rid of at most two cards (these can be even other Jacks). This is done before swapping hands with another player.

###Queens

This card can be played regardless of the last cards suit. If this card is played, the player has to choose a new suit and the game will continue as if the queen had that suit. The color is chosen by typing a number 1 through 4 when prompted, with the suits in relation to the numbers being clubs, diamonds, hearts and spades. The game direction will also be switched.

###Kings (offensive card)

The player has to choose a new color. The next player draws 3 cards.

###Jokers

The next player draws 5 cards. This card is suitless and cannot be defended against using a 3.

###2 (except 2 of clubs), 4, 5, 6, 8, 9, 10 (defensive cards)

If the player has to draw cards, they can play a defensive card, which has the last cards suit and the number of this card is the same as the mandatory draw value.

