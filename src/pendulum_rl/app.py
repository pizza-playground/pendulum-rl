from math import cos, sin
import pygame

# pygame 창 크기 설정
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 450
FPS = 60

# 레일 위치 지정
RAIL = 380

# 카트 정보
CART_WIDTH = 40
CART_HEIGHT = 28
CART_START_X = (WINDOW_WIDTH - CART_WIDTH) / 2
CART_Y = RAIL - CART_HEIGHT // 2

# 막대(진자 막대) 정보
BAR_LENGTH = 100
BAR_WIDTH = 8
BAR_INSET = 4

# 막대축 정보
PIVOT_OFFSET_Y = 5
PIVOT_RADIUS = 4

# 시스템 컬러 설정
BACKGROUND_COLOR = (255, 255, 255)
GROUND_COLOR = (70, 70, 70)
CART_COLOR = (0, 0, 0)
BAR_COLOR = (202, 164, 114)
PIVOT_COLOR = (135, 135, 255)


def draw_cart_pole(
    screen: pygame.Surface,
    cart_x: float,
    bar_angle: float,
) -> None:

    # 카트
    cart = pygame.Rect(
        round(cart_x),
        CART_Y,
        CART_WIDTH,
        CART_HEIGHT,
    )

    # 축
    pivot_center = pygame.Vector2(
        cart.centerx,
        cart.top + PIVOT_OFFSET_Y,
    )

    # 막대의 방향
    bar_direction = pygame.Vector2(
        sin(bar_angle),
        -cos(bar_angle),
    )

    # 막대의 두께
    bar_side = pygame.Vector2(
        cos(bar_angle),
        sin(bar_angle),
    ) * (BAR_WIDTH / 2)

    # 막대의 끝지점 좌표
    bar_top = pivot_center + bar_direction * BAR_LENGTH

    # 막대의 밑동 좌표 
    bar_root = pivot_center - bar_direction * BAR_INSET

    # 막대 생성
    bar_corners = (
        bar_top - bar_side,
        bar_top + bar_side,
        bar_root + bar_side,
        bar_root - bar_side,
    )

    # 레일
    pygame.draw.line(
        screen,
        GROUND_COLOR,
        (0, RAIL),
        (WINDOW_WIDTH, RAIL),
        2,
    )

    # 카트 그리기
    pygame.draw.rect(screen, CART_COLOR, cart)

    # 막대 그리기
    pygame.draw.polygon(screen, BAR_COLOR, bar_corners)

    # 회전축 그리기
    pygame.draw.circle(
        screen,
        PIVOT_COLOR,
        pivot_center,
        PIVOT_RADIUS,
    )


def main() -> None:
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Inverted Pendulum")

    clock = pygame.time.Clock()

    # 카트는 화면 중앙에 고정
    cart_x = CART_START_X

    # 막대는 항상 수직(일직선)으로 고정
    bar_angle = 0.0

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill(BACKGROUND_COLOR)

        # 카트, 회전축, 막대를 그리기
        draw_cart_pole(screen, cart_x, bar_angle)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()