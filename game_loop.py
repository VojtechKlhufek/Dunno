from init import player_hand, bot1_hand, bot2_hand, draw_pile
from cards_def import Number, Suit, offensive_cards
from os import system, name
from time import sleep
from termcolor import colored

mandatory_draw_val = 0  # The number of cards the following player will have to draw.
ace_effect = False  # Says if the next player will be under the effect of an ace.
direction = "Clockwise"  # Says which direction the game goes.

player_hand_color = "light_magenta"


# Prints the user interface
def announcer(turn, last_card):
    global mandatory_draw_val, direction
    clear()
    if mandatory_draw_val > 0:
        print(colored(f"mandatory draw value: {mandatory_draw_val}", "light_red"))
    else:
        print(colored(f"mandatory draw value: {mandatory_draw_val}", "light_blue"))
    if direction:
        print(colored(f"direction is {direction}", "light_blue"))
    else:
        print(colored(f"direction is {direction}", "light_red"))
    print(colored(f"Card counts: Player = {len(player_hand)}, Bot1 = {len(bot1_hand)}, Bot2 = {len(bot2_hand)}",
                  "light_blue"))
    print(colored(f"\nPlayer hand: ", player_hand_color))
    last_card_string = print_player_hand(last_card)
    print()
    print(colored(f"{turn} turn!", "light_green"))
    print(colored(f"last card was {last_card_string}", "light_green"))
    if turn != "Player":
        print(colored("Press enter to progress...", "light_grey"))


# Prints the players hand and at the same time creates a string for the last played card.
def print_player_hand(last_card):
    list_of_tens = []  # Will be used to align the guiding numbers under 10s
    player_hand.append(last_card)  # This is done to easily format the last_card, it will be popped at the end.
    for i in range(0, len(player_hand)):

        number = player_hand[i][0]
        suit = player_hand[i][1]

        if number == 11:
            num = "J"
        elif number == 12:
            num = "Q"
        elif number == 13:
            num = "K"
        elif number == 14:
            num = "A"
        elif number == 0:
            num = "J"
        else:
            num = number
        if num == 10:
            list_of_tens.append(i + 1)

        if suit == Suit.clubs():
            symbol = "♣"
        elif suit == Suit.diamonds():
            symbol = "♦"
        elif suit == Suit.hearts():
            symbol = "♥"
        elif suit == Suit.spades():
            symbol = "♠"
        else:
            symbol = "$"
        if i != len(player_hand) - 1:
            print(colored(str(num) + symbol, player_hand_color), end=" ")
        else:
            player_hand[i] = str(num) + symbol
    print()

    # Prints the guiding numbers under players cards.
    for i in range(1, len(player_hand)):
        # Fixes the position of numbers >= 10
        if i >= 10:
            end_space = " "
        else:
            end_space = "  "
        # Fixes the position of numbers under cards, that have the number 10.
        if list(filter((lambda x: x == i), list_of_tens)):
            print(colored(f"{i}", "light_grey"), end=end_space + " ")
        else:
            print(colored(i, "light_grey"), end=end_space)
    print()
    return player_hand.pop()


def start_game(last_card):
    global ace_effect

    last_player = "bot2"

    while True:
        # starts players turn
        if (direction == "Clockwise" and last_player == "bot2") or \
                (direction == "Counter-clockwise" and last_player == "bot1"):
            last_player = "player"
            player_hand.sort(key=lambda x: (x[1], x[0]), reverse=True) # Sorts the players hand
            announcer("Player", last_card)

            if not ace_effect:
                last_card = player_turn(last_card)
            else:
                perform_ace_effect()

        # starts bot1s turn
        if (direction == "Clockwise" and last_player == "player") or \
                (direction == "Counter-clockwise" and last_player == "bot2"):
            last_player = "bot1"
            announcer("Bot1", last_card)

            input()

            if not ace_effect:
                last_card = bot_turn(bot1_hand, 1, last_card, 1)
            else:
                perform_ace_effect()

        # starts bot2s turn
        if (direction == "Clockwise" and last_player == "bot1") or \
                (direction == "Counter-clockwise" and last_player == "player"):
            last_player = "bot2"
            announcer("Bot2", last_card)
            input()

            if not ace_effect:
                last_card = bot_turn(bot2_hand, 1, last_card, 2)
            else:
                perform_ace_effect()


