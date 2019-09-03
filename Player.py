from abc import abstractmethod
import logging
import pygame as pg

import Constants
from Constants import PlayerActions as pa
from DeckOfCards import Card
from PlayerState import PlayerState


logging.basicConfig(level=Constants.LOGGING_LEVEL)


class Player:
    def __init__(self, name=Constants.DEFAULT_HUMAN_NAME, stack=Constants.DEFAULT_STACK):
        self.name = name
        self.stack = stack
        self.bet_amount = 0
        self.hand: [Card] = []
        self.in_hand = True
        self.is_dealer = False

        self.player_state_history: [PlayerState] = []

        self.pygame_surface = pg.Surface((100, 100))
        self.pygame_surface.fill(Constants.PygameConstants.PLAYER_SURFACE_COLOR)

    def receive_card(self, received_card):
        self.hand.append(received_card)

    def __print_stack(self):
        logging.info(f'{self.name}\'s stack: {self.stack}')

    def __print_hand(self):
        logging.info(f'{self.name}\'s hand:')

        for card in self.hand:
            card.print_card()

    def print_state(self):
        self.__print_stack()
        self.__print_hand()

    @abstractmethod
    def bet(self, poker_game):
        pass

    def call(self, poker_game, bet_size):
        player_bet = min(self.stack, bet_size)
        self.stack -= player_bet
        poker_game.pot += player_bet

    def fold(self):
        self.in_hand = False

    def __log_player_state(self):
        self.player_state_history.append(
            PlayerState(self.stack, self.bet_amount, self.hand, self.in_hand, self.is_dealer))


class HumanPlayer(Player):
    def __init__(self, name=Constants.DEFAULT_HUMAN_NAME, stack=Constants.DEFAULT_STACK):
        super().__init__(name, stack)

    def make_decision(self):
        while True:
            player_input = input(Constants.DEFAULT_PLAYER_INSTRUCTION)
            if self.__validate_player_input(player_input):
                logging.info("Was valid input")
                break

    @staticmethod
    def __validate_player_input(player_input):
        logging.info("Validating player input")

        input_tokens = player_input.split()
        player_action = input_tokens[0]

        valid_actions = [action.value for action in Constants.PlayerActions]

        input_length = len(input_tokens)

        if input_length == 1 or input_length == 2:
            if player_action in valid_actions:
                if (player_action == pa.CALL.value or player_action == pa.FOLD.value) and input_length == 1:
                    return True
                elif player_action == pa.BET.value and input_length == 2:
                    try:
                        bet_amount = input_tokens[1]
                        float(bet_amount)
                        return True
                    except ValueError:
                        logging.debug(f"Player action '{pa.BET.value}' requires a number following it")
                        return False
                else:
                    logging.debug(Constants.DEFAULT_PLAYER_INSTRUCTION)
                    return False
            else:
                logging.debug("Player action must be one of the following")
                for action in pa:
                    logging.debug(f"\'{action.value}\'")
                return False
        else:
            logging.debug(Constants.DEFAULT_PLAYER_INSTRUCTION)
            return False

    def get_pygame_surface(self):
        super().get_pygame_surface()


class BotPlayer(Player):
    def __init__(self, name=Constants.DEFAULT_BOT_NAME, stack=Constants.DEFAULT_STACK):
        super().__init__(name, stack)

    def bet(self, poker_game):
        self.decide_bet_amount

    def make_decision(self):
        pass

    def get_pygame_surface(self):
        super().get_pygame_surface()
