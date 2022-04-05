from settings import *
from Block import Block
from random import choice
import pygame


class Shape:
    def __init__(self, figure: tuple, x_: int, destroy: list, b_field: list):

        # Model of shape
        self.figure = figure[0]
        self.verticalSize = figure[1][1]
        self.horizontalSize = figure[1][0]

        # Blocks of shape
        self.shape = []

        # Pictures of blocks
        self.pictures = []

        # start pos
        collisionX = int((shapeSurfaceWidth - self.horizontalSize) / 2 * smalltall)
        collisionY = int((shapeSurfaceHeight - self.verticalSize) / 2 * smalltall)

        self.start_x = x_ + collisionX
        self.start_y = shapeSurfaceY + collisionY

        # current pos
        self.x = self.start_x
        self.y = self.start_y

        # Blocks which need to destroy
        self.destroy = destroy

        # block structure of field
        self.b_field = b_field

        # Holding Shape
        self.pressMode = False

        # Stored difference (dx, dy)
        self.difference = (0, 0)

    def install(self):
        if not self.in_field():
            self.x = self.start_x
            self.y = self.start_y

            self.init_shape()

            return False

        for s_block in self.shape:
            xb, yb = int(s_block.x / block + .5) - x, int(s_block.y / block + .5) - y

            s_block.x = xb * block
            s_block.y = yb * block

            self.b_field[yb][xb] = s_block

            if self.b_field[yb].count(False) == 0:
                self.destroy.extend([(i, yb) for i in range(len(self.b_field[yb]))])
            if sum([bool(self.b_field[i][xb]) for i in range(len(self.b_field))]) == len(self.b_field):
                self.destroy.extend([(xb, i) for i in range(len(self.b_field))])

        return True

    def setPressMode(self, mode: bool):
        sx, sy = pygame.mouse.get_pos()

        self.difference = (sx - self.x, sy - self.y)
        self.pressMode = mode

    def in_field(self):
        for s_block in self.shape:
            xb, yb = int(s_block.x / block + .5) - x, int(s_block.y / block + .5) - y

            if len(self.b_field) <= yb or yb < 0 or len(self.b_field[yb]) <= xb or xb < 0 or self.b_field[yb][xb]:
                return False
        return True

    def toBigSize(self):
        collisionX = int(self.horizontalSize * (tall - smalltall) / 2)
        collisionY = int(self.verticalSize * (tall - smalltall) / 2)

        self.x -= collisionX
        self.y -= collisionY

        for f_block, s_block in zip(self.figure, self.shape):
            s_block.x = self.x + (tall + 1) * f_block[0]
            s_block.y = self.y + (tall + 1) * f_block[1]

            s_block.width = tall
            s_block.height = tall

        for s_block, picture in zip(self.shape, self.pictures):
            s_block.path = picture
            s_block.installImg()

    def belongTo(self, x_: int, y_: int) -> bool:
        for block_ in self.shape:
            if block_.x <= x_ <= block_.x + tall and block_.y <= y_ <= block_.y + tall:
                return True
        return False

    def move(self):
        sx, sy = pygame.mouse.get_pos()

        offsetX = self.difference[0] - (sx - self.x)
        offsetY = self.difference[1] - (sy - self.y)

        self.x -= offsetX
        self.y -= offsetY

        for s_block in self.shape:
            s_block.x -= offsetX
            s_block.y -= offsetY

    def init_images(self):
        for _ in self.figure:
            path = "pictures/blocks/" + choice(bPictures)
            self.pictures.append(path)

    def init_shape(self):
        self.shape.clear()

        for block_, picture in zip(self.figure, self.pictures):
            x_ = self.start_x + (smalltall + 1) * block_[0]
            y_ = self.start_y + (smalltall + 1) * block_[1]

            # self.shape.append(pygame.Rect(x_, y_, smalltall, smalltall))
            self.shape.append(Block(x_, y_, smalltall, smalltall))

            self.shape[-1].path = picture + "s"
            self.shape[-1].installImg()
