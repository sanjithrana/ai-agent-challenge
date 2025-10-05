import time
import time
import pygame   # this pygame is used for creating a game
from pygame.locals import*
import time

SIZE = 43

class Apple:
    def __int__(self):
        pass
class Snake:
    def __init__(self, surface, length):
        self.length = length
        self.Screen_one = surface
        self.block = pygame.image.load("th123.jpg").convert()  # image of the game like a snake.
        self.x = [SIZE]*length
        self.y = [SIZE]*length
        self.direction = 'up'
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def draw(self):
        self.Screen_one.fill((148, 236, 156))  # color
        for i in range(self.length):
            self.Screen_one.blit(self.block, (self.x[i], self.y[i])) # this the function to move the x ,y directions
        pygame.display.flip()

    def walk(self):

        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE

        self.draw()



class Game:
    def __init__(self):
        pygame.init()  # we have to init the pygame this the imp step to control the game
        self.surface = pygame.display.set_mode((1000, 800))  # ''' display property , we can use different screen by change the x,y directions'''
        self.surface.fill((148, 236, 156))  # color
        self.snake = Snake(self.surface, 6)
        self.snake.draw()

    def run(self):

        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:  # this key is to exit while we press escape.
                        running = False
                    if event.key == K_UP:  # key up use for move upward
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                    if event.key == K_LEFT:  # key up use for move upward
                        self.snake.move_left()
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                elif event.type == QUIT:  # quit is to exit directly by pressing close.
                    running = False

            self.snake.walk()
            time.sleep(0.4)


if __name__ == "__main__":
    game = Game()
    game.run()

