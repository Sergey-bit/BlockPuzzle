import pygame
from settings import block, f_width, f_height
from draw import Draw
from createShapes import createShapes


def startGame(screen: pygame.Surface):
    field = pygame.Surface((f_width * block, f_height * block))
    b_field = [[False for _ in range(f_width)] for _ in range(f_height)]

    shapes = []
    destroy = []
    score = [0, ]

    createShapes(shapes, destroy, b_field)
    drawer = Draw(screen, field, b_field, shapes, destroy, score)

    return type(
        'Struct', (object, ), {
            'screen': screen, 'field': field, 'b_field': b_field, 'shapes': shapes, 'destroy': destroy, 'score': score,
            'drawer': drawer, 'ptr': None
        }
    )()
