import pygame


class Paddle:
    def __init__(self, x: int , y: int, width, height, surface):
        self.color = (0, 250, 154)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.start_position = y  # Used for putting paddles at original position once scored on
        self.screen = surface

    def draw_paddle(self):
        pygame.draw.rect(self.screen, self.color, [self.x, self.y, self.width, self.height])

    def movement(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and (self.x < 500 and self.y >= 0): self.y -= 4
        elif keys[pygame.K_s] and (self.x < 500 and self.y + self.height <= 600): self. y += 4

        if keys[pygame.K_UP] and (self.x > 500 and self.y >= 0): self.y -= 4
        elif keys[pygame.K_DOWN] and (self.x > 500 and self.y + self.height <= 600): self.y += 4

    def update(self):
        self.draw_paddle()
        self.movement()
