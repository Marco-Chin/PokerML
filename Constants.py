from enum import Enum
from aenum import MultiValueEnum
import logging
from PIL import Image


class CardSuits (MultiValueEnum):
    SPADES = 'Spades', 'spades'
    HEARTS = 'Hearts', 'hearts'
    CLUBS = 'Clubs', 'clubs'
    DIAMONDS = 'Diamonds', 'diamonds'


class CardValues (MultiValueEnum):
    ACE = 'Ace', 'ace'
    TWO = 'Two', 2
    THREE = 'Three', 3
    FOUR = 'Four', 4
    FIVE = 'Five', 5
    SIX = 'Six', 6
    SEVEN = 'Seven', 7
    EIGHT = 'Eight', 8
    NINE = 'Nine', 9
    TEN = 'Ten', 10
    JACK = 'Jack', 'jack'
    QUEEN = 'Queen', 'queen'
    KING = 'King', 'king'


DEFAULT_STACK = 100

DEFAULT_HUMAN_NAME = 'Mecro'
DEFAULT_BOT_NAME = 'John Doe'
HOLDEM_HAND_SIZE = 2


class PlayerActions (Enum):
    BET = 'Bet'
    CALL = 'Call'
    FOLD = 'Fold'


DEFAULT_PLAYER_INSTRUCTION = \
    f'{PlayerActions.BET.value}: \"{PlayerActions.BET.value}\" [amount]\n' \
    f'{PlayerActions.CALL.value}: \"{PlayerActions.CALL.value}\"\n' \
    f'{PlayerActions.FOLD.value}: \"{PlayerActions.FOLD.value}\"\n'

LOGGING_LEVEL = logging.DEBUG


class HandPhases (Enum):
    PRE_FLOP = 'Pre_Flop'
    FLOP = 'Flop'
    TURN = 'Turn'
    RIVER = 'River'


class PygameConstants:
    IMAGE_SOURCE_PATH = 'Resources/CardPngs/'

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    SCREEN_DIMENSIONS = (SCREEN_WIDTH, SCREEN_HEIGHT)

    CARD_PNG_SIZE = Image.open(f'{IMAGE_SOURCE_PATH}ace_of_spades.png').size
    CARD_HEIGHT = 100  # pixels
    CARD_WIDTH = int((CARD_PNG_SIZE[0] / CARD_PNG_SIZE[1]) * CARD_HEIGHT)
    CARD_DIMENSIONS = (CARD_WIDTH, CARD_HEIGHT)

    PLAYER_SURFACE_COLOR = (224, 156, 255)
    POKER_BG_SURFACE_COLOR = (114, 81, 245)




