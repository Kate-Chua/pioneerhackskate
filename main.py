import pygame
import random
import time

import os
pygame.init()
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 626
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Pioneer Hacks")
clock = pygame.time.Clock()
lastTime = time.time()


font = pygame.font.Font(None, 40)
messages = ["If this doesn't work I'm throwing hands", "I think it's working", "YIPPEEEEE"]
activeMessage = 0
message = messages[activeMessage]
messageLetter = font.render("", True, "white")

messageCounter = 0
messageSpeed = 3
messageDone = False

screen_shake = 500
render_offset = [0,0]
#Sprite List
parrotCawOriginal = pygame.image.load("parrotCaw.png")
parrotStillOriginal = pygame.image.load("parrotStill.png")
parrotCawMugshotOriginal = pygame.image.load("cawMugshot.png")
parrotStillMugshotOriginal = pygame.image.load("stillMugshot.png")

#animation list for player walking
class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.animationListPlayerWalk = []
        self.animationListPlayerWalk.append(pygame.image.load("Player_14.png"))
        self.animationListPlayerWalk.append(pygame.image.load("Player_15.png"))
        self.animationListPlayerWalk.append(pygame.image.load("Player_16.png"))
        self.animationListPlayerWalk.append(pygame.image.load("Player_17.png"))
        self.currentPlayerWalkSprite = 0
        self.image = self.animationListPlayerWalk[self.currentPlayerWalkSprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

#Resized Sprites
parrotCawResized = pygame.transform.scale(parrotCawOriginal, (138, 94.5))
parrotStillResized = pygame.transform.scale(parrotStillOriginal, (138, 94.5))
parrotCawMugshotResized = pygame.transform.scale(parrotCawMugshotOriginal, (130, 130))
parrotStillMugshotResized = pygame.transform.scale(parrotStillMugshotOriginal, (130, 130))
#Flipped Sprites
parrotCaw = pygame.transform.flip(parrotCawResized, True, False)
parrotStill = pygame.transform.flip(parrotStillResized, True, False)
parrotCawMugshot = pygame.transform.flip(parrotCawMugshotResized, True, False)
parrotStillMugshot = pygame.transform.flip(parrotStillMugshotResized, True, False)
#Background Sprites
backgroundOriginalSize = pygame.image.load("background.png")
background = pygame.transform.scale(backgroundOriginalSize, (1200, 626))

running = True
while running:
    dt = time.time() - lastTime
    dt *= 60
    lastTime = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: break
        if event.type == pygame.USEREVENT: message.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and messageDone and activeMessage < len(messages) - 1:
                activeMessage += 1
                messageDone = False
                message = messages[activeMessage]
                messageWidth = messageLetter.get_width()
                messageCounter = 0
    else:
        screen.blit(background, render_offset)
        screen.blit(parrotStill, (930, 310))
        screen.blit(parrotStillMugshot, (1070, 20))
        pygame.draw.rect(screen, "white", (1050, 0, 150, 150), 5)
        player = Player(10,10)
        if messageCounter < messageSpeed * len(message):
            messageCounter += 1
        elif messageCounter >= messageSpeed * len(message):
            messageDone = True
        messageLetter = font.render(message[0:messageCounter//messageSpeed], True, "white")
        messageLetterRect = messageLetter.get_rect()
        messageLetterRect.center = (SCREEN_WIDTH // 2, 60)
        screen.blit(messageLetter, messageLetterRect)
        if screen_shake > 0:
            screen_shake -= 1
        if screen_shake:
            render_offset[0] = random.randint(0, 8) - 4
            render_offset[1] = random.randint(0, 8) - 4

        pygame.display.flip()
        clock.tick(60)
        continue
    break
pygame.quit()