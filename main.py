from init import deal_cards, draw_pile
from cards_def import Number
import random
from game_loop import start_game

# Dunno
# Vojtěch Klhůfek, I. ročník
# zimní semestr 2022/23
# NPRG030


def main():
    deal_cards()

    starting_card = draw_pile.pop(0)    # the card that will be considered as the top of the discard pile

    # if the starting card is a queen, we generate a random suit for that card,
    # since queens are implemented without a suit
    if starting_card[0] == Number.queen():
        starting_card = (starting_card[0], random.randint(1, 4))

    start_game(starting_card)


main()
