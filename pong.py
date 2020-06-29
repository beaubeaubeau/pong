# Import the pygame library
import pygame
import constants
from player import Player
from ball import Ball

# Initialize pygame library and set up screen
def setup():
    pygame.init()
    # Set up the drawing window
    return pygame.display.set_mode([constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT])

# Updates the display on the SCREEN_WIDTH
def updateScreen(screen, ball, p1, p2):
    # Fill the background with black
    screen.fill((0, 0, 0))
    x,y = ball.getBallPos()
    left1, top1 = p1.getPlayerPos()
    left2, top2 = p2.getPlayerPos()
    # draw the ball
    pygame.draw.circle(screen, (255, 255, 255), (x, y), ball.RADIUS)
    pygame.draw.rect(screen, (255, 255, 255), (left1, top1, p1.WIDTH, p1.HEIGHT))
    pygame.draw.rect(screen, (255, 255, 255), (left2, top2, p2.WIDTH, p2.HEIGHT))
    pygame.display.update()


# checks for key press and moves ball
def updateBallGivenKeypress(ball):
    x,y = ball.getBallPos()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y = max(y - ball.SPEED, ball.RADIUS)
    elif keys[pygame.K_DOWN]:
        y = min(y + ball.SPEED, constants.SCREEN_HEIGHT - ball.RADIUS)
    elif keys[pygame.K_RIGHT]:
        x = min(x + ball.SPEED, constants.SCREEN_WIDTH - ball.RADIUS)
    elif keys[pygame.K_LEFT]:
        x = max(x - ball.SPEED, ball.RADIUS)
    ball.setBallPos(x,y)

#checks for key press and moves player
def updatePlayerGivenKeypress(p1,p2):
    left1,top1 = p1.getPlayerPos()
    left2,top2 = p2.getPlayerPos()

    keys = pygame.key.get_pressed()
    # process keys for player 1
    if keys[pygame.K_w]:
        if(top1 - p1.SPEED < 0):
            top1 = 0
        else:
            top1 = top1 - p1.SPEED
    elif keys[pygame.K_s]:
        top1 = min(top1 + p1.SPEED, constants.SCREEN_HEIGHT - p1.HEIGHT)

    # process keys for player 2
    if keys[pygame.K_UP]:
        if(top2 - p2.SPEED < 0):
            top2 = 0
        else:
            top2 = top2 - p2.SPEED
    elif keys[pygame.K_DOWN]:
        top2 = min(top2 + p2.SPEED, constants.SCREEN_HEIGHT - p2.HEIGHT)

    p1.setPlayerPos(left1,top1)
    p2.setPlayerPos(left2,top2)



ball = Ball()
screen = setup()
p1 = Player()
p2 = Player()
p1.setPlayerPos(0, constants.SCREEN_HEIGHT//2-p1.HEIGHT)
p2.setPlayerPos(constants.SCREEN_WIDTH-p2.WIDTH,constants.SCREEN_HEIGHT//2-p2.HEIGHT)
# Run until the user asks to quit
running = True
while running:
    # get ball position
    x,y = ball.getBallPos()
    # minimum time between frames
    pygame.time.delay(10)

    # Close window if user quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #check for a key press and move ball as necessary
    updatePlayerGivenKeypress(p1,p2)

    # Update the screen display
    updateScreen(screen, ball, p1, p2)

# Quits game after completion
pygame.quit()
