from math import cos, sin
import pygame

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 450
FPS = 60
RAIL = 380

CART_WIDTH, CART_HEIGHT = 40, 30
CART_START_X = (WINDOW_WIDTH - CART_WIDTH) / 2
CART_Y = RAIL - CART_HEIGHT // 2

BAR_LENGTH, BAR_WIDTH, BAR_INSET = 100, 8, 5
PIVOT_OFFSET_Y, PIVOT_RADIUS = 6, 5

BACKGROUND_COLOR = (255, 255, 255)
GROUND_COLOR = (70, 70, 70)
CART_COLOR = (0, 0, 0)
BAR_COLOR = (202, 164, 114)
PIVOT_COLOR = (135, 135, 255)


def draw_cart_pole(screen: pygame.Surface, cart_x: float, bar_angle: float) -> None:
    cart = pygame.Rect(round(cart_x), CART_Y, CART_WIDTH, CART_HEIGHT)
    pivot_center = pygame.Vector2(cart.centerx, cart.top + PIVOT_OFFSET_Y)

    bar_direction = pygame.Vector2(sin(bar_angle), -cos(bar_angle))
    bar_side = pygame.Vector2(cos(bar_angle), sin(bar_angle)) * (BAR_WIDTH / 2)

    bar_top = pivot_center + bar_direction * BAR_LENGTH
    bar_root = pivot_center - bar_direction * BAR_INSET

    bar_corners = (
        bar_top - bar_side,
        bar_top + bar_side,
        bar_root + bar_side,
        bar_root - bar_side,
    )

    pygame.draw.line(screen, GROUND_COLOR, (0, RAIL), (WINDOW_WIDTH, RAIL), 3)
    pygame.draw.rect(screen, CART_COLOR, cart)
    pygame.draw.polygon(screen, BAR_COLOR, bar_corners)
    pygame.draw.circle(screen, PIVOT_COLOR, pivot_center, PIVOT_RADIUS)


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Inverted Pendulum")
    clock = pygame.time.Clock()

    cart_x = CART_START_X
    bar_angle = 0.0

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        screen.fill(BACKGROUND_COLOR)
        draw_cart_pole(screen, cart_x, bar_angle)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()