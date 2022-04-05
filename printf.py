import pygame


def printText(message, size, font_='fonts/Roboto.ttf', color=(0, 0, 0)):
    font_type = pygame.font.Font(font_, size, )
    text = font_type.render(message, True, color)

    return text, font_type.size(message)
