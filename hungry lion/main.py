import pygame
import math
import time
import random
from pygame.locals import *
#My Global variables#################
WIDTH = 750
HEIGHT = 530
ENEMY_WIDTH = 20
ENEMY_HEIGHT = 20
POINTS_WIDTH = 20
POINTS_HEIGHT = 20
PLAYER_WIDTH = 20
PLAYER_HEIGHT = 20
START_X = 600
START_Y = 300
N_ENEMIES = 50
N_POINTS = 20
ZERO = 0
###################################
pygame.mixer.init()
#The class of the enemy blocks####################
class Enemy_block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([ENEMY_HEIGHT, ENEMY_WIDTH])
        self.image.fill((0 , 0 , 0))
        self.rect = self.image.get_rect()

    def respawn(self):
        self.rect.y = random.randrange(-300 , -20)
        self.rect.x = random.randrange(WIDTH - 20)

    def update(self):
        self.rect.y = self.rect.y + 1
        if self.rect.y >= HEIGHT + 1:
            self.respawn()

#########################################################################
#The POINTS class is the class of eatble blocks
class Points(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([POINTS_HEIGHT, POINTS_WIDTH])
        self.image.fill((255 , 255 , 0))
        self.rect = self.image.get_rect()
##############################################################################
#The characteristic and change behavior of my block
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([PLAYER_HEIGHT, PLAYER_WIDTH])
        self.image.fill((78 , 87 , 84))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #change is equal to 0 to hold the balance
        self.changing_x = ZERO
        self.changing_y = ZERO
#####################################################################################
    def speed_changing(self , x , y):
        self.changing_x = self.changing_x + x
        self.changing_y = self.changing_y + y

    def update(self):
        self.rect.x = self.rect.x + self.changing_x
        self.rect.y = self.rect.y + self.changing_y

class Game(object):  
    def __init__(self):
        self.collision = ZERO
        self.score = ZERO

        self.winning = False
        self.game_over = False

        self.blockskvat = pygame.sprite.Group()
        self.points = pygame.sprite.Group()
        self.all_blocks = pygame.sprite.Group()

        for i in range(N_ENEMIES):
            block = Enemy_block()
            block.rect.x = random.randrange(WIDTH - 20)
            block.rect.y = random.randrange(-300, HEIGHT)
            self.blockskvat.add(block)
            self.all_blocks.add(block)

        for i in range(N_POINTS):
            block = Points()
            block.rect.x = random.randrange(WIDTH - 25)
            block.rect.y = random.randrange(HEIGHT - 25)
            self.points.add(block)
            self.all_blocks.add(block)

        self.player = Player(START_X , START_Y)
        self.all_blocks.add(self.player)

    def menu_process(self):
        for event in pygame.event.get():
            #Чтобы выключить игру крестиком
            if event.type == pygame.QUIT:
                return True
            #Чтобы выключить игру клавишей ESC
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True
            #Клик мышкой для продолжения игры или рестарта
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_over == True:
                    self.__init__()
                elif self.winning == True:
                    self.__init__()
                    
            
            
            
            #Настройка кнопок управления стрелочками или же привычными для геймера w a s d
            #В моем случае w a s d нужны для максимального разгона блока
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.player.speed_changing(-4, 0)
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.player.speed_changing(4, 0)
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.player.speed_changing(0, -4)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.player.speed_changing(0, 4)
            #
            elif event.type == pygame.KEYUP:
                if event.key == (pygame.K_LEFT or pygame.K_a):
                    self.player.speed_changing(4, 0)
                elif event.key == (pygame.K_RIGHT or pygame.K_d):
                    self.player.speed_changing(-4, 0)
                elif event.key == (pygame.K_UP or pygame.K_w):
                    self.player.speed_changing(0, 4)
                elif event.key == (pygame.K_DOWN or pygame.K_s):
                    self.player.speed_changing(0, -4)

        return False
    #Here our background updates
    def back_moving(self):
        if self.game_over == False and self.winning == False:
            self.all_blocks.update()

            enemy_area = pygame.sprite.spritecollide(self.player, self.blockskvat, True)
            friendly_area = pygame.sprite.spritecollide(self.player, self.points, True)

            for block in enemy_area:
                self.collision = self.collision + 1
                if self.collision % 1 == ZERO:
                    self.score = self.score - 1
            for block in friendly_area:
                self.score = self.score + 1
            if self.score < ZERO or len(self.blockskvat) == ZERO:
                self.game_over = True
            if len(self.points) == ZERO:
                self.winning = True

    def display_frame(self, screen):
        screen.fill((255 , 255 , 255))
        font_50 = pygame.font.SysFont('Arial', 50)
        font_25 = pygame.font.SysFont('serif', 25)
        if self.game_over == True:
            render_game_over = font_50.render("This Game is OVER!", True, (255 , 0 , 0))
            render_restart = font_25.render("LEFT MOUSE to restart the game", True, (255 , 0 , 0))
            screen.blit(render_game_over, (200, 135))
            screen.blit(render_restart, (280, 315))
        if self.game_over == False:
            self.all_blocks.draw(screen)

        if self.winning == True:
            render_game_over = font_50.render("WINNING!", True, (0 , 128 , 0))
            render_restart = font_25.render("LEFT MOUSE to restart the game", True, (0 , 128 , 0))
            screen.blit(render_game_over, (200, 135))
            screen.blit(render_restart, (280, 315))

        if self.winning == False:
            self.all_blocks.draw(screen)

        render_score = font_25.render(f'Score: {self.score}', True, (255 , 77 , 0))
        screen.blit(render_score, [13, 10])
        
        pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption("Sultanbek")
    pygame.mouse.set_visible(True)
    clock = pygame.time.Clock()
    game = Game()
    running = False
    while running == False:
        running = game.menu_process()
        game.back_moving()
        game.display_frame(screen)
        clock.tick(90)
    pygame.quit()
#Вызов функций в main
if __name__ == "__main__":
    main()