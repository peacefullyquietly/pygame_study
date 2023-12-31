import pygame
import assets
import configs

from objects.background import Background
from objects.bird import Bird
from objects.column import Column
from objects.floor import Floor
from objects.gamestart_message import GameStartMessage

pygame.init()

screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))
clock = pygame.time.Clock()
column_create_event = pygame.USEREVENT
running = True
gameover = False
gamestarted = False
score = 0

assets.load_sprites()
sprites = pygame.sprite.LayeredUpdates()


Background(0, sprites)
Background(1, sprites)
Floor(0, sprites)
Floor(1, sprites)

bird = Bird(sprites)

game_start_message = GameStartMessage(sprites)

pygame.time.set_timer(column_create_event, 1500)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == column_create_event:
            Column(sprites)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                gamestarted = True
                game_start_message.kill()

        bird.handle_event(event)

    screen.fill(0)

    sprites.draw(screen)

    if gamestarted and not gameover:
        sprites.update()

    if bird.check_collision(sprites):
        gameover = True
        gamestarted = False

    for sprite in sprites:
        if type(sprite) is Column and sprite.is_passed():
            score += 1

    pygame.display.flip()
    clock.tick(configs.FPS)

pygame.quit()
