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
GRÅ = (50, 50, 50)
RØD = (255, 0, 0)
GRØNN = (0, 255, 0)
BLÅ = (0, 0, 255)

# -- Skjerminstillinger -- 
pg.display.set_caption("BALD RUN v0.1")
SKJERM_HØYDE = 720
SKJERM_BREDDE = 1080

# -- Mapinstillinger --
MAP_STØRRELSE = 250 # 200 = normal
VEGG_FARGE = (GRÅ)

# -- Objektinstillinger --
DUDE_STØRRELSE = (150, 150) # BREDDE x HØYDE

# -- Definer skjerm --
SKJERM = pg.display.set_mode((SKJERM_BREDDE, SKJERM_HØYDE))
BG_FARGE = (HVIT)

CENTER_X = SKJERM_BREDDE//2 # Midten av skjermen
CENTER_Y = SKJERM_HØYDE//2
SCREEN_CENTER = (CENTER_X, CENTER_Y)


# --------------------------------- Objektkontroll -----------------------------------

class Dude():
    """
    Lag en dude
    """
    def __init__(self, x, y, størrelse):
        self.pos = (x, y) # Posisjonen til dude (Definert ved skapelse)
        self.størrelse = størrelse # Størrelsen til dude (Definert i -- Objektinstillinger --)

        self.hair0 = pg.image.load("Prosjekt-Pygame\Sprites\Head_hair0.png") # Frisyrer (For parykkene)
        self.hair1 = pg.image.load("Prosjekt-Pygame\Sprites\Head_hair1.png") # 1
        self.hair2 = pg.image.load("Prosjekt-Pygame\Sprites\Head_hair2.png") # 2
        self.hair3 = pg.image.load("Prosjekt-Pygame\Sprites\Head_hair3.png") # 3
        self.frisyre = self.hair0 # Frisyren dude starter med

        self.body0 = pg.image.load("Prosjekt-Pygame\Sprites\Body0.png") # Kropp-stadier (for walkcycle)
        self.body1 = pg.image.load("Prosjekt-Pygame\Sprites\Body1.png") # 1
        self.body2 = pg.image.load("Prosjekt-Pygame\Sprites\Body2.png") # 2
        self.kropp = self.body0 # Idle kropp
        self.walkcycle = [self.body0, self.body1, self.body2] # Liste med forskjellige "stages" i walkcyclen
        self.walking_timer = 0 # En klokke som tikker oppover og holder styr over hvor i walkcyclen vi er

        self.opp = 0 # Retningene dude peker
        self.ned = 180 
        self.venstre = 90
        self.høyre = -90
        self.opp_venstre = 45
        self.ned_venstre = 135
        self.opp_høyre = -45
        self.ned_høyre = -135
        self.retning = self.opp # Startretning er alltid opp

        # -- justeringer og funksjoner -- 
        self.oppdater_størrelse() # Skalerer dude til riktig størrelse (basert på self.størrelse)
        self.oppdater_retning() # Roterer dude til riktig retning (basert på self.retning)
        self.oppdater_rect() # Lager en rect som kan brukes for posisjon og rotasjon
        self.kollisjon() # Lager en rect som kan brukes for kollisjon, og sjekker for kollisjon med recten

    def oppdater_størrelse(self):
        self.skalert_hode = pg.transform.scale(self.frisyre, self.størrelse) # Skalerer dude til riktig størrelse
        self.skalert_kropp = pg.transform.scale(self.kropp, self.størrelse)
    
    def oppdater_retning(self):
        self.rotert_hode = pg.transform.rotate(self.skalert_hode, self.retning) # Roterer dude i riktig retning
        self.rotert_kropp = pg.transform.rotate(self.skalert_kropp, self.retning)

    def oppdater_rect(self):
        self.dude_rect = self.rotert_hode.get_rect(center = self.pos)

    def kollisjon(self):
        self.kollisjon_rect = self.skalert_hode.get_rect(center = self.pos)
        for vegg in MAP_VEGGER:
            if self.kollisjon_rect.colliderect(vegg):
                if self.retning == self.opp:
                    pass
                elif self.retning == self.venstre:
                    pass
                elif self.retning == self.ned:
                    pass
                elif self.retning == self.høyre:
                    pass
                elif self.retning == self.opp_venstre:
                    pass
                elif self.retning == self.ned_venstre:
                    pass
                elif self.retning == self.ned_høyre:
                    pass
                elif self.retning == self.opp_høyre:
                    pass
                

    def tegn_hode(self, skjerm):
        skjerm.blit(self.rotert_hode, self.dude_rect) # Viser den nye, og skalerte, duden

    def tegn_kropp(self, skjerm):

        skjerm.blit(self.rotert_kropp, self.dude_rect) # Viser den nye, og skalerte, duden

    def oppdater_walkcycle(self):
        if walking: # walkcyckle skal bare oppdateres når et input sier at dude går
            if self.walking_timer % 10 == 0: # Walking timer går opp med 1 per frame, hver 10 frames er dette sant
                self.walking_frame += 1 # Går til neste bilde i walkcycle lista
                if self.walking_frame == 3: # Når cyclen har gått igjennom hele lista (etter 3 stages), starter den på nytt fra 0
                    self.walking_frame = 0 
                self.kropp = self.walkcycle[self.walking_frame] # Setter bildet for kropp til riktig stadie i walkcycle
            self.walking_timer += 1 # Øker walking timeren hver frame/hver gang oppdater_walkcycle() funksjon blir kallt
        else: # Setter alt tilbake til standard når spilleren slutter å gå
            self.kropp = self.body0
            self.walking_frame = 0
            self.walking_timer = 0
        
