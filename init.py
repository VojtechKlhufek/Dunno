from cards_def import draw_pile


player_hand = []
bot1_hand = []
bot2_hand = []


# Deals the cards the same way, one would deal real cards.
def deal_cards():
    global player_hand, bot1_hand, bot2_hand
    for i in range(0, 7):
        player_hand.append(draw_pile.pop(0))
        bot1_hand.append(draw_pile.pop(0))
        bot2_hand.append(draw_pile.pop(0))



