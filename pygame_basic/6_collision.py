import pygame

pygame.init()  # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game")  # 게임 이름

# FPS
clock = pygame.time.Clock()

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

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6

# 적 캐릭터
enemy = pygame.image.load(
    "C:\\파이썬\\ap_WorkSpace_1\\Python-practice_application\\pygame_basic\\enemy.png")
enemy_size = enemy.get_rect().size  # 이미지의 크기를 구함
enemy_width = enemy_size[0]  # 캐릭터의 가로크기
enemy_height = enemy_size[1]  # 캐릭터의 세로크기
# 화면 가로의 절반 크기에 해당하는 곳에 위치
enemy_x_pos = (screen_width / 2) - (enemy_width/2)
# 화면 세로의 절반 크기에 해당하는 곳에 위치
enemy_y_pos = (screen_height / 2) - (enemy_height / 2)

# 이벤트 루프 => 프로그램이 종료되지 않도록 대기하는것으로 마우스나 키보드 입력을 체크하는것
# 이벤트 루프가 있어야 화면이 종료되지 않으므로 설정
running = True  # 게임이 진행중인가?
while running:
    # 캐릭터가 1초동안에 100만큼 이동해야한다면
    # 10 fps: 1초동안에 10번 동작 => 1초에 10만큼 이동해야함
    # 20 fps: 1초동안에 20번 동작 => 1초에 5만큼 이동해야함
    dt = clock.tick(60)  # 게임화면의 초당 프레임 수를 설정
    # 프레임 수에 따라 부드러움이 달라질 수는 있지만 이동거리가 달라지면 안됨

    # print("fps : "+str(clock.get_fps()))

    for event in pygame.event.get():  # 어떤 이벤트가 발생했는지
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하면
            running = False  # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:  # 키보드를 눌렀을 경우
            if event.key == pygame.K_LEFT:  # 캐릭터를 왼쪽으로
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:  # 캐릭터를 오른쪽으로
                to_x += character_speed
            elif event.key == pygame.K_UP:  # 캐릭터를 위로
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:  # 캐릭터를 아래로
                to_y += character_speed

        if event.type == pygame.KEYUP:  # 방향키를 땠을 경우
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:  # x방향으로의 이동을 멈춤
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:  # y방향으로의 이동을 멈춤
                to_y = 0

    # 이동한 만큼 캐릭터의 좌표를 수정
    # 프레임이 달라도 이동거리를 같게 보정해주기 위해 dt값을 곱해줌
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 캐릭터의 가로 경계값 처리(화면 밖으로 벗어나지 못하게)
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 캐릭터의 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    # 움직이는 캐릭터의 좌표 정보를 저장
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    # 적 캐릭터의 좌표 정보를 저장
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):  # 캐릭터 rect 기준으로 충돌여부를 확인
        print("충돌했어요")
        running = False

    # 배경그리기, blit()로 background 이미지를 시작좌표에 맞게 그린다.
    screen.blit(background, (0, 0))

    # 캐릭터 그리기, blit()로 character 이미지를 시작좌표에 맞게 그린다.
    screen.blit(character, (character_x_pos, character_y_pos))

    # 적 캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    # pygame에서 매 프레임마다 화면을 새로 그리는 동작을 해줘야함
    pygame.display.update()  # 게임화면을 다시 그리기!


# pygame 종료
pygame.quit()
