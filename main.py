import pygame
import configs
import assets
from objects.background import Background
from objects.column import Column
from objects.floor import Floor


pygame.init()

screen = pygame.display.set_mode(
    (configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))         # set_mode = 화면 해상도 초기화

clock = pygame.time.Clock()         # 게임 루프 내 FPS(초당 프레임 수)를 조절 하는 데 사용
column_create_event = pygame.USEREVENT
running = True

assets.load_sprites()

# LayerUpdates() ==> sprite의 순서를 변경할 때 사용, sprite를 레이어 별로 관리하는 데 사용됨
sprites = pygame.sprite.LayeredUpdates()


Background(0, sprites)
Background(1, sprites)
Floor(0, sprites)
Floor(1, sprites)

# Column(sprites)

pygame.time.set_timer(column_create_event, 1500)

while running:
    for event in pygame.event.get():            # pygame.event.get() --> 마우스, 키보드 입력값을 받는다
        if event.type == pygame.QUIT:           # pygame.QUIT == 윈도우를 닫을 때 발생하는 이벤트
            running = False                     # 창이 닫히면 게임 종료
        if event.type == column_create_event:
            Column(sprites)

    screen.fill("pink")

    sprites.draw(screen)

    # 일부 화면만 업데이트 할 경우..?
    sprites.update()

    # 전체 화면을 업데이트
    pygame.display.flip()

    # 초당 configs.FPS 프레임으로 설정
    clock.tick(configs.FPS)

pygame.quit()
