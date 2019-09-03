from Dealer import Dealer
from Player import *
import Constants

import logging
from random import randint

logging.basicConfig(level=Constants.LOGGING_LEVEL)


class PokerGame:
    def __init__(self, players):
        if len(players) <= 1:
            raise Exception('Players must be of length 2 or more')

        self.players = players
        self.player_count = len(players)
        self.dealer = Dealer()
        self.dealer_position_idx = self.__get_random_player_idx()
        self.hand_phase = Constants.HandPhases.PRE_FLOP
        self.pot = 0

    def __get_random_player_idx(self):
        random_player_idx = randint(0, self.player_count-1)
        logging.debug(f'Setting {self.players[random_player_idx].name} to dealer')
        return randint(0, self.player_count-1)

    def round(self):
        self.pre_flop()

        self.print_state()

    def pre_flop(self):
        self.hand_phase = Constants.HandPhases.PRE_FLOP
        self.__deal_cards()

    def __deal_cards(self):
        self.dealer.deck.shuffle()

        for _ in range(Constants.HOLDEM_HAND_SIZE):
            left_of_dealer_idx = self.dealer_position_idx+1 if self.dealer_position_idx+1 <= self.player_count-1 else 0

            current_player_idx = left_of_dealer_idx

            for _ in range(self.player_count):
                current_player = self.players[current_player_idx]
                card_to_receive = self.dealer.deck.deal_card()

                logging.debug(f'Dealing {card_to_receive.get_card_info()} to {current_player.name}')
                current_player.receive_card(card_to_receive)

                current_player_idx = current_player_idx+1 if current_player_idx+1 <= self.player_count-1 else 0

    def print_state(self):
        logging.info(f'Dealer: {self.players[self.dealer_position_idx].name}')

        for player in self.players:
            player.print_state()


class HeadsUpHumanVsComputerPokerGame(PokerGame):
    def __init__(self):
        human_player = HumanPlayer('Marco', 100)
        bot_player = BotPlayer('Bot', 100)

        super().__init__([human_player, bot_player])

