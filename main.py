import pygame as pg
import sys
import json

pg.init() # Start pygame tulling

# ----------------------------------Instillinger -------------------------------------

# --Klokke --
fps = 60 # Spill fps
clock = pg.time.Clock()

# -- Farger --
SVART = (20, 20, 20)
HVIT = (255, 255 , 255)
GRÅ = (180, 180, 180)
RØD = (255, 0, 0)
GRØNN = (0, 255, 0)
BLÅ = (0, 0, 255)

# -- Skjerminstillinger -- 
pg.display.set_caption("BALD RUN v0.1")
SKJERM_HØYDE = 720
SKJERM_BREDDE = 1080

# -- Mapinstillinger --
MAP_STØRRELSE = 200 # 200 = normal

# -- Objektinstillinger --
DUDE_STØRRELSE = (150, 150) # BREDDE x HØYDE

# -- Definer skjerm --
SKJERM = pg.display.set_mode((SKJERM_BREDDE, SKJERM_HØYDE))
BG_FARGE = (HVIT)

CENTER_X = SKJERM_BREDDE//2 # Midten av skjermen
CENTER_Y = SKJERM_HØYDE//2


# --------------------------------- Objektkontroll -----------------------------------

class Dude():
    """
    Lag en dude
    """
    def __init__(self, x, y, scale):
        self.hair0 = pg.image.load("Prosjekt-Pygame\Sprites\Head_hair0.png") # Frisyrer
        self.hair1 = pg.image.load("Prosjekt-Pygame\Sprites\Head_hair1.png")
        self.hair2 = pg.image.load("Prosjekt-Pygame\Sprites\Head_hair2.png")
        self.hair3 = pg.image.load("Prosjekt-Pygame\Sprites\Head_hair3.png")
        self.frisyre = self.hair0 # Frisyren dude starter med

        self.body0 = pg.image.load("Prosjekt-Pygame\Sprites\Body0.png")
        self.body1 = pg.image.load("Prosjekt-Pygame\Sprites\Body1.png")
        self.body2 = pg.image.load("Prosjekt-Pygame\Sprites\Body2.png")
        self.kropp = self.body0 # Kroppen dude starter med

        self.walkcycle = [self.body0, self.body1, self.body2] # Liste med forskjellige "stages" i walkcyclen
        self.walking_timer = 10

        self.scale = scale # Størrelsen til dude (Definert i -- Objektinstillinger --)
        self.width = self.scale[0]
        self.height = self.scale[1]
        self.x = x - self.width//2
        self.y = y - self.height//2
        
        self.opp = 0
        self.venstre = 90
        self.ned = 180
        self.høyre = -90
        self.retning = self.opp # Startretning er alltid opp

        self.oppdater_størrelse() # Sørg for at frisyren er oppdatert til den nye størrelsen
        self.oppdater_retning() # Sørg for at duden peker riktig vei

    def oppdater_størrelse(self):
        self.skalert_hode = pg.transform.scale(self.frisyre, self.scale) # Skalerer dude til riktig størrelse
        self.skalert_kropp = pg.transform.scale(self.kropp, self.scale)
    
    def oppdater_retning(self):
        self.skalert_hode = pg.transform.rotate(self.skalert_hode, self.retning) # Roterer dude i riktig retning
        self.skalert_kropp = pg.transform.rotate(self.skalert_kropp, self.retning)

    def tegn_hode(self, skjerm):
        skjerm.blit(self.skalert_hode, (self.x, self.y)) # Viser den nye, og skalerte, duden

    def tegn_kropp(self, skjerm):
        skjerm.blit(self.skalert_kropp, (self.x, self.y)) # Viser den nye, og skalerte, duden

    def oppdater_walkcycle(self):
        if walking:
            if self.walking_timer % 10 == 0: # Walking timer går opp med 1 per frame, hver 10 frames er dette sant
                self.walking_frame += 1
                if self.walking_frame == 3: # Når cyclen har gått igjennom hele lista (etter 3 stages), starter den på nytt fra 0
                    self.walking_frame = 0 
                self.kropp = self.walkcycle[self.walking_frame]
            self.walking_timer += 1 # Øker walking timeren
        else: # Setter alt tilbake til standard når spilleren slutter å gå
            self.kropp = self.body0
            self.walking_frame = 0
            self.walking_timer = 0
        
class Map():
    """
    Map stuff
    """
    def __init__(self, scale):
        self.tilesize = scale
        self.offset_x = -3330 # Startposisjon (midten av kartet)
        self.offset_y = -2350

    def LoadMap(self, mapfil):
        with open(mapfil, "r") as fil:
            return json.load(fil)
        
    def VisMap(self, loadedmap):
        tilesize = self.tilesize
        for tile in loadedmap:
            pos = loadedmap[tile]["position"]
            type = loadedmap[tile]["type"]
            pg.draw.rect(SKJERM, (SVART), (pos[0] * tilesize + self.offset_x, pos[1] * tilesize + self.offset_y, tilesize, tilesize))


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

    taster = pg.key.get_pressed() # Holder en liste over alle taster som er trykt ned 

    # Bevegelse (flytter map/bakgrunn)
    walking = False
    if taster[pg.K_w]:
        MAP.offset_y += 500/fps
        DUDE.retning = DUDE.opp
        walking = True
    if taster[pg.K_a]:
        MAP.offset_x += 500/fps 
        DUDE.retning = DUDE.venstre
        walking = True
    if taster[pg.K_s]:
        MAP.offset_y -= 500/fps
        DUDE.retning = DUDE.ned
        walking = True
    if taster[pg.K_d]:
        MAP.offset_x -= 500/fps
        DUDE.retning = DUDE.høyre
        walking = True
    DUDE.oppdater_retning() # VIKTIG! Passer på at duden peker i riktig retning når den byttes

    DUDE.oppdater_walkcycle()  # Oppdater walkcycle hvis spilleren går

    # -- Vis skjermobjekter --
    SKJERM.fill(BG_FARGE)
    MAP.VisMap(MAP_1)
    DUDE.tegn_kropp(SKJERM)
    DUDE.tegn_hode(SKJERM)

    pg.display.flip()
    clock.tick(fps)

    # -- Debug -- 
    if taster[pg.K_0]:
        DUDE.frisyre = DUDE.hair0
    if taster[pg.K_1]:
        DUDE.frisyre = DUDE.hair1
    if taster[pg.K_2]:
        DUDE.frisyre = DUDE.hair2
    if taster[pg.K_3]:
        DUDE.frisyre = DUDE.hair3 
    DUDE.oppdater_størrelse() # VIKTIG! passer på at duden er skalert riktig når frisyren byttes

    print(f"X = {MAP.offset_x}, Y = {MAP.offset_y}")