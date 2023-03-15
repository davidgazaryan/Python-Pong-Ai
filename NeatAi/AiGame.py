from Game.main import *
import neat
import os
import pickle


class PongGame:
    def __init__(self):
        self.left_paddle = left_paddle
        self.right_paddle = right_paddle
        self.ball = ball
        self.background = background

    def test_ai(self, genome, config):
        net = neat.nn.FeedForwardNetwork.create(genome, config)

        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w] and (self.left_paddle.x < 500 and self.left_paddle.y >= 0):
                self.left_paddle.y -= 4
            elif keys[pygame.K_s] and (left_paddle.x < 500 and left_paddle.y + left_paddle.height <= 600):
                self.left_paddle.y += 4

            output = net.activate(
                (self.right_paddle.y, ball.y, abs(self.right_paddle.x - self.ball.x)))
            decision = output.index(max(output))

            if decision == 1:
                self.right_paddle.y -= 4
            else:
                self.right_paddle.y += 4

            game = main()
            self.background.update()
            self.left_paddle.draw_paddle()
            self.right_paddle.draw_paddle()
            pygame.display.update()

        pygame.quit()

    def training_ai(self, genome1, genome2, config):
        net1 = neat.nn.FeedForwardNetwork.create(genome1, config)
        net2 = neat.nn.FeedForwardNetwork.create(genome2, config)

        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            output1 = net1.activate(
                (self.left_paddle.y, self.ball.y, abs(self.left_paddle.x - self.ball.x)))
            decision1 = output1.index(max(output1))

            if decision1 == 1:
                self.left_paddle.y -= 4
            else:
                self.left_paddle.y += 4

            output2 = net2.activate(
                (self.right_paddle.y, self.ball.y, abs(self.right_paddle.x - self.ball.x)))
            decision2 = output2.index(max(output2))

            if decision2 == 1:
                self.right_paddle.y -= 4
            else:
                self.right_paddle.y += 4

            game = main()
            self.background.update()
            self.left_paddle.draw_paddle()
            self.right_paddle.draw_paddle()
            pygame.display.update()

            if self.background.left_score >= 1 or self.background.right_score >= 1 or self.background.left_hits > 50:
                self.calculate_fitness(genome1, genome2)
                break

    def calculate_fitness(self, genome1, genome2):
        genome1.fitness += self.background.left_hits
        genome2.fitness += self.background.right_hits


def eval_genomes(genomes, config):
    width, height = 1000, 600
    window = pygame.display.set_mode((width, height))

    for i, (genome_id1, genome1) in enumerate(genomes):
        if i == len(genomes) - 1:
            break
        genome1.fitness = 0
        for genome_id2, genome2 in genomes[i+1:]:
            genome2.fitness = 0 if genome2.fitness == None else genome2.fitness
            game = PongGame()
            game.training_ai(genome1, genome2, config)


def run_neat(config):
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(1))

    winner = p.run(eval_genomes, 50)
    with open("best.pickle", "wb") as f:
        pickle.dump(winner, f)


def test_ai(config):
    width, height = 1000, 600
    window = pygame.display.set_mode((width, height))

    with open("best.pickle", "rb") as f:
        winner = pickle.load(f)

    game = PongGame(window, width, height)
    game.test_ai(winner, config)


if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "Configuration.txt")

    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)
    run_neat(config)
    #test_ai(config)
