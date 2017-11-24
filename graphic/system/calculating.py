import math
from .parameters import *

def normalize_angle(angle):
    angle = angle % (2 * pi)
    angle = (angle + (2 * pi)) % (2 * pi)
    if (angle > pi):
        angle -= 2 * pi
    return angle


def sgn(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    return 0


def inverted(action, state):
    (x, v, a, θ, ω, α) = state

    cosθ, sinθ = math.cos(θ), math.sin(θ)
    Fp = action * F

    Nc = m_total * g - m_pole * l * (α * sinθ + (ω ** 2) * cosθ)

    α = (g * sinθ + cosθ * (
        ((-Fp - m_pole * l * (ω ** 2) * (sinθ + µc * sgn(Nc * v) * cosθ)) * (1 / m_total)) + µc * g * sgn(Nc * v)) - (
             (µp * ω) / (m_pole * l))) / (l * ((4 / 3) - ((m_pole * cosθ) / m_total) * (cosθ - µc * sgn(Nc * v))))

    a = (Fp + m_pole * l * ((ω ** 2) * sinθ - α * cosθ) - µc * Nc * sgn(Nc * v)) / m_total

    x += dt * v
    v += dt * a

    θ += dt * ω
    ω += dt * α

    return ((x, v, a, θ, ω, α), (dt * v), (dt * ω))
