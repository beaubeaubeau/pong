# Import the pygame library
import pygame
import constants
from player import Player
from ball import Ball

# gameState is one of several options:
# start, play, score, win
global gameState
gameState = "start"

# Initialize pygame library and the screen
def setup():
    pygame.init()
    # Set up and return the drawing window
    return pygame.display.set_mode([constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT])

# starts the ball moving on the screen and handles collisions
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

# checks if a player has scored
def checkForGoal(ball,p1,p2):
    x,y = ball.getBallPos()
    left = x-ball.RADIUS
    right = x+ball.RADIUS
    #player 1 on the left has been scored on
    if(left < 0):
        p2Score = p2.getScore()
        p2.setScore(p2Score+1)
        return True
    #player 2 on the right has been scored on
    if(right > constants.SCREEN_WIDTH):
        p1Score = p1.getScore()
        p1.setScore(p1Score+1)
        return True
    return False

def displayStartScreen(screen):
    text = font.render("Press Enter to Start", 1, (255,255,255))
    screen.blit(text,(constants.SCREEN_WIDTH/2 - 180, 50))

def displayScoreScreen(screen, p1Score, p2Score):
    text = font.render("Player 1: "+str(p1Score)+"     Player 2: "\
        +str(p2Score), 1, (255,255,255))
    screen.blit(text,(constants.SCREEN_WIDTH/2 - 220, 50))
    text = font.render("Press Space to Cont.", 1, (255,255,255))
    screen.blit(text,(constants.SCREEN_WIDTH/2 - 200, constants.SCREEN_HEIGHT-200))

def displayWinnerScreen(screen, p1, p2):
    winner = "Player 1"
    if(p2.getScore()==constants.POINTS_TO_WIN):
        winner = "Player 2"
    text = font.render("Player 1: "+str(p1.getScore())+"     Player 2: "\
        +str(p2.getScore()), 1, (255,255,255))
    screen.blit(text,(constants.SCREEN_WIDTH/2 - 220, 50))
    text = font.render(winner + " wins!", 1, (255,255,255))
    screen.blit(text,(constants.SCREEN_WIDTH/2 - 140, 200))
    text = font.render("Press Enter to Restart", 1, (255,255,255))
    screen.blit(text,(constants.SCREEN_WIDTH/2 - 200, constants.SCREEN_HEIGHT-200))


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
        displayStartScreen(screen)
    elif(gameState=="score"):
        p1Score = p1.getScore()
        p2Score = p2.getScore()
        displayScoreScreen(screen, p1Score, p2Score)
    elif(gameState =="win"):
        displayWinnerScreen(screen, p1, p2)
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
        p1.setScore(0)
        p2.setScore(0)
        ball.reset()

    #check for a key press and move players as necessary
    if(gameState == "play"):
        p1.updatePlayerGivenKeypress(True)
        p2.updatePlayerGivenKeypress(False)
        move(ball,p1)
        move(ball,p2)
        scored = checkForGoal(ball,p1,p2)
        if(scored==True):
            gameState = "score"

    #update scoreboard for user and wait for next point to start
    if(gameState == "score"):
        # check to see if someone has won
        if(p1.getScore()==constants.POINTS_TO_WIN  or\
            p2.getScore()==constants.POINTS_TO_WIN):
            gameState = "win"

        # go to next point if space is pressed
        keys = pygame.key.get_pressed()
        if(gameState=="score" and keys[pygame.K_SPACE]):
            gameState = "play"
            # reset ball position and sets new random speed and direction
            ball.reset()

    # someone has won the game
    if(gameState == "win"):
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_RETURN]):
            gameState = "start"
    # Update the screen display
    updateScreen(screen, ball, p1, p2)

# Quits game after completion
pygame.quit()
