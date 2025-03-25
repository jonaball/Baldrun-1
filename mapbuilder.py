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
MAP_TO_EDIT = f"Prosjekt\Bald run\maps/map{currentMap}.json" # ENDRE DENNE TIL MAP DU VIL ENDRE
loadedData = loadJson(MAP_TO_EDIT)
print(loadedData)

def DisplayMap():
    for tile in loadedData:
        pos = loadedData[tile]["position"]
        if loadedData[tile]["type"] == "wall":
            pygame.draw.rect(win, (200, 200, 200), (pos[0]*tilesize, pos[1]*tilesize, tilesize, tilesize))
        elif loadedData[tile]["type"] == "parykk":
            pygame.draw.rect(win, (200, 0, 0), (pos[0]*tilesize, pos[1]*tilesize, tilesize, tilesize))


def DisplayHover():
    pos = pygame.mouse.get_pos()
    pygame.draw.rect(win, (100, 100, 100), (pos[0]-pos[0]%tilesize, pos[1]-pos[1]%tilesize, tilesize, tilesize))

def DrawMap(x):
    pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    tilepos = [pos[0]//tilesize, pos[1]//tilesize]
    type = x

    if click[0] == True:
        loadedData[f"{tilepos[0]},{tilepos[1]}"] = {"type": type, "position": tilepos}
    if click[2] == True:
        try:
            loadedData.pop(f"{tilepos[0]},{tilepos[1]}")
        except:
            print(f"No tile at {tilepos} to remove.")

tileType = "wall"
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
                MAP_TO_EDIT = f"Prosjekt\Bald run\maps/map{currentMap}.json"
                if loadJson(MAP_TO_EDIT) != None:
                    loadedData = loadJson(MAP_TO_EDIT)
                else:
                    currentMap -= 1
                    MAP_TO_EDIT = f"Prosjekt\Bald run\maps/map{currentMap}.json"
            if event.key == pygame.K_LEFT:
                if currentMap != 1:
                    # SAVE
                    saveJson(loadedData, MAP_TO_EDIT)
                    # LOAD
                    currentMap -= 1
                    MAP_TO_EDIT = f"Prosjekt\Bald run\maps/map{currentMap}.json"
                    loadedData = loadJson(MAP_TO_EDIT)
            if event.key == pygame.K_w:
                tileType = "wall"
            if event.key == pygame.K_p:
                tileType = "parykk"
            
    win.fill((0,0,0))
    DisplayMap()
    DisplayHover()
    DrawMap(tileType)
    
    pygame.display.flip()
    clock.tick(60)