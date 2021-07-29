import pygame
import random
import time
from pygame.locals import *
SIZE = 40
background_color = (255 , 255 , 255)
game_over_color = (255 , 0 , 0)

class Food:
    def __init__(self , main_screen):
        self.image = pygame.image.load("res/food.jpg").convert()
        self.main_screen = main_screen
        self.x = SIZE * 3
        self.y = SIZE * 3
    def draw(self):
        self.main_screen.blit(self.image , (self.x , self.y))
        pygame.display.flip()
    def teleport(self):
        self.x = random.randint(0 , 24) * SIZE
        self.y = random.randint(0 , 19) * SIZE

class Jylan:
    def __init__(self , main_screen , length):
        #конвертируем блок из папки res
        self.length = length
        self.main_screen = main_screen

        self.block = pygame.image.load("res/block.jpg").convert()
        self.x = [SIZE] * length
        self.y = [SIZE] * length
        self.direction = "up"
    def length_increment(self):
        self.length = self.length + 1
        self.x.append(-1)
        self.y.append(-1)
    def draw(self):
        self.main_screen.fill(background_color) #also needs for clearing the screen
        for i in range(self.length):
            self.main_screen.blit(self.block , (self.x[i] , self.y[i]))
        pygame.display.flip()
    def go_up(self):
        self.direction = "up"
    def go_down(self):
        self.direction = "down"
    def go_right(self):
        self.direction = "right"
    def go_left(self):
        self.direction = "left"
    #функция продолжительности нажатия стрелок
    def going(self):
        for i in range(self.length - 1 , 0 , -1):
            #current block's position is a previous block's position
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == "down":
            self.y[0] = self.y[0] + SIZE
        if self.direction == "up":
            self.y[0] = self.y[0] - SIZE
        if self.direction == "right":
            self.x[0] = self.x[0] + SIZE
        if self.direction == "left":
            self.x[0] = self.x[0] - SIZE
        self.draw()
class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000 , 800))
        self.surface.fill((255 , 255 , 255))
        self.snake = Jylan(self.surface , 1)
        self.snake.draw()
        self.food = Food(self.surface)
        self.food.draw()
    def collision(self , x1 , y1 , x2 , y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def play(self):
        self.snake.going()
        self.food.draw()
        self.show_score()
        pygame.display.flip()
        # colision between snake and food
        if self.collision(self.snake.x[0] , self.snake.y[0] , self.food.x , self.food.y):
            self.snake.length_increment()
            self.food.teleport()
        # jylan is colliding himself
        for i in range(1 , self.snake.length):
            if self.collision(self.snake.x[0] , self.snake.y[0] , self.snake.x[i] , self.snake.y[i]):
                raise "Game over"


    def show_score(self):
        #include font module
        font = pygame.font.SysFont('arial' , 30)
        scores = font.render(f"scores: {self.snake.length}", True, (200 , 200 , 200))
        self.surface.blit(scores , (800 , 10))
    def gameover_show(self):
        self.surface.fill(background_color)
        font = pygame.font.SysFont('arial' , 30)
        text1 = font.render(f"This Game is over! Total scores: {self.snake.length}" , True , game_over_color)
        self.surface.blit(text1 , (200 , 300))
        text2 = font.render("Press enter to replay, to exit press esc", True, game_over_color)
        self.surface.blit(text2 , (200 , 350))
        pygame.display.flip()
    def reload(self):
        self.snake = Jylan(self.surface , 1)
        self.food = Food(self.surface)
    def run(self):
        #on - переменная которая отвечает за то чтобы окно приложения было отрыто
        on = True
        pause = False
        while on :
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                #когда нажимаем на esc наше окно закрывается  
                    if event.key == K_ESCAPE:
                        on = False
                    if event.key == K_RETURN:
                        pause = False
                #coordinate movement.Движемся на координаты и рисуем наш блок
                    if not pause:
                        if event.key == K_UP:
                            self.snake.go_up()
                        if event.key == K_DOWN:
                            self.snake.go_down()
                        if event.key == K_RIGHT:
                            self.snake.go_right()
                        if event.key == K_LEFT:
                            self.snake.go_left()

        #когда нажимаем на крестик окно закрывается
                elif event.type == QUIT:
                    on = False
            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.gameover_show()
                pause = True
                self.reload()
            time.sleep(0.3)
#my blockdraw function for drawing the block. Тоже самое что и снизу в виде функций
'''
def blockdraw():
    surface.fill((255 , 255 , 255)) #also needs for clearing the screen
    surface.blit(block, (block_x, block_y))
    pygame.display.flip()
'''
if __name__ == "__main__":
    game = Game()
    game.run()
'''
#blit funtion for drawing the image on our surface
surface.blit(block, (block_x, block_y))
pygame.display.flip()
'''

