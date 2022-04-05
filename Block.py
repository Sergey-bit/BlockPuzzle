import pygame


class Block(pygame.Rect):
    def __init__(self, left, top, width, height):
        super().__init__(left, top, width, height)

        self.img = None
        self.path = None

    def installImg(self):
        self.img = pygame.image.load(self.path + ".png").convert()

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))
