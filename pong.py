# Import the pygame library
import pygame
import constants
from player import Player
from ball import Ball

# Initialize pygame library and the screen
def setup():
    pygame.init()
    # Set up and return the drawing window
    return pygame.display.set_mode([constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT])

# Updates the display on the screen
def updateScreen(screen, ball, p1, p2):
    # Fill the background with black
    screen.fill((0, 0, 0))
    # draw the ball and player boards
    ball.render(screen)
    p1.render(screen)
    p2.render(screen)
    pygame.display.update()


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

ball = Ball()
screen = setup()
p1 = Player()
p2 = Player()
p1.setPlayerPos(0, constants.SCREEN_HEIGHT//2-p1.HEIGHT)
p2.setPlayerPos(constants.SCREEN_WIDTH-p2.WIDTH,constants.SCREEN_HEIGHT//2-p2.HEIGHT)
# Run until the user asks to quit
running = True
while running:
    # minimum time between frames
    pygame.time.delay(10)
    # Close window if user quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #check for a key press and move players as necessary
    p1.updatePlayerGivenKeypress(True)
    p2.updatePlayerGivenKeypress(False)
    # Update the screen display
    updateScreen(screen, ball, p1, p2)

# Quits game after completion
pygame.quit()
