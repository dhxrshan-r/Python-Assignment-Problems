def add_cards(deck):
    if deck == []:
        return 0
    else:
        smaller_deck = deck[1:]
        partial_total = add_cards(smaller_deck)
        extra_card = deck[0]
        return extra_card + partial_total

print(add_cards([5, 2, 7, 3]))