import constants
import pygame
import random
# class for the pong ball
class Ball():
    # creates a ball that starts in the middle of screen
    def __init__(self):
        self.x = int(constants.SCREEN_WIDTH/2)
        self.y = int(constants.SCREEN_HEIGHT/2)
        self.DX = self.getRandSpeed()
        self.DY = self.getRandSpeed()
        self.RADIUS = 5

    #resets all properties of the ball
    def reset(self):
        self.x = int(constants.SCREEN_WIDTH/2)
        self.y = int(constants.SCREEN_HEIGHT/2)
        self.DX = self.getRandSpeed()
        self.DY = self.getRandSpeed()

    # get a random velocity
    # if random number is 0, set it to something else
    def getRandSpeed(self):
        num = int(random.uniform(-4,4))
        while(-1<=num and num<=1):
            num = int(random.uniform(-4,4))
        return num

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
