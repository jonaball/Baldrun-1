import pygame as pg

pg.init()

# Klokke
fps = 60 # Spill fps
tikk = pg.time.Clock()

# Skjerminstillinger
SKJERM_HØYDE = 800
SKJERM_BREDDE = 800
# Farger


# Definer skjerm
pg.display.set_mode((SKJERM_BREDDE, SKJERM_HØYDE))
pg.display.fill(255,255,255)

# Spilløkke
running = True
while running:
    pg.display.flip()