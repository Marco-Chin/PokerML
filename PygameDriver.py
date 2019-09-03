# import the pygame module, so you can use it
import pygame as pg

import Constants
from DeckOfCards import Card
from Player import *
import PokerGame


def main():
    pg.init()

    pg.display.set_caption("minimal program")

    screen = pg.display.set_mode(Constants.PygameConstants.SCREEN_DIMENSIONS)

    test_card_surface = Card().get_sprite()

    test_card_surface = pg.transform.scale(test_card_surface, Constants.PygameConstants.CARD_DIMENSIONS)

    test_card_screen_pos = (0, 0)

    # define a variable to control the main loop
    running = True

    poker_game = PokerGame.HeadsUpHumanVsComputerPokerGame()
    poker_game.round()
    me: HumanPlayer = poker_game.players[0]

    screen.fill(Constants.PygameConstants.POKER_BG_SURFACE_COLOR)
    screen.blit(me.pygame_surface, (100, 100))
    # main loop
    while running:
        # screen.blit(test_card_surface, test_card_screen_pos)
        pg.display.flip()
        # event handling, gets all event from the event queue
        for event in pg.event.get():
            # only do something if the event is of type QUIT
            if event.type == pg.QUIT:
                # change the value to False, to exit the main loop
                running = False


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
