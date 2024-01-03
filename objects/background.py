import pygame.sprite

import assets
import configs
from layer import Layer


class Background(pygame.sprite.Sprite):
    def __init__(self, index,  *groups):
        self._layer = Layer.BACKGROUND
        self.image = assets.get_sprite("background")

        # set_mode()를 통해 생성된 스크린에 get_rect를 통해 이미지를 위치시킴
        # set_mode = 스크린의 크기 설정, get_rect = 스크린 크기에 따른 객체의 위치 설정
        # 이동하려는 이미지의 위치를 좌측 상단에 (configs.SCREEN_WIDTH*index,0)에 설정
        self.rect = self.image.get_rect(
            topleft=(configs.SCREEN_WIDTH * index, 0))

        # 부모 클래스인 pygame.sprite.Sprite의 초기화를 수행
        super().__init__(*groups)

    # 배경이 움직이는 역할을 하는 함수
    def update(self):
        self.rect.x -= 1            # 배경의 x좌표 감소

        # 만일 배경이 화면을 벗어나면 다시 오른쪽 끝에 배치한다 == 화면이 왼쪽으로 스크롤되는 효과
        if self.rect.right <= 0:
            self.rect.x = configs.SCREEN_WIDTH
