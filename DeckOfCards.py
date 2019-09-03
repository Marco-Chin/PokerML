from random import randint
import logging
import pygame as pg

import Constants


logging.basicConfig(level=Constants.LOGGING_LEVEL)


class Card:
    def __init__(self, suit=Constants.CardSuits.SPADES, value=Constants.CardValues.ACE):
        self.suit = suit
        self.value = value

        self.sprite = self.get_sprite()

    def __eq__(self, other):
        if not isinstance(other, Card):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.suit == other.suit and self.value == other.value

    def get_card_info(self):
        return f'{self.value.values[0]} of {self.suit.values[0]}'

    def get_sprite(self) -> pg.Surface:
        return pg.image.load(self.get_pygame_sprite_file_name())

    def get_pygame_sprite_file_name(self):
        return f'{Constants.PygameConstants.IMAGE_SOURCE_PATH}{self.value.values[1]}_of_{self.suit.values[1]}.png'

    def print_card(self):
        logging.info(self.get_card_info())


class Deck:
    def __init__(self):
        self.deck = self.__init_deck()

    @staticmethod
    def __init_deck():
        constructed_deck = []

        for suit in Constants.CardSuits:
            for value in Constants.CardValues:
                constructed_deck.append(Card(suit, value))

        return constructed_deck

    def shuffle(self):
        for idx in range(len(self.deck)):
            self.__swap_card_to_random_pos_in_deck(idx)

    def __swap_card_to_random_pos_in_deck(self, p1):
        random_pos = randint(0, len(self.deck)-1)
        self.deck[p1], self.deck[random_pos] = self.deck[random_pos], self.deck[p1]

    def deal_card(self):
        return self.deck.pop()

    def print_deck(self):
        for card in self.deck:
            card.print_card()

    def validate_deck(self):
        valid_deck = Deck().deck

        if len(valid_deck) != len(self.deck):
            return False

        for valid_card in valid_deck:
            is_valid_card_in_deck = False
            for card in self.deck:
                if valid_card.__eq__(card):
                    is_valid_card_in_deck = True
            if not is_valid_card_in_deck:
                return False

        return True

