from settings import window
from printf import printText as printT
from settings import height, width, block, textColour, MENU, CONTINUE
from Panel import Panel
import sqlite3
import pygame


class Menu(object):
    def __init__(self, screen):
        self.screen = screen
        self.panel = Panel(20)

        # Mode
        self.startGame = MENU

        # DataBase
        self.database = sqlite3.connect('inf.db')
        self.cursor = self.database.cursor()
    
    def createDataBase(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS scores (id INTEGER PRIMARY KEY AUTOINCREMENT, score TEXT)')

    def serialization(self):
        for item in self.cursor.execute("SELECT score FROM scores ORDER BY score DESC").fetchall():
            self.addInTable(item[0])

    def printMsg(self, text, size, y):
        w = size[0]
        self.screen.blit(text, ((width * block - w) / 2, y))

    def draw(self, colour):
        self.screen.fill(window)
        self.panel.draw()
        self.screen.blit(self.panel.sc, (self.panel.x, self.panel.y))
        self.printMsg(*printT("Press any key...", 30, color=[colour, ] * 3), (height - 3) * block)

    def setStartGame(self, mode: int):
        self.startGame = mode

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            elif event.type == pygame.KEYDOWN:
                self.setStartGame(CONTINUE)
            elif event.type == pygame.MOUSEMOTION:
                x, y = pygame.mouse.get_pos()

                if (self.panel.y + self.panel.height * block) >= y >= self.panel.y and \
                        self.panel.x <= x <= width * block:
                    self.panel.setMode(self.panel.left)

                elif self.panel.getR():
                    self.panel.setMode(self.panel.right)

    def outScore(self, score):
        self.printMsg(*printT(f"{score}", 100, color=textColour), 4 * block)

    def panelMotion(self):
        self.panel.move()

    def addInDataBase(self, other: str):
        self.cursor.execute("INSERT INTO scores (score) VALUES (?)", (other, ))
        self.database.commit()

    def addInTable(self, other):
        if isinstance(other, str):
            unit = other
        else:
            unit = str(other)

        self.panel.add(unit)

    def on(self, lastScore, colour):
        self.events()
        self.panelMotion()
        self.draw(colour)

        if isinstance(lastScore, int):
            self.outScore(lastScore)
        else:
            self.outScore("Play")

        return self.startGame
