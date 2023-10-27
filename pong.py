import pygame
import random

class Player:
    def __init__(self, x, y, width, height, velocity) -> None:
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.velocity = velocity

class Ball:
    def __init__(self, x, y, velocityX, velocityY, oVelocity):
        self.x = x
        self.y = y
        self.velocityX = velocityX
        self.velocityY = velocityY
        self.oVelocity = oVelocity



def update(playerOne, playerTwo, theBall, theKey, heg):
    if theKey[pygame.K_w]:
        if playerOne.y > 0:
            playerOne.y -= playerOne.velocity
    if theKey[pygame.K_s]:
        if playerOne.y < heg - playerOne.height:
            playerOne.y += playerOne.velocity
    if theKey[pygame.K_UP]:
        if playerTwo.y > 0:
            playerTwo.y -= playerTwo.velocity
    if theKey[pygame.K_DOWN]:
        if playerTwo.y < heg - playerTwo.height:
            playerTwo.y += playerTwo.velocity
    theBall.x += theBall.oVelocity
    theBall.y += theBall.velocityY
    
def checkCol(theBall, playerOne, playerTwo, wid, heg):
    print(f"top: {playerTwo.y}, bot: {playerTwo.y+playerTwo.height}, mid: {playerOne.x}, ballX: {theBall.x}")
    #print(f"{theBall.y}")
    if theBall.y > heg or theBall.y < 0:
        theBall.velocityY = -1*theBall.velocityY
    check1 = theBall.y >= playerOne.y and theBall.y <= playerOne.y+playerOne.height and (theBall.x >= playerOne.x+20 and theBall.x <= playerOne.x+30)
    check2 = theBall.y >= playerTwo.y and theBall.y <= playerTwo.y+playerTwo.height and (theBall.x+20 >= playerTwo.x-10 and theBall.x+20 <= playerTwo.x+10)
    if check1 or check2:
        theBall.oVelocity =  (-1*theBall.oVelocity)
        theBall.velocityY = random.uniform(-5,5)
        theBall.velocityY = -1*theBall.velocityY
        
def game_check(theBall, wid):
    if theBall.x < wid and theBall.x > 0:
        return True
    else:
        return False
        
def run():
    pygame.init()
    pygame.font.init()
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    text_surface = my_font.render('Game Over', False, (255, 255, 255))
    wid = 1280
    heg = 720
    screen = pygame.display.set_mode((wid, heg))
    clock = pygame.time.Clock()
    running = True
    playerOne = Player(30,30, 30, 140, 10)
    playerTwo = Player((wid-60), 30, 30, 140, 10)
    gameBall = Ball(wid//2, heg//2, 5, 0, 15)
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")
        # RENDER YOUR GAME HERE
        if game_check(gameBall, wid):
            keys = pygame.key.get_pressed()
            update(playerOne, playerTwo, gameBall, keys, heg)
            checkCol(gameBall, playerOne, playerTwo, wid, heg)
            game_check(gameBall, wid)
            pygame.draw.rect(screen, "white", pygame.Rect(playerOne.x, playerOne.y, playerOne.width, playerOne.height))
            pygame.draw.rect(screen, "white", pygame.Rect(playerTwo.x, playerTwo.y, playerTwo.width, playerTwo.height))
            pygame.draw.circle(screen, "white", (gameBall.x, gameBall.y), 15)
        else:
            screen.blit(text_surface, (wid//2-50, heg//2))
        
        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()

if __name__ == "__main__":
    run()