from graphic import window


env = window.Application(gui=True)

totalReward = 0

while env.alive:

    # la ou on va prédire
    action = 0

    oldState = env.state

    state, reward, done = env.step(action)
    totalReward += reward

    if done:
        print(totalReward)
        totalReward = 0


print('Fin de la Simulation')
