import pygame

import physics
import rendering
import random

FPS = 60
PIXELS_PER_METER = 100 

PHYSICS_DT = 1 / 60  
MAX_FRAME_TIME = 0.25


def to_screen_x(cart_position_m: float) -> float:
    center_x = rendering.WINDOW_WIDTH / 2 + cart_position_m * PIXELS_PER_METER
    return center_x - rendering.CART_WIDTH / 2


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((rendering.WINDOW_WIDTH, rendering.WINDOW_HEIGHT))
    pygame.display.set_caption("CartPole RL")
    clock = pygame.time.Clock()

    start_angle = random.uniform(-1.0, 1.0)
    state = physics.State(bar_angle=start_angle)
    accumulator = 0.0

    running = True
    while running:
        frame_time = clock.tick(FPS) / 1000
        frame_time = min(frame_time, MAX_FRAME_TIME)
        accumulator += frame_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        while accumulator >= PHYSICS_DT:
            state = physics.step(state, PHYSICS_DT)
            accumulator -= PHYSICS_DT

        screen.fill(rendering.BACKGROUND_COLOR)
        rendering.draw_cart_pole(screen, to_screen_x(state.cart_x), state.bar_angle)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()