def perform_ace_effect():
    global ace_effect
    print(colored("Ace!", "red"))
    sleep(2)
    ace_effect = False


def player_turn(last_card):
    global mandatory_draw_val
    if not player_hand and mandatory_draw_val == 0:
        print(colored("Player wins!", "light_green"))
        exit()

    # Theoretically it is possible to reach recursion error, by inputting an invalid input around 1000 times,
    # but it takes a long time to reach and is only really possible, if the user is really trying to reach it.

    try:
        if player_hand:
            print(colored(f"Select cards by typing numbers from 1 to {len(player_hand)}, or 0 to draw", "light_grey"))
        else:
            print(colored(f"Type 0 to draw", "light_grey"))

        played_card_pos = input().split()

        played_card_pos = list(map((lambda x: int(x)), played_card_pos))

        if played_card_pos[0] <= 0:

            draw_cards(player_hand)
            player_hand.sort(key=lambda x: (x[1], x[0]), reverse=True)
            return last_card

        first_card = player_hand[played_card_pos[0] - 1]

        multi_chosen_cards_check = list(filter((lambda x: player_hand[x - 1][0] != first_card[0]), played_card_pos))
        is_only_one_jack = first_card[0] == Number.jack() and len(played_card_pos) > 1

        same_num_or_suit_check = first_card[1] == last_card[1] or first_card[0] == last_card[0]
        no_suit_check = last_card[1] == Suit.none() or last_card[0] == Number.joker() or first_card[1] == Suit.none()

        # checks if all the chosen cards have the same number as the first one and if there aren't multiple Jacks
        if multi_chosen_cards_check or is_only_one_jack:
            raise IndexError

        # checks if the first chosen card can be legally played
        elif not (same_num_or_suit_check or no_suit_check):
            raise IndexError

        else:

            # makes a list of selected cards (instead of positions)
            played_card_list = []
            for pos in played_card_pos:
                played_card_list.append(player_hand[pos - 1])

            card_check = played_card_list[0]
            is_not_offensive = {card_check}.isdisjoint(offensive_cards)
            three_bool = not ((card_check[0] == Number.three()) and (last_card[0] != Number.joker()))

            # checks if the played card(s) defends against mandatory drawing
            if mandatory_draw_val > 0 and three_bool:
                # checks if the played card has the same value as mandatory_draw_val while being a 10 or lower
                if mandatory_draw_val == card_check[0] and card_check[0] <= 10 and is_not_offensive:
                    mandatory_draw_val = 0
                # if the played card didn't pass the previous conditions, and it isn't offensive,
                # the played card is unplayable
                elif is_not_offensive:
                    raise MandatoryDraw

            # removes played cards from players hand and places them on the bottom of the draw pile
            for card in played_card_list:
                player_hand.remove(card)
                draw_pile.append(card)

            # sets the last chosen card as the future last_card
            played_card = played_card_list[len(played_card_list) - 1]

            # if effect is not None it has the value of the newly selected color,
            # which is than assigned to the played card
            # (this does not affect the card, which was earlier placed at the bottom of the draw pile)
            effect = check_and_perform_effect(played_card_list, "player")
            if effect is not None:
                played_card = (played_card[0], effect)

        return played_card

    except UnicodeDecodeError:
        print(colored("Error.", "red"))
        print_player_hand(last_card)
        print()
        return player_turn(last_card)
    except IndexError:
        print(colored("Invalid card or cards.", "red"))
        print_player_hand(last_card)
        print()
        return player_turn(last_card)
    except ValueError:
        print(colored("Invalid input: Unknown symbol.", "red"))
        print_player_hand(last_card)
        print()
        return player_turn(last_card)
    except MandatoryDraw:
        print(colored("Invalid input: You have to draw.", "red"))
        print_player_hand(last_card)
        print()
        return player_turn(last_card)


