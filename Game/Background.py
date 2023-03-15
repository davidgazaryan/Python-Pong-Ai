import pygame


class Background:
    def __init__(self, width, score, surface):
        self.color = 'white'
        self.width = width
        self.right_score = score
        self.left_score = score
        self.screen = surface
        self.left_hits = 0
        self.right_hits = 0

    def draw_background(self):
        pygame.draw.rect(self.screen, self.color, [965, 100, 50, 400], self.width)  # 220 + 160 = 370. (370 + 230) / 2 = 300 or halfway
        pygame.draw.rect(self.screen, self.color, [-15, 100, 50, 400], self.width)  # 50 - 15 = 35. 1000 - 965 = 35.
        for i in range(615, -20, -50):
            pygame.draw.line(self.screen, self.color, (500, i), (500, i + 20), self.width)

    def score(self):
        right_score = pygame.font.Font(None, 40)
        left_score = pygame.font.Font(None, 40)
        right_score = right_score.render(str(self.right_score), False, 'White')
        left_score = left_score.render(str(self.left_score), False, 'White')
        total_hits = pygame.font.Font(None, 40)
        total_hits = total_hits.render(str(self.left_hits + self.right_hits), False, 'Red')
        self.screen.blits([(right_score, (975, 15)), (left_score, (10, 15)), (total_hits, (500, 15))])

    def update(self):
        self.draw_background()
        self.score()

