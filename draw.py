import pygame
from settings import *
from printf import printText


class Draw:
    def __init__(self, screen: pygame.Surface, field: pygame.Surface,
                 b_field: list, shapes_: list, destroy: list, score: list):

        # Areas
        self.sc = screen
        self.field = field

        #  Block structure of field
        self.b_field = b_field

        # Free shapes
        self.shapes = shapes_

        # Block which need to destroy
        self.destroy = destroy

        # Score
        self.score = score

    def dShapes(self):
        for y_ in range(f_height):
            for x_ in range(f_width):
                if self.b_field[y_][x_]:
                    self.b_field[y_][x_].draw(self.field)

        for shape_ in self.shapes:
            for block_ in shape_.shape:
                block_.draw(self.sc)

    def dWindow(self):
        self.sc.fill(window)
        self.sc.blit(self.field, (x * block, y * block))
        self.field.fill(fieldColour)
        pygame.draw.rect(
            self.sc,
            borderSurfaceColour,
            [x * block - 1, y * block - 1, f_width * block + 1, f_height * block + 1],
            1
        )

    def shadow(self, ptr):
        shape = self.shapes[ptr]
        if shape.in_field():
            for block_ in shape.shape:
                x_, y_ = int(block_.x / block + .5) - x, int(block_.y / block + .5) - y
                pygame.draw.rect(self.field, shadowBlock, [x_ * block, y_ * block, tall, tall])

    def destroyBlocks(self):
        if not self.destroy:
            return
        x_, y_ = self.destroy.pop(-1)
        self.b_field[y_][x_] = False
        self.score[0] += 5

        if len(self.destroy):
            x_, y_ = self.destroy.pop(0)
            self.b_field[y_][x_] = False
            self.score[0] += 5

    def dField(self):
        for y_ in range(f_height):
            for x_ in range(f_width):
                pygame.draw.rect(self.field, borderFieldColour, [x_ * block, y_ * block, tall, tall], 1)

    def dSurfaces(self):
        size = (shapeSurfaceWidth * smalltall, shapeSurfaceHeight * smalltall)

        pygame.draw.rect(self.sc, surfaceColour, [shapeSurfaceOneX, shapeSurfaceY, *size])
        pygame.draw.rect(self.sc, surfaceColour, [shapeSurfaceTwoX, shapeSurfaceY, *size])
        pygame.draw.rect(self.sc, surfaceColour, [shapeSurfaceThreeX, shapeSurfaceY, *size])

        pygame.draw.rect(
            self.sc, borderSurfaceColour, [shapeSurfaceOneX - 1, shapeSurfaceY - 1, size[0] + 1, size[0] + 1], 1)
        pygame.draw.rect(
            self.sc, borderSurfaceColour, [shapeSurfaceTwoX - 1, shapeSurfaceY - 1, size[0] + 1, size[0] + 1], 1)
        pygame.draw.rect(
            self.sc, borderSurfaceColour, [shapeSurfaceThreeX - 1, shapeSurfaceY - 1, size[0] + 1, size[0] + 1], 1)

    def printScore(self):
        text, size = printText(f"SCORE: {self.score}", 22, color=textColour)

        self.sc.blit(text, ((width * block - size[0]) // 2, 10))

    def draw(self, ptr):
        self.dWindow()
        self.dSurfaces()
        self.dField()
        self.printScore()
        self.dShapes()
        self.destroyBlocks()

        if ptr is not None:
            self.shadow(ptr)
