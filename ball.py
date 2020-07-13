import constants
import pygame
import random

class Ball():
    """
    A class used to represent a ball

    Attributes
    ----------
    x: int
        Location of the ball along the x axis
    y: int
        Location of the ball along the y axis
    DX: int
        Change in x location. Equivalent to speed along x axis
    DY: int
        Change in y location. Equivalent to speed along y axis
    RADIUS: int
        The constant radius of the ball

    Methods
    -------
    reset()
        Resets all attributes of the ball to their default settings
    getRandSpeed() -> int
        Returns a random speed value between 2 and 4 for x and y axes
        or between -4 and -2
    setBallPos(x: int, y:int)
        Sets the x and y position of the ball
    getBallPos() -> (int, int)
        Returns the x and y position of the ball
    render(screen: Pygame object)
        Updates the drawing of the circle on the screen
    """

    def __init__(self):
        """
        Creates a ball that starts in the middle of screen
        """
        self.x = int(constants.SCREEN_WIDTH/2)
        self.y = int(constants.SCREEN_HEIGHT/2)
        self.DX = self.getRandSpeed()
        self.DY = self.getRandSpeed()
        self.RADIUS = 5

    def reset(self):
        """"
        Resets all properties of the ball
        """
        self.x = int(constants.SCREEN_WIDTH/2)
        self.y = int(constants.SCREEN_HEIGHT/2)
        self.DX = self.getRandSpeed()
        self.DY = self.getRandSpeed()

    def getRandSpeed(self) -> int:
        """
        Returns a random speed between 2 and 4, or -4 and -2.
        """
        num = int(random.uniform(-4,4))
        while(-1<=num and num<=1):
            num = int(random.uniform(-4,4))
        return num

    def setBallPos(self, x: int, y: int):
        """
        Sets the (x,y) position of the ball

        Parameters
        ----------
        x: int
            Desired x location of where to place the ball
        y: int
            Desired y location of where to place the ball
        """
        self.x = x
        self.y = y

    def getBallPos(self) -> (int,int):
        """
        Get the (x,y) position of the ball

        Returns
        -------
        (x location of ball, y location of ball)
        """
        return self.x, self.y

    # updates the screen rendering of the ball
    # pong.py will call the pygame update display method once to reduce computation
    def render(self, screen):
        """
        Updates the drawing of hte ball on the screen
        Pong.py will call the pygame updateDisplay method one time
        to reduce computation

        Parameters
        ----------
        screen: pygame object
            The Pygame screen
        """
        x,y = self.getBallPos()
        pygame.draw.circle(screen, (255, 255, 255), (x, y), self.RADIUS)