def bot_turn(bot_hand, card_pos, last_card, bot_num):
    global mandatory_draw_val
    if not bot_hand and mandatory_draw_val == 0:
        print(colored(f"Bot{bot_num} wins!", "light_green"))
        exit()

    # draws a card if the bot has no playable card
    if card_pos > len(bot_hand):
        draw_cards(bot_hand)
        return last_card

    suit_check = (last_card[1] != bot_hand[card_pos - 1][1])
    num_check = (last_card[0] != bot_hand[card_pos - 1][0])
    no_suit_check = last_card[1] != 0 and bot_hand[card_pos - 1][1] != 0

    # checks cards one by one, until it finds a card, that can be played
    if no_suit_check and suit_check and num_check:
        return bot_turn(bot_hand, card_pos + 1, last_card, bot_num)

    else:

        played_card = bot_hand.pop(card_pos - 1)
        card_num = played_card[0]
        is_not_offensive = {played_card}.isdisjoint(offensive_cards)
        three_bool = not ((card_num == Number.three()) and (last_card[0] != Number.joker()))

        # checks if the bots chosen card defends against drawing
        if mandatory_draw_val > 0 and three_bool:
            if card_num == mandatory_draw_val and card_num <= 10 and is_not_offensive:
                mandatory_draw_val = 0
            elif is_not_offensive:
                bot_hand.insert(card_pos - 1, played_card)
                return bot_turn(bot_hand, card_pos + 1, last_card, bot_num)

        played_card_list = [played_card]
        draw_pile.append(played_card)

        # finds all cards with the same number as the played card and plays them too
        for card in bot_hand:
            if card[0] == played_card[0] and card[0] != Number.jack():
                played_card = card
                played_card_list.append(card)

        f = played_card_list.pop(0)
        # removes all played cards form the bots hand and places them on the bottom of the draw pile
        for c in played_card_list:
            bot_hand.remove(c)
            draw_pile.append(c)

        played_card_list = [f] + played_card_list

        effect = check_and_perform_effect(played_card_list, f"bot{bot_num}")
        # same as in players turn
        if effect is not None:
            played_card = (played_card[0], effect)

    return played_card


# credit: https://www.tutorialspoint.com/how-to-clear-python-shell
# is used to clear the terminal
def clear():
    # for windows
    if name == 'nt':
        system('cls')

    # for mac and linux
    else:
        system('clear')


def draw_cards(hand):
    global mandatory_draw_val
    if mandatory_draw_val > 0:
        while True:
            if not draw_pile:
                mandatory_draw_val = 0
                return
            hand.append(draw_pile.pop(0))
            mandatory_draw_val -= 1
            if mandatory_draw_val < 1:
                return
    else:
        if not draw_pile:
            return
        hand.append(draw_pile.pop(0))
        return


def check_and_perform_effect(played_card_list, player):
    global mandatory_draw_val, ace_effect, direction
    amount_of_cards = len(played_card_list)
    card_on_top = played_card_list[amount_of_cards - 1]

    # 2♣ = draw 1
    if card_on_top == (Number.two(), Suit.clubs()):
        mandatory_draw_val += 1
    # 7 = draw 2
    elif card_on_top[0] == Number.seven():
        mandatory_draw_val += (2 * amount_of_cards)
    # J = swap hands with another player, J♦ = J + you can throw away 2 cards
    elif card_on_top[0] == Number.jack():
        if card_on_top[1] == Suit.diamonds():
            throw_away(player)
        swap_hands(player)
    # Q = choose a new suit and switch direction
    elif card_on_top[0] == Number.queen():
        direction = not direction
        return choose_suit(player)
    # K = draw 3 and choose a new suit
    elif card_on_top[0] == Number.king():
        mandatory_draw_val += (3 * amount_of_cards)
        return choose_suit(player)
    # do not play for 1 turn
    elif card_on_top[0] == Number.ace():
        ace_effect = True
    elif card_on_top[0] == Number.joker():
        mandatory_draw_val += (5 * amount_of_cards)
    return None


# a function for J♦ special effect
def throw_away(player):
    try:
        if player == "player":
            if not player_hand:
                return
            print_player_hand((0, 0))

            print(colored(f"\nChoose at most 2 cards to throw away", "light_grey"))
            print(colored(f"Select cards by typing numbers from 1 to {len(player_hand)} "
                          f"or press Enter if you do not wish to throw away any cards", "light_grey"))

            cards = input().split()
            if not cards:
                return
            cards = list(map((lambda x: int(x)), cards))
            played_card_list = []
            for pos in cards:
                played_card_list.append(player_hand[pos - 1])
            for card in played_card_list:
                player_hand.remove(card)
                draw_pile.append(card)
        elif player == "bot1":
            bot_throw_away(bot1_hand)
        else:
            bot_throw_away(bot2_hand)
    except IndexError:
        print(colored("Invalid input.", "red"))
        throw_away(player)


