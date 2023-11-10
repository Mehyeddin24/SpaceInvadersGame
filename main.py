import time

import pygame
from pygame import mixer
import random
import math

pygame.init()
gameRunning = True
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("alienlogo.png")
pygame.display.set_icon(icon)

playerImage = pygame.image.load("arcade-game.png")
playerX = 370
playerY = 480
playerX_change = 0

enemyImage = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
numberofenemies = 10

for i in range(numberofenemies):
    enemyImage.append(pygame.image.load("mob.png"))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.3)
    enemyY_change.append(40)

bulletImage = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 3
bullet_state = "ready"

background = pygame.image.load("space.png")

score = 0
font = pygame.font.Font('mehyeddinistfont.ttf', 50)
textX = 10
textY = 10

randomtX = 450
randomtY = 9

winX = 10
winY = 10

gameoverfont = pygame.font.Font("mehyeddinistfont.ttf", 70)
randomtext = pygame.font.Font("font2.ttf", 40)
wintextfont = pygame.font.Font("font2.ttf", 150)

def printScore(x, y):
    pscore = font.render("Score : " + str(score), True, (255, 255, 255))
    screen.blit(pscore, (x, y))

def getrandomtext(x, y):
    rtext = randomtext.render("Kill 30 Enemies!", True, (255, 255, 255))
    screen.blit(rtext, (x, y))

def player(x, y):
    screen.blit(playerImage, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImage[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImage, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

def gameovertext():
    gotext = gameoverfont.render("GAME OVER!", True, (255, 255, 255))
    screen.blit(gotext, (200, 250))

def youwin():
    wintext = wintextfont.render("YOU WIN!", True, (255, 255, 255))
    screen.blit(wintext, (130, 165))

while gameRunning:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    line = pygame.image.load("redline.png")
    scaled_image = pygame.transform.scale(line, (1000, 100))
    screen.blit(scaled_image, (-30, 380))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletsound = pygame.mixer.Sound("bulletsound.wav")
                    bulletsound.set_volume(0.1)
                    bulletsound.play()
                    bulletX = playerX
                    fire_bullet(playerX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX = playerX + playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    for i in range(numberofenemies):
        if score >= 30:
            for j in range(numberofenemies):
                enemyY[j] = -2900
            youwin()
            break
    for i in range(numberofenemies):
        if enemyY[i] > 380:
            for j in range(numberofenemies):
                enemyY[j] = 2000
            gameovertext()
            break
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]

        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosionSound = mixer.Sound("bulletexp.wav")
            explosionSound.play()
            bulletY = 480
            bullet_state = "ready"
            score += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    printScore(textX, textY)
    getrandomtext(randomtX, randomtY)
    pygame.display.update()
