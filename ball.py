import constants
import pygame
import random
# class for the pong ball
class Ball():
    # creates a ball that starts in the middle of screen
    def __init__(self):
        self.x = int(constants.SCREEN_WIDTH/2)
        self.y = int(constants.SCREEN_HEIGHT/2)
        #if random number is 0, set it to something else
        self.DX = int(random.uniform(-4,4))
        if(self.DX==0):
            self.DX = 2
        self.DY = int(random.uniform(-4,4))
        if(self.DY == 0):
            self.DY = -2
        self.RADIUS = 5
        self.score = 0

    # set (x,y) position of the ball
    def setBallPos(self,x,y):
        #assert x>=0 and x<=constants.SCREEN_WIDTH
        #assert y>=0 and y<=constants.SCREEN_HEIGHT
        self.x = x
        self.y = y

    # get the (x,y) position of the ball
    def getBallPos(self):
        return self.x, self.y

    # updates the screen rendering of the ball
    # pong.py will call the pygame update display method once to reduce computation
    def render(self, screen):
        x,y = self.getBallPos()
        pygame.draw.circle(screen, (255, 255, 255), (x, y), self.RADIUS)



    # # checks for key press and moves ball
    # def updateBallGivenKeypress(ball):
    #     x,y = ball.getBallPos()
    #     keys = pygame.key.get_pressed()
    #     if keys[pygame.K_UP]:
    #         y = max(y - ball.SPEED, ball.RADIUS)
    #     elif keys[pygame.K_DOWN]:
    #         y = min(y + ball.SPEED, constants.SCREEN_HEIGHT - ball.RADIUS)
    #     elif keys[pygame.K_RIGHT]:
    #         x = min(x + ball.SPEED, constants.SCREEN_WIDTH - ball.RADIUS)
    #     elif keys[pygame.K_LEFT]:
    #         x = max(x - ball.SPEED, ball.RADIUS)
    #     ball.setBallPos(x,y)
