import pygame as pg
import sys

pg.init()

# Klokke
fps = 120 # Spill fps
tikk = pg.time.Clock()

# Farger
SVART = (0, 0, 0)
HVIT = (255, 255 , 255)
RØD = (255, 0, 0)
GRØNN = (0, 255, 0)
BLÅ = (0, 0, 255)

# Skjerminstillinger
SKJERM_HØYDE = 720
SKJERM_BREDDE = 1080

# Definer skjerm
SKJERM = pg.display.set_mode((SKJERM_BREDDE, SKJERM_HØYDE))
SKJERM.fill(SVART)

CENTER_X = SKJERM_BREDDE//2
CENTER_Y = SKJERM_HØYDE//2

# Objekter
class Dude():
    """
    Lag en dude
    """
    def __init__(self, image, x, y):
        self.image = pg.image.load(image)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = x - self.width//2
        self.y = y - self.height//2

    def render(self, skjerm):
        skjerm.blit(self.image, (self.x, self.y))

HAIRSTAGE = "Pygame_spill\Sprites\Head_hair0.png"


# Spilløkke
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_0:
                HAIRSTAGE = "Pygame_spill\Sprites\Head_hair0.png"
            if event.key == pg.K_1:
                HAIRSTAGE = "Pygame_spill\Sprites\Head_hair1.png"
            if event.key == pg.K_2:
                HAIRSTAGE = "Pygame_spill\Sprites\Head_hair2.png"
            if event.key == pg.K_3:
                HAIRSTAGE = "Pygame_spill\Sprites\Head_hair3.png" 
    
    SKJERM.fill(SVART)
    DUDE = Dude(HAIRSTAGE, CENTER_X, CENTER_Y)
    DUDE.render(SKJERM)
    pg.display.flip()
    tikk.tick(fps)
