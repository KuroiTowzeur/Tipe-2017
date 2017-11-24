# -*- coding: utf-8 -*-

import math

# world constantes
g = 9.81  # gravitational acceleration[m/s²]
pi = math.pi

# Simulation
fps = 60  # image par seconde
dt = 1 / 60  # dt

# Dimension de la fenetre d'affichage
screen_width_px = 800
screen_height_px = 600

# Rupture pour les episodes
θ_threshold = 3 * pi
x_threshold = 1.5

# output parameters
x0 = 0  # cart position[m]
v0 = 0  # cart velocity [m/s]
a0 = 0  # cart acceleration [m/s²]

θ0 = 0.1#pi  # angular  position [Rad]
ω0 = 0   # angular velocity pendulum[rad/s]
α0 = 0   # angular acceleration [rad/s²]

# cart
m_cart = 1.0  # cart weight [kg]
width_cart = 0.4  # cart width [m]
length_cart = 0.24  # cart length [m]

# pole
m_pole = 0.1  # pendulum weight [kg]
l = 0.5   # distance between pivot point and center of mass of first pendulum [m]
length_pole = l * 2  # pendulum length [m]
width_pole = 0.08  # pendulum width [m]
I_inertia = 0.011  # moment of inertia of first pendulum [kg.m²]

# global system
m_total = m_pole + m_cart

# friction
µp = 0.01  # coeficient of friction in the articulation connecting the pole to the cart [Ns/m]
# Cr = µp*ω
µc = 0.01  # coeficient of friction between the cart and the track [Ns/m]

# motor
k = 5.47  # motor constant [N/V]
F = 10.0  # force poussée / traction [N]
