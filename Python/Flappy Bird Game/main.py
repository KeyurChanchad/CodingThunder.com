from harry.main import GROUNDY, mainGame, welcomeScreen
import random   # For generating random  number 
import pygame
import sys
from pygame.locals import *

#Globle variable for the Game
FPS = 32    # Frames per seconds means in one second how many images blit(show on screen) on screen   
SCREEN_WIDTH = 289
SCREEN_HEIGHT = 511
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  #Initialize screen or window for display
GROUNDY = SCREEN_HEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUND = {}
BACKGROUND = 'gallery/sprites/background.png'
PLAYER = 'gallery/sprites/bird.png'
MESSAGE = 'gallery/sprites/message.png'
PIPE = 'gallery/sprites/pipe.png'

def welcomeScreen():
    playerx = int(SCREEN_WIDTH/5)
    playery = int((SCREEN_HEIGHT - GAME_SPRITES['player'].get_height())/2)
    messagex = int((SCREEN_WIDTH - GAME_SPRITES['message'].get_width())/2)
    messagey = int(SCREEN_HEIGHT * 0.13)
    basex = 0
    while True:
        # pygame.event.get() it just do that you press any key in keyboard and click by mouse that track  
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP ):
                return
            
            else:
                SCREEN.blit(GAME_SPRITES['background'],(0,0))
                SCREEN.blit(GAME_SPRITES['player'],(playerx, playery))
                SCREEN.blit(GAME_SPRITES['message'],(messagex, messagey))
                SCREEN.blit(GAME_SPRITES['base'],(basex, GROUNDY))
                pygame.display.update()
                FPSCLOCK.tick(FPS)

    

# if __name__ == '__main__': It executed when it run from this particular file
if __name__ == '__main__':
    pygame.init()
    FPSCLOCK =  pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird by Keyur Chanchad')
    # convert.alpha() is do in screen blit faster executable, image become otimize/capable for game
    GAME_SPRITES['number'] = (
        pygame.image.load('gallery/sprites/0.png').convert_alpha(),
        pygame.image.load('gallery/sprites/1.png').convert_alpha(),
        pygame.image.load('gallery/sprites/2.png').convert_alpha(),
        pygame.image.load('gallery/sprites/3.png').convert_alpha(),
        pygame.image.load('gallery/sprites/4.png').convert_alpha(),
        pygame.image.load('gallery/sprites/5.png').convert_alpha(),
        pygame.image.load('gallery/sprites/6.png').convert_alpha(),
        pygame.image.load('gallery/sprites/7.png').convert_alpha(),
        pygame.image.load('gallery/sprites/8.png').convert_alpha(),
        pygame.image.load('gallery/sprites/9.png').convert_alpha()
    )
    
    GAME_SPRITES['message'] = pygame.image.load(MESSAGE).convert_alpha()
    GAME_SPRITES['pipe'] = ( pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(),180), 
    pygame.image.load(PIPE).convert_alpha() )
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()
    GAME_SPRITES['base'] = pygame.image.load('gallery/sprites/base.png').convert()


    
    # Game Sounds
    GAME_SOUND['die'] = pygame.mixer.Sound('gallery/audio/die.wav')
    GAME_SOUND['hit'] = pygame.mixer.Sound('gallery/audio/hit.wav')
    GAME_SOUND['point'] = pygame.mixer.Sound('gallery/audio/point.wav')
    GAME_SOUND['swoosh'] = pygame.mixer.Sound('gallery/audio/swoosh.wav')
    GAME_SOUND['wing'] = pygame.mixer.Sound('gallery/audio/wing.wav')

    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
    while True:
        welcomeScreen()
        mainGame()

    
            
    

    


