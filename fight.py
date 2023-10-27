import pygame

GRAVITY = 1

class Fighter():
    def __init__(self,x,y,height, width, velocity) -> None:
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.velocity = velocity
    def draw(self, screen, grav):
        pygame.draw.rect(screen, "red", pygame.Rect(self.x, self.y, self.height, self.width))
        #self.y += grav
    def move(self, screen, key):
        if key == 'up':
            self.y -= 10
        if key == 'left':
            self.x -= self.velocity
        if key == 'right':
            self.x += self.velocity

def update(screen, wid, heg, keys, playerOne, playerTwo):
    if keys[pygame.K_w]:
        playerOne.move(screen, 'up')
    if keys[pygame.K_a]:
        playerOne.move(screen, 'left')
    if keys[pygame.K_d]:
        playerOne.move(screen, 'right')
    if keys[pygame.K_UP]:
        playerTwo.move(screen, 'up')
    if keys[pygame.K_LEFT]:
        playerTwo.move(screen, 'left')
    if keys[pygame.K_RIGHT]:
        playerTwo.move(screen, 'right')
        
        



def run():
    pygame.init()
    pygame.font.init()
    
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    text_surface = my_font.render('Game Over', False, (255, 255, 255))
    wid = 1280
    heg = 720
    
    playerOne = Fighter(30, heg-350, 30, (100), 5)
    playerTwo = Fighter(wid-60, heg-350, 30, 100, 5)
    
    
    screen = pygame.display.set_mode((wid, heg))
    clock = pygame.time.Clock()
    running = True
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("white")
        
        keys = pygame.key.get_pressed()
        update(screen, wid, heg, keys, playerOne, playerTwo)
        playerOne.draw(screen, GRAVITY)
        playerTwo.draw(screen, GRAVITY)
        
        pygame.draw.rect(screen, "black", pygame.Rect(0, heg-250, wid, heg))
        
        # flip() the display to put your work on screen
        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60

    pygame.quit()

if __name__ == "__main__":
    run()