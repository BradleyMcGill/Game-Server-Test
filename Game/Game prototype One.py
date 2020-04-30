import pygame as pg

class Game:
    def __init__(self):
        WIDTH,HEIGHT = 800,600
        self.window = pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption('Quiz')
        self.function = self.mainMenu

    def mainMenu(self):
        self.window.fill((255,255,255))

    def run(self):
        self.function()
        pg.display.update()
        


if __name__ == '__main__':
    game = Game()
    while True:
        game.run()
