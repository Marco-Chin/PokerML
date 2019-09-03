from DeckOfCards import Card


class PlayerState:
    def __init__(self, stack, bet_amount, hand, in_hand, is_dealer):
        self.stack = stack
        self.bet_amount = bet_amount
        self.hand: [Card] = hand
        self.in_hand = in_hand
        self.is_dealer = is_dealer

