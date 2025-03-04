import pygame as pg
import sys
import objekter as obj

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
SKJERM_HØYDE = 800
SKJERM_BREDDE = 800

# Definer skjerm
SKJERM = pg.display.set_mode((SKJERM_BREDDE, SKJERM_HØYDE))
SKJERM.fill(BLÅ)

SKJERM_CENTER = (SKJERM_BREDDE//2, SKJERM_HØYDE//2)

# Objekter
obj.Dude("Prosjekt\Pygame_spill\Sprites\Head_hair0.png", SKJERM_CENTER)

# Spilløkke
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()
            sys.exit()
    
    pg.display.flip()
    tikk.tick(fps)
