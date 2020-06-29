import constants
import pygame
# class for the pong ball
class Ball():
    # creates a ball that starts in the middle of screen
    def __init__(self):
        self.x = int(constants.SCREEN_WIDTH/2)
        self.y = int(constants.SCREEN_HEIGHT/2)
        self.SPEED = 5
        self.RADIUS = 20

    # set (x,y) position of the ball
    def setBallPos(self,x,y):
        assert x>=0 and x<=constants.SCREEN_WIDTH
        assert y>=0 and y<=constants.SCREEN_HEIGHT
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
