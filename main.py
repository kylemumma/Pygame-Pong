import pygame, paddle, ball, random

#make paddles
player1 = paddle.Paddle()
player2 = paddle.Paddle()
ball = ball.Ball()

def keepPaddlesInBound():
    #keep player1 paddle within bounds
    if(player1.getY() <= 0):
        player1.setUpVel(0)
        player1.setY(0)
    elif(player1.getY() >= 400):
        player1.setDownVel(0)
        player1.setY(400)

    #keep player2 paddle within bounds
    if(player2.getY() <= 0):
        player2.setUpVel(0)
        player2.setY(0)
    elif(player2.getY() >= 400):
        player2.setDownVel(0)
        player2.setY(400)

def keepBallInBounds():
    #keep ball within bounds
    if(ball.getY() <= 0 or ball.getY() >= 490):
        ball.setYVel(ball.getYVel() * -1)

    if(ball.getX() <= 0 or ball.getX() >= 590):
        if(ball.getX() <= 0):
            player2.addPoint()
        else:
            player1.addPoint()

        ball.setX(295)
        ball.setY(245)
        ball.setRandomVel()

        print(f"Player 1: {player1.getPoints()}")
        print(f"Player 2: {player2.getPoints()}")
        print()

def ballPaddleCollision():
    #ball collisions with player1 or 2
    if(ball.getX() <= player1.getX() + player1.getWidth() and ball.getY() >= player1.getY() - ball.getRadius() and
    ball.getY() <= player1.getY() + player1.getHeight()):
        ball.setXVel(ball.getXVel() * -1)
    elif(ball.getX() >= 600 - player2.getX() - player2.getWidth() - ball.getRadius() and ball.getY() >= player2.getY() - ball.getRadius() and ball.getY() <= player2.getY() + player2.getHeight()):
        ball.setXVel(ball.getXVel() * -1)

def simulatePhysics():
    #update object positions
    player1.update()
    player2.update()
    ball.update()

def processCollisions():

    keepPaddlesInBound()

    keepBallInBounds()

    ballPaddleCollision()

def repaint(screen, background, player1_surface, player2_surface, ball_surface, font):

    #make points text
    player1points_surface = font.render(str(player1.getPoints()), False, (255, 255, 255))
    player2points_surface = font.render(str(player2.getPoints()), False, (255, 255, 255))

    #draw objects
    background.fill((0,0,0)) #bg
    pygame.draw.rect(player1_surface, (255, 255, 255), (0, 0, player1.getWidth(), 100)) #player1
    pygame.draw.rect(player2_surface, (255, 255, 255), (0, 0, player2.getWidth(), 100))
    pygame.draw.rect(ball_surface, (255, 255, 255), (0, 0, ball.getRadius(), ball.getRadius()))

    #converts to make blitting faster
    background = background.convert()
    player1_surface = player1_surface.convert()
    player2_surface = player2_surface.convert()
    ball_surface = ball_surface.convert()
    player1points_surface = player1points_surface.convert()

    #puts the background layer on the screen
    screen_width, screen_height = screen.get_size()
    background.blit(player1_surface, (player1.getX(), player1.getY()))
    background.blit(player2_surface, (screen_width - player2.getWidth() - player2.getX(), player2.getY()))
    background.blit(ball_surface, (ball.getX(), ball.getY()))
    background.blit(player1points_surface, (250, 20))
    background.blit(player2points_surface, (350, 20))
    screen.blit(background, (0, 0))

    #update screen
    pygame.display.update()

def gameLoop(screen, background, player1_surface, player2_surface, ball_surface, font):
    running = True
    while running:
        #KEY LISTENERS
        for event in pygame.event.get():
            #if they press exit quit the game
            if(event.type == pygame.QUIT):
                running = False

            #--- PLAYER 1 MOVEMENT ---
            #if w key pressed
            if(event.type == pygame.KEYDOWN and event.key == pygame.K_w):
                player1.setUpVel(10)

            #if s key pressed
            if(event.type == pygame.KEYDOWN and event.key == pygame.K_s):
                player1.setDownVel(10)

            #if w key released
            if(event.type == pygame.KEYUP and event.key == pygame.K_w):
                player1.setUpVel(0)

            #if s key released
            if(event.type == pygame.KEYUP and event.key == pygame.K_s):
                player1.setDownVel(0)

            #--- PLAYER 2 MOVEMENT ---
            #if up key pressed
            if(event.type == pygame.KEYDOWN and event.key == pygame.K_UP):
                player2.setUpVel(10)

            #if down key pressed
            if(event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN):
                player2.setDownVel(10)

            #if up key released
            if(event.type == pygame.KEYUP and event.key == pygame.K_UP):
                player2.setUpVel(0)

            #if down key released
            if(event.type == pygame.KEYUP and event.key == pygame.K_DOWN):
                player2.setDownVel(0)

        simulatePhysics()

        processCollisions()

        repaint(screen, background, player1_surface, player2_surface, ball_surface, font)

def main():
    #init pygame
    pygame.init()
    pygame.font.init()

    #set font
    font = pygame.font.SysFont("Comic Sans MS", 50)

    #set screen title
    pygame.display.set_caption("Pong")

    #set display size
    screen = pygame.display.set_mode((600,500)) # Set screen size of pygame window
    background = pygame.Surface(screen.get_size())  # Create empty pygame surface

    player1_surface = pygame.Surface((25, 100))
    player2_surface = pygame.Surface((25, 100))
    ball_surface = pygame.Surface((10, 10))

    gameLoop(screen, background, player1_surface, player2_surface, ball_surface, font)

if __name__ == "__main__":
    main()
