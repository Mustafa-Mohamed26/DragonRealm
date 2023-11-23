import pygame
import random

# Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((1200, 700))

# Title and Icon
pygame.display.set_caption("Dragon Realm")
icon = pygame.image.load("dragon-icon.png")
pygame.display.set_icon(icon)

# Background
mainCave = pygame.image.load("caves.jpg")
caveInter = pygame.image.load("caveInter.jpg")

# objects
dragon = pygame.image.load("dragon.png")
treasure = pygame.image.load("treasure.png")

# game font
font = pygame.font.Font('freesansbold.ttf', 35)


# Game Intro Text
def intro_text():
    text1 = font.render('You are in a land full of dragons. In front of you,', True, (255, 255, 255))
    screen.blit(text1, (200, 250))

    text2 = font.render('you see two caves. In one cave, the dragon is friendly,', True, (255, 255, 255))
    screen.blit(text2, (200, 300))

    text3 = font.render('and will share his treasure with you. The other dragon', True, (255, 255, 255))
    screen.blit(text3, (200, 350))

    text4 = font.render('is greedy and hungry, and will eat you on sight.', True, (255, 255, 255))
    screen.blit(text4, (200, 400))

    text5 = font.render("choose on of the two caves press 1 or 2", True, (255, 255, 255))
    screen.blit(text5, (200, 450))


# Game Win Text
def win():
    text1 = font.render("you are win the treasure", True, (255, 255, 255))
    screen.blit(text1, (350, 500))

    text2 = font.render("press space to play again", True, (255, 255, 255))
    screen.blit(text2, (350, 550))


# Game Lose Text
def lose():
    text1 = font.render("you have been eaten by the dragon", True, (255, 255, 255))
    screen.blit(text1, (275, 600))

    text2 = font.render("press space to play again", True, (255, 255, 255))
    screen.blit(text2, (350, 650))


cave1 = True
cave2 = False


# Game loop
running = True
while running:
    # RGB - Red, Green, Blue background color
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                cave1 = False
                cave2 = True
                # random value
                chosen_cave = random.randint(1, 2)

            if event.key == pygame.K_2:
                cave1 = False
                cave2 = True
                # random value
                chosen_cave = random.randint(1, 2)

            if event.key == pygame.K_SPACE:
                cave1 = True
                cave2 = False

    # background image
    if cave1:
        screen.blit(mainCave, (0, 0))
        intro_text()
    if cave2:
        screen.blit(caveInter, (0, 0))
        if chosen_cave == 1:
            screen.blit(treasure, (300, 50))
            win()
        else:
            screen.blit(dragon, (0, 0))
            lose()

    pygame.display.update()
