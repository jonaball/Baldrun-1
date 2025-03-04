import pygame as pg

class Dude():
    """
    Lag en dude
    """
    def __init__(self, image, x, y):
        self.image = pg.image.load(image)
        self.x = x
        self.y = y

    def render(self, skjerm):
        skjerm.blit(self.image, (self.x, self.y))
