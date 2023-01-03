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

# 이벤트 루프 => 프로그램이 종료되지 않도록 대기하는것으로 마우스나 키보드 입력을 체크하는것
# 이벤트 루프가 있어야 화면이 종료되지 않으므로 설정
running = True  # 게임이 진행중인가?
while running:
    for event in pygame.event.get():  # 어떤 이벤트가 발생했는지
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하면
            running = False  # 게임이 진행중이 아님

    # 배경그리기, blit()로 background 이미지를 시작좌표에 맞게 그린다
    screen.blit(background, (0, 0))
    # screen.fill((0, 0, 255)) => fill()을 통해서 이미지가 아닌 색상으로 배경을 채울수 있음

    # pygame에서 매 프레임마다 화면을 새로 그리는 동작을 해줘야함
    pygame.display.update()  # 게임화면을 다시 그리기!


# pygame 종료
pygame.quit()
