from graphic import window
import graphic.system.parameters as cnst


win = window.Application()

while win.alive:
    win.render()

    action = 0
    win.realStep(action)


print('Fin de la Simulation')
#######

import numpy as np


parameters = np.random.rand(4) * 2 - 1

action = 0 if np.matmul(parameters,observation) < 0 else 1

def run_episode(env, parameters):
    observation = env.reset()
    totalreward = 0

    for _ in xrange(200):
        action = 0 if np.matmul(parameters,observation) < 0 else 1
        observation, reward, done, info = env.step(action)
        totalreward += reward
        if done:
            break
    return totalreward


bestparams = None
bestreward = 0

for episode in xrange(1000):
    parameters = np.random.rand(4) * 2 - 1
    reward = run_episode(env, parameters)

    if reward > bestreward:
        bestreward = reward
        bestparams = parameters
        # considered solved if the agent lasts 200 timesteps
        if reward == 200:
            break

