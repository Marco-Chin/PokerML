import PokerGame
import logging

import Constants

logging.basicConfig(level=Constants.LOGGING_LEVEL)

poker_game = PokerGame.HeadsUpHumanVsComputerPokerGame()
poker_game.round()
me = poker_game.players[0]

