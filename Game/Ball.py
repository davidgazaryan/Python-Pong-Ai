import pygame


class Ball:
    max_speed = 10

    def __init__(self, x: int, y: int, radius: int, speed: int, surface):
        self.color = (220, 20, 60)
        self.radius = radius
        self.x = x
        self.y = self.y_start = y
        self.x_speed = speed
        self.y_speed = 0
        self.screen = surface

    def draw_ball(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def movement(self):
        self.x += self.x_speed
        self.y += self.y_speed

    def update(self):
        self.draw_ball()
        self.movement()

