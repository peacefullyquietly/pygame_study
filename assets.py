import os
import pygame
sprites = {}


# 지정된 디렉토리 내의 이미지 파일을 불러와 sprites라는 딕셔너리에 저장
def load_sprites():
    path = os.path.join("assets", "sprites")

    # listdir의 인자로 경로를 전달할 경우 해당 경로에 존재하는 파일과 디렉터리 목록을 구할 수 있음
    for file in os.listdir(path):

        # sprites는 이미지의 이름을 키(key)로 가지고 해당 이미지를 값(value)으로 가지는 딕셔너리
        sprites[file.split('.')[0]] = pygame.image.load(
            os.path.join(path, file))

    # print("확인용: ", len(sprites))


def get_sprite(name):
    return sprites[name]
