from settings import p_width, p_height, width, block, surfaceColour, textColour
from printf import printText
import pygame


class Panel(object):
    static, left, right = 0, -1, 1

    def __init__(self, offsetY: int):
        self.sc = pygame.Surface((p_width * block, p_height * block))

        # Pos
        self.x = (width - 1) * block
        self.y = 2 * block

        # Offset at Oy
        self.offset = offsetY + 30

        # Size
        self.width = p_width
        self.height = p_height

        # moving mode
        self.mode = self.static

        self.speed = 4

        # table content
        self.items = []

    def add(self, other: str):
        self.items.append(other)

    def extend(self, other):
        self.items.extend(other)

    def __drawTable(self):
        y = self.offset
        vertical = block
        for item in sorted(self.items, key=lambda x: int(x), reverse=True)[:self.height - 2]:
            text, size = printText(item, 16, color=textColour)

            self.sc.blit(text, ((self.width * block - size[0]) // 2, y + (vertical - size[1]) // 2))

            y += vertical

    def draw(self):
        self.sc.fill(surfaceColour)
        pygame.draw.rect(
            self.sc, "black", [0, 0, self.width * block, self.height * block], 1
        )
        self.__drawTable()

        text, size = printText("best scores", 18, color=textColour)
        self.sc.blit(text, ((self.width * block - size[0]) // 2, 10))

    def getR(self):
        return self.x != (width - 1) * block

    def setMode(self, new):
        self.mode = new

    def move(self):
        if (width - self.width) * block <= self.x + self.speed * self.mode <= (width - 1) * block:
            self.x += self.speed * self.mode
        else:
            self.mode = self.static
