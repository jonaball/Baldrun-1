import pygame as pg
import sys
import json

pg.init() # Start pygame tulling

# --Klokke --
fps = 60 # Spill fps
clock = pg.time.Clock()

# -- Farger --
SVART = (0, 0, 0)
HVIT = (255, 255 , 255)
RØD = (255, 0, 0)
GRØNN = (0, 255, 0)
BLÅ = (0, 0, 255)

# -- Skjerminstillinger -- 
pg.display.set_caption("BALD RUN v0.1")
SKJERM_HØYDE = 720
SKJERM_BREDDE = 1080

# -- Definer skjerm --
SKJERM = pg.display.set_mode((SKJERM_BREDDE, SKJERM_HØYDE))
BG_FARGE = (SVART)

CENTER_X = SKJERM_BREDDE//2 # Midten av skjermen
CENTER_Y = SKJERM_HØYDE//2


# --------------------------------- Objektkontroll -----------------------------------

class Dude():
    """
    Lag en dude
    """
    def __init__(self, x, y):
        self.hair0 = pg.image.load("Prosjekt-Pygame\Sprites\Head_hair0.png")
        self.hair1 = pg.image.load("Prosjekt-Pygame\Sprites\Head_hair1.png")
        self.hair2 = pg.image.load("Prosjekt-Pygame\Sprites\Head_hair2.png")
        self.hair3 = pg.image.load("Prosjekt-Pygame\Sprites\Head_hair3.png")

        self.frisyre = self.hair0

        self.width = self.frisyre.get_width()
        self.height = self.frisyre.get_height()
        self.x = x - self.width//2
        self.y = y - self.height//2

    def tegn(self, skjerm):
        skjerm.blit(self.frisyre, (self.x, self.y))

class Map():
    """
    Lag mappet
    """
    def __init__(self, loadedmap):
        self.tilesize = 25
        self.loadedmap = loadedmap

    def LoadMap(mapfil):
        with open(mapfil, "r") as fil:
            return json.load(fil)
        
    def VisMap(loadedmap):
        tilesize = 25
        for tile in loadedmap:
            pos = loadedmap[tile]["position"]
            type = loadedmap[tile]["type"]
            pg.draw.rect(SKJERM, (200, 200, 200), (pos[0]*tilesize, pos[1]*tilesize, tilesize, tilesize))


# --------------------------------- Spilløkke ------------------------------------
    
    # -- Oprett objektene: --
DUDE = Dude(CENTER_X, CENTER_Y) # Lager en "Dude"
MAP_1 = Map.LoadMap("Prosjekt-Pygame\maps\map1.json")


running = True
while running: # Hovedløkken til spillet

    # -- Eventer handler --
    for event in pg.event.get():
        if event.type == pg.QUIT: # Når spillet avsluttes ved å trykke på X-en
            running = False
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN: # Alle eventer for tastetrykk kommer under her
            if event.key == pg.K_0:
                DUDE.frisyre = DUDE.hair0
            if event.key == pg.K_1:
                DUDE.frisyre = DUDE.hair1
            if event.key == pg.K_2:
                DUDE.frisyre = DUDE.hair2
            if event.key == pg.K_3:
                DUDE.frisyre = DUDE.hair3 

    # -- Vis skjermobjekter --
    SKJERM.fill(BG_FARGE)
    Map.VisMap(MAP_1)
    DUDE.tegn(SKJERM)

    pg.display.flip()
    clock.tick(fps)
