import pygame
pygame.init()

class Game:
    def __init__(self):
        self.state = [[None, None, None],
                      [None, None, None],
                      [None, None, None]]
        self.winner = False

    def check(self):
        for i in range(3):
            if self.state[i][0] == self.state[i][1] and self.state[i][0] == self.state[i][2]:
                self.winner = True
                break
            if self.state[0][i] == self.state[1][i] and self.state[0][i] == self.state[2][i]:
                self.winner = True
                break


            else:
                self.winner = False


def redraw_window(surface, w, h, game):
    surface.fill((0, 0, 0))
    gaps = w // 5
    x = gaps
    y = gaps
    for i in range(2):
        x += gaps
        y += gaps
        pygame.draw.line(surface, (255, 255, 255), (x, gaps), (x, h - gaps))
        pygame.draw.line(surface, (255, 255, 255), (gaps, y), (w - gaps, y))


    pygame.display.update()


def main():
    display_height = 500
    display_width = 500
    screen = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption("Noughts and Crosses")
    clock = pygame.time.Clock()
    game = Game()

    while not game.winner:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break

        clock.tick(60)
        redraw_window(screen, display_width, display_height, game)

main()

