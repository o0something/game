
from numpy import number
import pygame
import sys

class kopalnia():
    
    def __init__(self) -> None:
        super().__init__()
        self.width, self.height = (600,500)
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GRAY = (30, 30, 30)
        self.image=pygame.image.load('D:/pycha/Home/gra/kopalni1.png')

    def loop(self,gracz):
        pygame.init()
        pygame.font.init()
        clock = pygame.time.Clock()
        number = 0
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.font.init()
        self.font = pygame.font.Font("freesansbold.ttf", 50)
        pygame.display.set_caption("Kopalnia")
        # The button is just a rect.
        button = pygame.Rect(250, 200, 100, 100)
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                # This block is executed once for each MOUSEBUTTONDOWN event.
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # 1 is the left mouse button, 2 is middle, 3 is right.
                    if event.button == 1:
                        # `event.pos` is the mouse position.
                        if button.collidepoint(event.pos):
                            # Increment the number.
                            number += 1

            self.screen.blit(self.image, (0, 0))
            pygame.draw.rect(self.screen, self.GRAY, button)
            text_surf = self.font.render(str(number), True, 'yellow')
            # You can pass the center directly to the `get_rect` method.
            text_rect = text_surf.get_rect(center=(self.width/2, 30))
            self.screen.blit(text_surf, text_rect)
            pygame.display.update()

            clock.tick(30)
        gracz.coins+=number*0.1
        print(f"monety : {gracz.coins}")
        pygame.display.quit()
        pygame.quit()