def bot_throw_away(bot_hand):
    has_jacks = list(filter((lambda x: x[0] == Number.jack()), bot_hand))
    has_offensive = list(filter((lambda x: list(filter((lambda y: y == x), offensive_cards)) != []), bot_hand))
    cards_to_throw = has_jacks + has_offensive
    if len(cards_to_throw) >= 2:
        while len(cards_to_throw) > 2:
            cards_to_throw.pop(len(cards_to_throw) - 1)
        for card in cards_to_throw:
            bot_hand.remove(card)
            draw_pile.append(card)


def swap_hands(player):
    global player_hand, bot1_hand, bot2_hand
    # any time 2 players have no cards at the same time, whoever played a J cannot switch cards with anyone
    if (player_hand == [] and bot1_hand == []) or (player_hand == [] and bot2_hand == []) or (
            bot1_hand == [] and bot2_hand == []):
        return
    else:
        try:
            if player == "player":
                if not player_hand:
                    return
                print(colored("Choose a player to swap hands with (1=bot1,2=bot2):", "light_grey"))

                whom = int(input())
                if whom > 2:
                    raise InvalidPlayerNumber
                if whom == 1:
                    if not bot1_hand:
                        raise InvalidPlayerCardCount
                    player_hand, bot1_hand = bot1_hand, player_hand
                else:
                    if not bot2_hand:
                        raise InvalidPlayerCardCount
                    player_hand, bot2_hand = bot2_hand, player_hand

            elif player == "bot1":
                if not bot1_hand:
                    return
                if len(player_hand) < len(bot2_hand) and player_hand != []:
                    bot1_hand, player_hand = player_hand, bot1_hand
                else:
                    bot1_hand, bot2_hand = bot2_hand, bot1_hand

            elif player == "bot2":
                if not bot2_hand:
                    return
                if len(player_hand) < len(bot1_hand) and player_hand != []:
                    bot2_hand, player_hand = player_hand, bot2_hand
                else:
                    bot2_hand, bot1_hand = bot1_hand, bot2_hand

        except ValueError:
            print(colored("Invalid input.", "red"))
            return swap_hands("player")
        except InvalidPlayerCardCount:
            print(colored("You have to pick a player with at least 1 card!", "red"))
            return swap_hands("player")
        except InvalidPlayerNumber:
            print(colored("Invalid input.", "red"))
            return swap_hands("player")


# lets player choose a new suit
def choose_suit(player):
    try:
        if player == "player":
            print(colored("Select a new suit (1=♣,2=♦,3=♥,4=♠):", "light_grey"))
            new_suit = int(input())
            if 1 > new_suit or new_suit > 4:
                raise InvalidSuit
            return new_suit

        elif player == "bot1":
            return bot_choose_suit(bot1_hand)
        else:
            return bot_choose_suit(bot2_hand)

    except InvalidSuit:
        print(colored("Invalid suit.", "red"))
        return choose_suit("player")
    except ValueError:
        print(colored("Invalid input.", "red"))
        return choose_suit("player")


# chooses a bots longest suit
def bot_choose_suit(bot_hand):
    spades = len(list(filter((lambda x: x[1] == Suit.spades()), bot_hand)))
    hearts = len(list(filter((lambda x: x[1] == Suit.hearts()), bot_hand)))
    diamonds = len(list(filter((lambda x: x[1] == Suit.diamonds()), bot_hand)))
    clubs = len(list(filter((lambda x: x[1] == Suit.clubs()), bot_hand)))
    longest = max(spades, hearts, diamonds, clubs)
    if longest == spades:
        return Suit.spades()
    elif longest == hearts:
        return Suit.hearts()
    elif longest == diamonds:
        return Suit.diamonds()
    else:
        return Suit.clubs()


class InvalidPlayerCardCount(Exception):
    pass


class InvalidPlayerNumber(Exception):
    pass


class InvalidSuit(Exception):
    pass


class MandatoryDraw(Exception):
    pass
