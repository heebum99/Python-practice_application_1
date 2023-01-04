import pygame

pygame.init()  # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game")  # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load(
    "C:\\파이썬\\ap_WorkSpace_1\\Python-practice_application\\pygame_basic\\background.png")

# 캐릭터(스프라이트) 이미지 불러오기
character = pygame.image.load(
    "C:\\파이썬\\ap_WorkSpace_1\\Python-practice_application\\pygame_basic\\character.png")
character_size = character.get_rect().size  # 이미지의 크기를 구함
character_width = character_size[0]  # 캐릭터의 가로크기
character_height = character_size[1]  # 캐릭터의 세로크기
# 화면 가로의 절반 크기에 해당하는 곳에 위치
character_x_pos = (screen_width / 2) - (character_width/2)
character_y_pos = screen_height - character_height  # 화면 세로 크기 가장 아래에 해당하는 곳에 위치

# 이벤트 루프 => 프로그램이 종료되지 않도록 대기하는것으로 마우스나 키보드 입력을 체크하는것
# 이벤트 루프가 있어야 화면이 종료되지 않으므로 설정
running = True  # 게임이 진행중인가?
while running:
    for event in pygame.event.get():  # 어떤 이벤트가 발생했는지
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하면
            running = False  # 게임이 진행중이 아님

    # 배경그리기, blit()로 background 이미지를 시작좌표에 맞게 그린다.
    screen.blit(background, (0, 0))

    # 캐릭터 그리기, blit()로 character 이미지를 시작좌표에 맞게 그린다.
    screen.blit(character, (character_x_pos, character_y_pos))

    # pygame에서 매 프레임마다 화면을 새로 그리는 동작을 해줘야함
    pygame.display.update()  # 게임화면을 다시 그리기!


# pygame 종료
pygame.quit()
