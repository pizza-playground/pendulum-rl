from dataclasses import dataclass
from math import cos, sin

GRAVITY = 9.8
CART_MASS = 1.0
POLE_MASS = 0.1
POLE_HALF_LENGTH = 0.5

TOTAL_MASS = CART_MASS + POLE_MASS
POLE_MASS_LENGTH = POLE_MASS * POLE_HALF_LENGTH

CART_FRICTION = 0.1
POLE_FRICTION = 0.02


@dataclass
class State:
    cart_x: float = 0.0
    cart_velocity: float = 0.0
    bar_angle: float = 0.0
    bar_angular_velocity: float = 0.0


def step(state: State, dt: float, force: float = 0.0) -> State:
    sin_theta = sin(state.bar_angle)
    cos_theta = cos(state.bar_angle)

    temp = (
        force + POLE_MASS_LENGTH * state.bar_angular_velocity**2 * sin_theta
    ) / TOTAL_MASS

    angular_acceleration = (GRAVITY * sin_theta - cos_theta * temp) / (
        POLE_HALF_LENGTH * (4.0 / 3.0 - POLE_MASS * cos_theta**2 / TOTAL_MASS)
    )

    cart_acceleration = (
        temp - POLE_MASS_LENGTH * angular_acceleration * cos_theta / TOTAL_MASS
    )

    cart_acceleration -= CART_FRICTION * state.cart_velocity
    angular_acceleration -= POLE_FRICTION * state.bar_angular_velocity

    cart_velocity = state.cart_velocity + cart_acceleration * dt
    cart_x = state.cart_x + cart_velocity * dt

    bar_angular_velocity = state.bar_angular_velocity + angular_acceleration * dt
    bar_angle = state.bar_angle + bar_angular_velocity * dt

    return State(cart_x, cart_velocity, bar_angle, bar_angular_velocity)