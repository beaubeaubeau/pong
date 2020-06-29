import constants
import pygame
# creates a player object i.e. a rectangular paddle
class Player():
    def __init__(self):
        self.WIDTH = 5 #paddle width
        self.HEIGHT = 100 #paddle height
        self.SPEED = 10 #how fast paddle can move
        # will change once placed on left or right half of playing field
        # specifies top left coordinate of the rectangle
        self.left = -100 #can have a value of 0 or constants.SCREEN_WIDTH-self.WIDTH
        self.top = -100

    # sets the location of the rectangular paddles
    def setPlayerPos(self,left,top):
        assert left==0 or left==(constants.SCREEN_WIDTH-self.WIDTH)
        assert top >=0 and top <= constants.SCREEN_HEIGHT-self.HEIGHT
        self.left = left
        self.top = top

    # gets the top left coordinate of the rectangle
    def getPlayerPos(self):
        return self.left,self.top

    # update the position of the player given key input
    # takes boolean input leftSide, which determines player
    # position on screen as well as player controls
    def updatePlayerGivenKeypress(self, leftSide):
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

    # updates the screen rendering of the player
    # pong.py will call the pygame update display method once to reduce computation
    def render(self, screen):
        left, top = self.getPlayerPos()
        pygame.draw.rect(screen, (255, 255, 255), (left, top, self.WIDTH, self.HEIGHT))
