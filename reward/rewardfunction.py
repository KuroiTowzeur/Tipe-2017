import numpy as np

#deer.readthedocs.io/en/latest/user/environments/toy_env_pendulum.html

def reward(x, v , theta, thetadot):

    a = - abs(theta) #such that the agent receives 0 when the pole is standing up,
                     # and a negative reward proportional to the angle otherwise.
    b = - abs(x)/2 # receive negative reward when

    return a + b

#- x * x




