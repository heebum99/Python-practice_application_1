import pygame

pygame.init()  # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game")  # 게임 이름

# 이벤트 루프 => 프로그램이 종료되지 않도록 대기하는것으로 마우스나 키보드 입력을 체크하는것
# 이벤트 루프가 있어야 화면이 종료되지 않으므로 설정
running = True  # 게임이 진행중인가?
while running:
    for event in pygame.event.get():  # 어떤 이벤트가 발생했는지
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하면
            running = False  # 게임이 진행중이 아님

# pygame 종료
pygame.quit()
