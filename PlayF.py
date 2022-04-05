from settings import OVER, CONTINUE, JUMP, block, width, height, textColour
from createShapes import createShapes
from printf import printText as printT
from checkForContinuos import checkForContinuous
import pygame


def game_(data, mode: int, colour=255):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        elif event.type == pygame.KEYDOWN and mode == OVER:
            return JUMP
        elif event.type == pygame.MOUSEBUTTONDOWN and mode == CONTINUE:
            for i, shape in enumerate(data.shapes):
                if shape.belongTo(*pygame.mouse.get_pos()):
                    shape.toBigSize()
                    shape.setPressMode(True)

                    data.ptr = i
                    break

        elif event.type == pygame.MOUSEBUTTONUP and data.ptr is not None and mode == CONTINUE:
            data.shapes[data.ptr].setPressMode(False)

            if data.shapes[data.ptr].install():
                data.shapes.pop(data.ptr)

                if len(data.shapes) == 0:
                    createShapes(data.shapes, data.destroy, data.b_field)

            data.ptr = None
        elif event.type == pygame.MOUSEMOTION and data.ptr is not None and mode == CONTINUE:
            data.shapes[data.ptr].move()

    data.drawer.draw(data.ptr)

    if mode == CONTINUE:

        if len(data.destroy) == 0 and not checkForContinuous(data.b_field, data.shapes):
            return OVER

        return CONTINUE
    else:
        text, size = printT("Press any key...", 40, color=[colour] * 3)

        data.screen.blit(text, ((width * block - size[0]) // 2, (height - 2) * block))

        return OVER
