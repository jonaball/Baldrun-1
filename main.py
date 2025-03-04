import pygame as pg
import sys

pg.init()

# Klokke
fps = 60 # Spill fps
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
SKJERM.fill(HVIT)

# Spilløkke
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    
    pg.display.flip()