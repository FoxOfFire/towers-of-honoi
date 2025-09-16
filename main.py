import pygame
from typing import List, Tuple
from random import randint

TOWER_HEIGHT = 10

def main() -> None:
    towers = [0 for i in range(TOWER_HEIGHT)]
    print(towers)
    pygame.init()
    window_dimension = (1920, 1080)
    
    if window_dimension not in pygame.display.list_modes():
        raise RuntimeError("Screen is not supported")

    pygame.display.set_mode(
        size=window_dimension,
        flags=pygame.DOUBLEBUF | pygame.FULLSCREEN,
    )
    clock = pygame.time.Clock()

    display = pygame.display.get_surface()
    plays = calc_honoi(TOWER_HEIGHT,0,2,1)
    for f, t in plays: 
        move_elem(towers,f,t)
        display.fill((10,10,10))
        t = [0,0,0]
        for j in range(TOWER_HEIGHT):
            make_box(towers[j],t[towers[j]],TOWER_HEIGHT - j,display)
            t[towers[j]] += 1
        pygame.display.flip()
        clock.tick(30)

def calc_honoi(height:int, f:int, t:int,h:int)->List[Tuple[int,int]]:
    if height == 1:
        return [(f,t)]
    else:
        return calc_honoi(height-1,f,h,t) + [(f,t)] + calc_honoi(height-1,h,t,f)

def make_box(tower:int,pos:int,width:int,display:pygame.Surface)->None:
    surf = pygame.Surface((20 +width*20,20))
    surf.fill((200,200,200))
    display.blit(surf,surf.get_rect(center=(300+tower*400,300-pos*20)))

def move_elem(towers: List[int], f: int, t: int)->None:
    target = -1
    if f == t:
        return
    for j in range(TOWER_HEIGHT):
        i = TOWER_HEIGHT-1-j
        if towers[i] == t:
            if target == -1:
                return
            else:
                break
        if towers[i] == f and target == -1:
            target = i
    towers[target] = t

if __name__ == "__main__":
    main()
