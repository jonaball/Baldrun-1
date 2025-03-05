import pygame as pg
import pygame
import json
import os
from tkinter import messagebox
import tkinter

def confirm(map):
    result = messagebox.askyesno("Lag ny fil", f"map{map}.json finnes ikke. Vil du lage den?")
    if result:
        return True
    else:
        return False

root = tkinter.Tk()
root.withdraw()

def loadJson(filename):
    global currentMap
    if not os.path.exists(filename):
        if confirm(currentMap):
            with open(filename, 'w') as f:
                json.dump({}, f)
        else: 
            return None
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
currentMap = 1
MAP_TO_EDIT = f"Prosjekt-Pygame/maps/map{currentMap}.json" # ENDRE DENNE TIL MAP DU VIL ENDRE
loadedData = loadJson(MAP_TO_EDIT)
print(loadedData)

tileset = pygame.image.load("Prosjekt-Pygame/Sprites/Map/Template.png")
tiles = {
    "i": tileset.subsurface(0,0, 3,3),
    "tb": tileset.subsurface(3,0, 3,3),
    "rl": tileset.subsurface(6,0, 3,3),
    "rb": tileset.subsurface(9,0, 3,3),
    "tr": tileset.subsurface(0,3, 3,3),
    "tl": tileset.subsurface(3,3, 3,3),
    "bl": tileset.subsurface(6,3, 3,3),
    "b": tileset.subsurface(9,3, 3,3),
    "r": tileset.subsurface(0,6, 3,3),
    "t": tileset.subsurface(3,6, 3,3),
    "l": tileset.subsurface(6,6, 3,3),
    "rbl": tileset.subsurface(9,6, 3,3),
    "trb": tileset.subsurface(0,9, 3,3),
    "trl": tileset.subsurface(3,9, 3,3),
    "tbl": tileset.subsurface(6,9, 3,3),
    "trbl": tileset.subsurface(9,9, 3,3)
}

def DisplayMap():
    for tile in loadedData:
        pos = loadedData[tile]["position"]
        type = loadedData[tile]["type"]
        pygame.draw.rect(win, (200, 200, 200), (pos[0]*tilesize, pos[1]*tilesize, tilesize, tilesize))

def DisplayHover():
    pos = pygame.mouse.get_pos()
    pygame.draw.rect(win, (100, 100, 100), (pos[0]-pos[0]%tilesize, pos[1]-pos[1]%tilesize, tilesize, tilesize))
    win.blit(pygame.transform.scale(tiles["i"], (tilesize, tilesize)), (pos[0]-pos[0]%tilesize, pos[1]-pos[1]%tilesize))

def DrawMap():
    pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    tilepos = pos[0]//tilesize, pos[1]//tilesize

    tileType = "wall"
    if click[0] == True:
        loadedData[f"{tilepos[0]},{tilepos[1]}"] = {"type": tileType, "position": tilepos}
    if click[2] == True:
        try:
            loadedData.pop(f"{tilepos[0]},{tilepos[1]}")
        except:
            print(f"No tile at {tilepos} to remove.")

def ConnectingTiles(tile):
    pass

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            saveJson(loadedData, MAP_TO_EDIT)
            pygame.quit()
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                saveJson(loadedData, MAP_TO_EDIT)
                pygame.quit()
                break
            if event.key == pygame.K_RIGHT:
                # SAVE
                saveJson(loadedData, MAP_TO_EDIT)
                # LOAD
                currentMap += 1
                MAP_TO_EDIT = f"Prosjekt-Pygame/maps/map{currentMap}.json"
                if loadJson(MAP_TO_EDIT) != None:
                    loadedData = loadJson(MAP_TO_EDIT)
                else:
                    currentMap -= 1
                    MAP_TO_EDIT = f"Prosjekt-Pygame/maps/map{currentMap}.json"
            if event.key == pygame.K_LEFT:
                if currentMap != 1:
                    # SAVE
                    saveJson(loadedData, MAP_TO_EDIT)
                    # LOAD
                    currentMap -= 1
                    MAP_TO_EDIT = f"Prosjekt-Pygame/maps/map{currentMap}.json"
                    loadedData = loadJson(MAP_TO_EDIT)
            
    win.fill((0,0,0))
    DisplayMap()
    DisplayHover()
    DrawMap()
    
    pygame.display.flip()
    clock.tick(60)