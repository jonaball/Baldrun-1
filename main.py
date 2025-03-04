import pygame as pg

pg.init()

# Skjerminstillinger
SKJERM_HØYDE = 800
SKJERM_BREDDE = 800
    # Farger
SVART = (0,0,0)
HVIT = (255,255,255)
RØD = (255,0,0)
GRØNN = (0,255,0)
BLÅ = (0,0,255)

pg.display.set_mode((SKJERM_BREDDE, SKJERM_HØYDE))
pg.display.flip()
