import constants
import pygame

class Player():
    """
    A class used to represent a player.
    Each player is represented as a rectangular paddle.

    Attributes
    ----------
    WIDTH: int
        Constant width of the paddle
    HEIGHT: int
        Constant height of the paddle
    SPEED: int
        Constant vertical speed of the paddle
    left: int
        X axis position of the rectangle's top left corner
    top: int
        Y axis position of the rectangle's top left corner
    score: int
        Number of points a player has


    Methods
    -------
    setPlayerPos(left: int, top: int)
        Sets the player paddle's position on the screen
    getPlayerPos() -> (int, int)
        Returns the top left coordinates of the paddle
    setScore(score: int)
        Sets the score for the player
    getScore() -> int
        Returns the player's score
    updatePlayerGivenKeypress(leftSide: bool)
        Updates the specified player's paddle position given keyboard input
    render(screen: Pygame object)
        Updates the drawing of the player paddle on the screen
    """

    def __init__(self):
        """
        Creates a rectangular paddle for a player.
        Paddle dimensions and speed are fixed.
        Paddle placement initialized later for the players.
        """
        self.WIDTH = 10 #paddle width
        self.HEIGHT = 100 #paddle height
        self.SPEED = 10 #how fast paddle can move
        # will change once placed on left or right half of playing field
        # specifies top left coordinate of the rectangle
        self.left = -100 #can have a value of 0 or constants.SCREEN_WIDTH-self.WIDTH
        self.top = -100
        self.score = 0

    def setPlayerPos(self, left: int, top: int):
        """
        Sets the location of the rectangular paddle.
        Ensures that the paddles are placed on the screen.

        Parameters
        ----------
        left: int
            X axis position of the rectangle's top left corner
        top: int
            Y axis position of the rectangle's top left corner
        """
        assert left==0 or left==(constants.SCREEN_WIDTH-self.WIDTH)
        assert top >=0 and top <= constants.SCREEN_HEIGHT-self.HEIGHT
        self.left = left
        self.top = top

    def getPlayerPos(self) -> (int, int):
        """
        Gets the top left coordinate of the rectangle

        Returns
        -------
        (Rectangle's top left corner's X coordinate,
        Rectangle's top left corner's Y coordinate)
        """
        return self.left,self.top


    def setScore(self, score: int):
        """
        Sets player's score

        Parameters
        ----------
        score: int
            Player's score for the game
        """
        assert score >= 0
        self.score = score

    def getScore(self) -> int:
        """
        Get the player's score

        Returns
        -------
        Game score of the player
        """
        return self.score


    def updatePlayerGivenKeypress(self, leftSide: bool):
        """
        Update the position of the player given keyboard input.
        Keys "W" and "S" move Player 1 up and down on the left half of the screen.
        Up and down arrows move Player 2 up and down on the right half of the screen.

        Parameters
        ---------
        leftSide: bool
            True for setting controls of Player 1 on the left side of the screen.
            False for setting controls of Player 2 on the right side of the screen.
        """
        left,top = self.getPlayerPos()
        keys = pygame.key.get_pressed()
        # for the left side player
        if leftSide:
            if keys[pygame.K_w]:
                top = max(0,top-self.SPEED)
            elif keys[pygame.K_s]:
                top = min(top + self.SPEED, constants.SCREEN_HEIGHT - self.HEIGHT)
        # for the right side player
        else:
            if keys[pygame.K_UP]:
                top = max(0,top-self.SPEED)
            elif keys[pygame.K_DOWN]:
                top = min(top + self.SPEED, constants.SCREEN_HEIGHT - self.HEIGHT)
        self.setPlayerPos(left,top)

    def render(self, screen):
        """
        Updates the drawing of the player paddle on the screen.
        pong.py will call the pygame update display method once to reduce computation

        Parameters
        ----------
        screen: Pygame object
            The Pygame screen the game itself is played on.
        """
        left, top = self.getPlayerPos()
        pygame.draw.rect(screen, (255, 255, 255), (left, top, self.WIDTH, self.HEIGHT))
