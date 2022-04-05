from settings import width, height, block, OVER, JUMP, CONTINUE, MENU, window
from PlayF import game_
from startGame import startGame
from menu import Menu
import pygame


def main():
    # Init
    pygame.init()
    pygame.display.set_caption("BlockPuzzle")
    clock = pygame.time.Clock()

    # Window
    screen = pygame.display.set_mode((width * block, height * block))
    menu = Menu(screen)

    menu.createDataBase()
    menu.serialization()

    # Score
    lastScore = None
    colour = -255

    data = startGame(screen)
    game = MENU

    while True:
        if game in (CONTINUE, OVER):
            game = game_(data, game, abs(colour))

        elif game == JUMP:
            game = MENU
            lastScore = data.score[0]

            menu.setStartGame(MENU)
            menu.addInTable(lastScore)
            menu.addInDataBase(str(lastScore))

            data = startGame(screen)
        else:
            game = menu.on(lastScore, abs(colour))
            if game == CONTINUE:
                colour = -221

        if colour >= 220:
            colour = - 220
        elif colour + window[0] in (0, 1):
            colour = abs(colour)

        colour += 2

        pygame.display.update()
        clock.tick(50)


if __name__ == '__main__':
    main()
