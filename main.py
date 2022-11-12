import pygame, sys
import pygame.locals as locals
from main_menu import MainMenu

SIZE = (640, 400)
BG_COLOUR = (0, 0, 0)
LINE_COLOUR = (255, 255, 255)

game_modules = [MainMenu(SIZE)]
current_module = 0

def run_game():
    global current_module
    pygame.init()

    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption('Aptitude Test')
    clock = pygame.time.Clock()

    while True:
        time_passed = clock.tick(30)
        for event in pygame.event.get():
            if event.type == locals.QUIT:
                exit_game()
            else:
                game_modules[current_module].event(event)
        
        reponse = game_modules[current_module].update(screen)
        if reponse:
            current_module += 1
            if current_module >= len(game_modules):
                print('Game Complete!')
                return
        pygame.display.flip()
        clock.tick(60)


def exit_game():
    sys.exit()


if __name__ == "__main__":
    run_game()
