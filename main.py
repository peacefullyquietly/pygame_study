import pygame
import configs
import assets
from objects.background import Background
from objects.bird import Bird
from objects.column import Column
from objects.floor import Floor
from objects.gameover_message import GameOverMessage
from objects.gamestart_message import GameStartMessage
from objects.score import Score


pygame.init()

screen = pygame.display.set_mode(
    (configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))         # set_mode = 화면 해상도 초기화

clock = pygame.time.Clock()         # 게임 루프 내 FPS(초당 프레임 수)를 조절 하는 데 사용
column_create_event = pygame.USEREVENT
running = True
gameover = False
gamestarted = False

assets.load_sprites()
assets.load_audios()

# LayerUpdates() ==> sprite의 순서를 변경할 때 사용, sprite를 레이어 별로 관리하는 데 사용됨
sprites = pygame.sprite.LayeredUpdates()


def create_sprites():
    Background(0, sprites)
    Background(1, sprites)
    Floor(0, sprites)
    Floor(1, sprites)

    return Bird(sprites), GameStartMessage(sprites), Score(sprites)


bird, game_start_message, score = create_sprites()


while running:
    for event in pygame.event.get():            # pygame.event.get() --> 마우스, 키보드 입력값을 받는다
        if event.type == pygame.QUIT:           # pygame.QUIT == 윈도우를 닫을 때 발생하는 이벤트
            running = False                     # 창이 닫히면 게임 종료
        if event.type == column_create_event:
            Column(sprites)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not gamestarted and not gameover:
                gamestarted = True
                game_start_message.kill()
                pygame.time.set_timer(column_create_event, 1500)

            if event.key == pygame.K_ESCAPE and gameover:
                gameover = False
                gamestarted = False
                sprites.empty()
                bird, game_start_message, score = create_sprites()

        # comment error
        if not gameover:
            bird.handle_event(event)

    screen.fill(0)

    sprites.draw(screen)

    if gamestarted and not gameover:
        # 일부 화면만 업데이트 할 경우..?
        sprites.update()

    if bird.check_collision(sprites) and not gameover:
        gameover = True
        gamestarted = False
        GameOverMessage(sprites)
        pygame.time.set_timer(column_create_event, 0)
        assets.play_audio("hit")

    for sprite in sprites:
        if type(sprite) is Column and sprite.is_passed():
            score.value += 1
            assets.play_audio("point ")

    # 전체 화면을 업데이트
    pygame.display.flip()

    # 초당 configs.FPS 프레임으로 설정
    clock.tick(configs.FPS)

pygame.quit()
