# Import the pygame library
import pygame
import constants
from player import Player
from ball import Ball

# gameState is one of several options:
# start, play, p1Score, p2Score, p1Win, p2Win
global gameState
gameState = "start"

# Initialize pygame library and the screen
def setup():
    pygame.init()
    # Set up and return the drawing window
    return pygame.display.set_mode([constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT])

# starts the ball moving on the screen
def move(ball, player):
    x, y = ball.getBallPos()
    # first bound the y direction
    # bound on top part of screen
    if(y+ball.DY < ball.RADIUS):
        ball.DY = ball.DY * -1 #change bounce direction
    # bound on bottom part of screen
    elif(y+ball.DY > constants.SCREEN_HEIGHT - ball.RADIUS):
        ball.DY = ball.DY * -1 #change bounce direction
    # next bound the x direction when ball collides with player
    left, top = player.getPlayerPos()
    right = left + player.WIDTH
    bottom = top + player.HEIGHT
    #make sure ball is in vertical range of player's paddle
    if((y+ball.RADIUS>=top and y+ball.RADIUS <= bottom) \
        or (y-ball.RADIUS >=top and y-ball.RADIUS <= bottom)):
        #make sure ball collides horizontally with paddle
        if((left <= x+ball.RADIUS and x+ball.RADIUS <= right) \
            or (left <= x-ball.RADIUS and x-ball.RADIUS <= right)):
            ball.DX = -1*ball.DX # change bounce direction
    #always update x and y position
    x = x + ball.DX
    y = y + ball.DY
    ball.setBallPos(x,y)

# Updates the display on the screen
def updateScreen(screen, ball, p1, p2):
    # Fill the background with black
    screen.fill((0, 0, 0))
    # draw the ball and player boards
    ball.render(screen)
    p1.render(screen)
    p2.render(screen)
    # display start screen instructions
    if(gameState=="start"):
        text = font.render("Press Enter to Start", 1, (255,255,255))
        screen.blit(text,(constants.SCREEN_WIDTH/2 - 180, 50))
    pygame.display.update()


ball = Ball()
screen = setup()
p1 = Player()
p2 = Player()
p1.setPlayerPos(0, constants.SCREEN_HEIGHT//2-p1.HEIGHT)
p2.setPlayerPos(constants.SCREEN_WIDTH-p2.WIDTH,constants.SCREEN_HEIGHT//2-p2.HEIGHT)
font = pygame.font.SysFont("arial",50, bold = True) #using Arial font

# Run until the user asks to quit
running = True
while running:
    pygame.display.set_caption("Pong")
    # minimum time between frames
    pygame.time.delay(10)
    # Close window if user quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # check if game can start
    keys = pygame.key.get_pressed()
    if(gameState=="start" and keys[pygame.K_RETURN]):
        gameState = "play"

    #check for a key press and move players as necessary
    if(gameState == "play"):
        p1.updatePlayerGivenKeypress(True)
        p2.updatePlayerGivenKeypress(False)
        move(ball,p1)
        move(ball,p2)
    # Update the screen display
    updateScreen(screen, ball, p1, p2)

# Quits game after completion
pygame.quit()
