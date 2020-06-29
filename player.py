import constants
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
