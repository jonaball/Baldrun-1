import pygame as pg
import pygame
import json

def loadJson(filename) -> dict:
    with open(filename, 'r') as f:
        return json.load(f)

def saveJson(data: dict, filename: str):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

SKJERM_HØYDE= 720
SKJERM_BREDDE = 1080
WIDTH, HEIGHT = SKJERM_BREDDE, SKJERM_HØYDE

win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("BALD RUN v1.0 - MAP EDITOR")

position = (0, 0)
tilesize = 25

loadedData = loadJson("Prosjekt-Pygame/maps/map1.json")
print(loadedData)

def DisplayMap(mapData):
    for tile in mapData:
        pos = mapData[tile]["position"]
        type = mapData[tile]["type"]
        pygame.draw.rect(win, (200, 200, 200), (pos[0]*tilesize, pos[1]*tilesize, tilesize, tilesize))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                break
    win.fill((0,0,0))
    DisplayMap(loadedData)
    
    pygame.display.flip()
    clock.tick(60)