class Map():
    """
    Map stuff
    """
    def __init__(self, størrelse):
        self.tilesize = størrelse
        self.offset_x = -3760 # Startposisjon (midten av kartet)
        self.offset_y = -2821

    def LoadMap(self, mapfil):
        with open(mapfil, "r") as fil:
            return json.load(fil)
    
    def LagVegger(self, lastetmap):
        global MAP_VEGGER
        tilesize = self.tilesize
        MAP_VEGGER = []
        for vegg in lastetmap:
            pos = lastetmap[vegg]["position"]
            MAP_VEGGER.append(pg.Rect(pos[0] * tilesize + self.offset_x, pos[1] * tilesize + self.offset_y, tilesize, tilesize))

    def VisMap(self, lastetmap):
        tilesize = self.tilesize
        for tile in lastetmap:
            pos = lastetmap[tile]["position"]
            pg.draw.rect(SKJERM, (VEGG_FARGE), (pos[0] * tilesize + self.offset_x, pos[1] * tilesize + self.offset_y, tilesize, tilesize))


# --------------------------------- Spilløkke ------------------------------------

# -- Oprett objektene: --
MAP = Map(MAP_STØRRELSE) # Lager et instans av Map classen
MAP_1 = MAP.LoadMap("Prosjekt-Pygame/maps/map1.json")
MAP_VEGGER = []
MAP.LagVegger(MAP_1)

DUDE = Dude(CENTER_X, CENTER_Y, DUDE_STØRRELSE) # Lager en "dude"

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

    # -- Bevegelse (flytter map/bakgrunn) --
    walking = False # Default verdien av walking er false (altså man står stille når ingenting skjer)
    
    bitmask = 0
    if taster[pg.K_w]:
        bitmask += 1
    if taster[pg.K_a]:
        bitmask += 2
    if taster[pg.K_s]:
        bitmask += 4
    if taster[pg.K_d]:
        bitmask += 8

    if bitmask == 1: # TRYKKER W
        MAP.offset_y += 500/fps
        DUDE.retning = DUDE.opp
        walking = True
    elif bitmask == 2: # TRYKKER A
        MAP.offset_x += 500/fps
        DUDE.retning = DUDE.venstre
        walking = True
    elif bitmask == 4: # TRYKKER S
        MAP.offset_y -= 500/fps
        DUDE.retning = DUDE.ned
        walking = True
    elif bitmask == 8: # TRYKKER D
        MAP.offset_x -= 500/fps
        DUDE.retning = DUDE.høyre
        walking = True
    elif bitmask == 3: # TRYKKER W A
        MAP.offset_x += 500/fps/1.4
        MAP.offset_y += 500/fps/1.4
        DUDE.retning = DUDE.opp_venstre
        DUDE.skrå = True
        walking = True
    elif bitmask == 6: # TRYKKER A S
        MAP.offset_x += 500/fps/1.4
        MAP.offset_y -= 500/fps/1.4
        DUDE.retning = DUDE.ned_venstre
        walking = True
    elif bitmask == 12: # TRYKKER S D
        MAP.offset_x -= 500/fps/1.4
        MAP.offset_y -= 500/fps/1.4
        DUDE.retning = DUDE.ned_høyre
        walking = True
    elif bitmask == 9: # TRYKKER D W
        MAP.offset_x -= 500/fps/1.4
        MAP.offset_y += 500/fps/1.4
        DUDE.retning = DUDE.opp_høyre
        walking = True

    # -- Logikk --
    DUDE.oppdater_retning() # VIKTIG! Passer på at duden peker i riktig retning når den byttes
    DUDE.oppdater_rect() # VIKTIG! Passer på at rectangle er oppdatert når karakteren endrer seg!!!! :=()
    DUDE.oppdater_walkcycle()  # Oppdater walkcycle hvis spilleren går
    MAP.LagVegger(MAP_1)
    DUDE.kollisjon()

    # -- Vis skjermobjekter --
    SKJERM.fill(BG_FARGE)
    DUDE.tegn_kropp(SKJERM)
    DUDE.tegn_hode(SKJERM)
    MAP.VisMap(MAP_1)

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

    for vegg in MAP_VEGGER:
        pg.draw.rect(SKJERM, (RØD), vegg)
    # pg.draw.rect(SKJERM, (200, 200, 200), DUDE.kollisjon_rect)
    # print(f"X = {MAP.offset_x}, Y = {MAP.offset_y}")

    pg.display.flip()
    clock.tick(fps)
