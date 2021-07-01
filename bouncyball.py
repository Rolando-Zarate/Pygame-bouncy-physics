import pygame
import random
pygame.init()
window = pygame.display.set_mode((600,500))
clock = pygame.time.Clock()
ballevent = "leftup"
ballx = 300
bally = 450
font = pygame.font.SysFont("Arial",20)
def bouncyphysics():
    global ballx,bally,ballevent
    if ballevent == "leftup":
        if ballx < 5:
            ballevent = "rightup"
        elif bally < 5:
            rand = random.randint(1,2)
            if rand == 1:
                ballevent = "leftup"
            else:
                ballevent = "leftdown"
        else:
            randx = random.randint(4,5)
            randy = random.randint(4,5)
            ballx -= randx
            bally -= randy
            pygame.draw.circle(window,(255,255,255),(ballx + 1,bally + 1),20)
    elif ballevent == "leftdown":
        if bally > 400:
            ballevent = "leftup"
        elif ballx < 5:
            rand = random.randint(1,2)
            if rand == 1:
                ballevent = "rightup"
            else:
                ballevent = "rightdown"
        else:
            randx = random.randint(4,5)
            randy = random.randint(4,5)
            ballx -= randx
            bally += randy
            pygame.draw.circle(window,(255,255,255),(ballx + 1,bally + 1),20)
    elif ballevent == "rightup":
        if bally < 5:
            ballevent = "rightdown"
        else:
            randx = random.randint(4,5)
            randy = random.randint(4,5)
            ballx += randx
            bally -= randy
            pygame.draw.circle(window,(255,255,255),(ballx + 1,bally + 1),20)
    elif ballevent == "rightdown":
        if ballx > 600:
            rand = random.randint(1,2)
            if rand == 1:
                ballevent = "leftup"
            else:
                ballevent = "leftdown"
        elif bally > 500:
            rand = random.randint(1,2)
            if rand == 1:
                ballevent = "leftup"
            else:
                ballevent = "rightdown"
        else:
            randx = random.randint(4,5)
            randy = random.randint(4,5)
            ballx += randx
            bally += randy
            pygame.draw.circle(window,(255,255,255),(ballx + 1,bally + 1),20)
def bouncyball():
    pygame.display.set_caption("Bouncy Physics")
    window.fill((20,20,20))
    pygame.draw.circle(window,(190,190,190),(ballx,bally),20)
    window.blit(font.render("Bouncy Physics by Rolando Zarate",True,(255,255,255),(20,20,20)),(10,10))
    window.blit(font.render("Apache License v2",True,(255,255,255),(20,20,20)),(10,35))
    bouncyphysics()
def update():
    pygame.display.update()
    clock.tick(60)
def main():
    while True:
        update()
        bouncyball()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
if __name__ == "__main__":
    main()
