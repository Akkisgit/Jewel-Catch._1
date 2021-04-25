import pgzrun
import pygame
import random
HEIGHT = 400
WIDTH = 400
rocket = Actor("small_rocket")
rocket._surf = pygame.transform.scale(rocket._surf, (rocket.width * 2, rocket.height * 2))
rocket._rect.width *= 2
rocket._rect.height *= 2
rocket.bottom = 0
rocket.bottom = 400
xspeed = 2
yspeed = 2
score = 0
j = random.randint(0,400)
c = random.randint(0,400)
jewels = []
bombs = []
for i in range(4):
    jewel = Actor("diamond_s")
    jewel.posxspeed = 1
    jewel.posyspeed = 1
    jewel.negxspeed = -1
    jewel.negyspeed = -1
    jewel.xspeed = jewel.posxspeed
    jewel.yspeed = jewel.posyspeed
    jewels.append(jewel)
    jewel.x = j
for i in range(3):
    bomb = Actor("bomb")
    bomb.bposxspeed = 2
    bomb.bposyspeed = 2
    bomb.bnegxspeed = -2
    bomb.bnegyspeed = -2
    bomb.xspeed = bomb.bposxspeed
    bomb.yspeed = bomb.bposyspeed
    bombs.append(bomb)
    bomb.x = c
def draw():
    screen.fill("red")
    rocket.draw()
    for jewel in jewels:
        jewel.draw()
    for bomb in bombs:
        bomb.draw()
    screen.draw.text("Score: " + str(score), (0, 0))
def update():
    for diamonds in jewels:
        global xspeed,yspeed,score,j,c
        diamonds.x += diamonds.xspeed
        diamonds.y += diamonds.yspeed
        if diamonds.right >= WIDTH:
            diamonds.xspeed = diamonds.negxspeed
        if diamonds.left <= 0:
            diamonds.xspeed = diamonds.posxspeed
        if diamonds.top <= 0:
            diamonds.yspeed = diamonds.posyspeed
    for explosives in bombs:
        global xspeed,yspeed
        explosives.x += explosives.xspeed
        explosives.y += explosives.yspeed
        if explosives.right >= WIDTH:
            explosives.xspeed = explosives.bnegxspeed
        if explosives.left <= 0:
            explosives.xspeed = explosives.bposxspeed
        if explosives.top <= 0:
            explosives.yspeed = explosives.bposyspeed
    for l in range(4):
        if jewels[l].y >= 400:
            j = 25
            for l in range(4):
                jewels[l].x = j
                jewels[l].y = 0
                j = random.randint(0,400)
        for l in range(3):
            if bombs[l].y >= 400:
                c = random.randint(0,400)
                for l in range(3):
                    bombs[l].x = c
                    bombs[l].y = 0
                    c += 75
    if keyboard.right:
        rocket.x += 10
    if keyboard.left:
        rocket.x -= 10
    if rocket.x > 400:
        rocket.x = 0
    if rocket.x < 0:
        rocket.x = 399
    if jewels[0].colliderect(rocket) == True:
        score += 5
        jewels[0].x = j
    if jewels[1].colliderect(rocket) == True:
        score += 5
        jewels[1].x = j
    if jewels[2].colliderect(rocket) == True:
        score += 5
        jewels[2].x = j
    if jewels[3].colliderect(rocket) == True:
        score += 5
        jewels[3].x = j
    if bombs[0].colliderect(rocket) == True:
        score += -10
        bombs[0].x = c
    if bombs[1].colliderect(rocket) == True:
        score += -10
        bombs[1].x = c
    if bombs[2].colliderect(rocket) == True:
        score += -10
        bombs[2].x = c
pgzrun.go()