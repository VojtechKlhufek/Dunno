import random


class Number:
    @staticmethod
    def two():
        return 2

    @staticmethod
    def three():
        return 3

    @staticmethod
    def four():
        return 4

    @staticmethod
    def five():
        return 5

    @staticmethod
    def six():
        return 6

    @staticmethod
    def seven():
        return 7

    @staticmethod
    def eight():
        return 8

    @staticmethod
    def nine():
        return 9

    @staticmethod
    def ten():
        return 10

    @staticmethod
    def jack():
        return 11

    @staticmethod
    def queen():
        return 12

    @staticmethod
    def king():
        return 13

    @staticmethod
    def ace():
        return 14

    @staticmethod
    def joker():
        return 0


# Suit values are assigned by their value in Bridge card game.
class Suit:
    @staticmethod
    def clubs():
        return 1

    @staticmethod
    def diamonds():
        return 2

    @staticmethod
    def hearts():
        return 3

    @staticmethod
    def spades():
        return 4

    @staticmethod
    def none():
        return 0


# each card is a tuple of (Number, Color)

draw_pile = [(Number.joker(), Suit.none()), (Number.joker(), Suit.none())]

# Even though queens technically do have a color,
# in this game it doesn't play any role, so it is more convenient not to assign it at the beginning.
for i in range(4):
    draw_pile.append((Number.queen(), Suit.none()))

for n in range(2, 14 + 1):
    if n == 12:
        continue
    for c in range(1, 4 + 1):
        draw_pile.append((n, c))

random.shuffle(draw_pile)

offensive_cards = {(Number.two(), Suit.clubs()), (Number.joker(), Suit.none())}

for i in range(1, 4+1):
    offensive_cards.add((Number.seven(), i))
    offensive_cards.add((Number.king(), i))
