import pygame as pg
import sys
import json

pg.init() # Start pygame tulling

# ----------------------------------Instillinger -------------------------------------

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

# -- Mapinstillinger --
MAP_STØRRELSE = 200 # 100 = normal

# -- Objektinstillinger --
DUDE_STØRRELSE = (150, 150) # BREDDE x HØYDE

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
    def __init__(self, x, y, scale):
        self.hair0 = pg.image.load("Prosjekt-Pygame\Sprites\Head_hair0.png")
        self.hair1 = pg.image.load("Prosjekt-Pygame\Sprites\Head_hair1.png")
        self.hair2 = pg.image.load("Prosjekt-Pygame\Sprites\Head_hair2.png")
        self.hair3 = pg.image.load("Prosjekt-Pygame\Sprites\Head_hair3.png")

        self.frisyre = self.hair0 # Frisyren dude starter med

        self.scale = scale # Størrelsen til dude (Definert i -- Objektinstillinger --)
        
        self.width = self.scale[0]
        self.height = self.scale[1]
        self.x = x - self.width//2
        self.y = y - self.height//2

        self.oppdater_frisyre() # Sørg for at frisyren er oppdatert til den nye størrelsen

    def oppdater_frisyre(self):
        self.skalert_dude = pg.transform.scale(self.frisyre, self.scale) # Skalerer dude til riktig størrelse

    def tegn(self, skjerm):
        skjerm.blit(self.skalert_dude, (self.x, self.y)) # Viser den nye, og skalerte, duden

class Map():
    """
    Lag mappet
    """
    def __init__(self, scale):
        self.tilesize = scale
        self.offset_x = 0
        self.offset_y = 0

    def LoadMap(self, mapfil):
        with open(mapfil, "r") as fil:
            return json.load(fil)
        
    def VisMap(self, loadedmap):
        tilesize = self.tilesize
        for tile in loadedmap:
            pos = loadedmap[tile]["position"]
            type = loadedmap[tile]["type"]
            pg.draw.rect(SKJERM, (HVIT), (pos[0]*tilesize + self.offset_x, pos[1]*tilesize + self.offset_y, tilesize, tilesize))


# --------------------------------- Spilløkke ------------------------------------
    
# -- Oprett objektene: --
DUDE = Dude(CENTER_X, CENTER_Y, DUDE_STØRRELSE) # Lager en "Dude"

MAP = Map(MAP_STØRRELSE) # Lager et instans av Map classen
MAP_1 = MAP.LoadMap("Prosjekt-Pygame/maps/map1.json")

# -- Hovedløkken til spillet --
running = True
while running:

    # -- Eventer handler --
    for event in pg.event.get():
        if event.type == pg.QUIT: # Når spillet avsluttes ved å trykke på X-en
            running = False
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN: # Alle eventer for tastetrykk kommer under her
            # Debug - hårfrisyre stuff
            if event.key == pg.K_0:
                DUDE.frisyre = DUDE.hair0
            if event.key == pg.K_1:
                DUDE.frisyre = DUDE.hair1
            if event.key == pg.K_2:
                DUDE.frisyre = DUDE.hair2
            if event.key == pg.K_3:
                DUDE.frisyre = DUDE.hair3 
            DUDE.oppdater_frisyre() # VIKTIG! passer på at duden er skalert riktig når frisyren byttes

            # Movement (flytter mappet)
            if event.key == pg.K_w:
                MAP.offset_y +10/fps
            if event.key == pg.K_a:
                MAP.offset_x +10/fps    
            if event.key == pg.K_s:
                MAP.offset_y -10/fps
            if event.key == pg.K_d:
                MAP.offset_x -10/fps

    # -- Vis skjermobjekter --
    SKJERM.fill(BG_FARGE)
    MAP.VisMap(MAP_1)
    DUDE.tegn(SKJERM)

    pg.display.flip()
    clock.tick(fps)
