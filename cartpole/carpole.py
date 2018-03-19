# I got the initial ideas and code from kvfrans post:
# http://kvfrans.com/simple-algoritms-for-solving-cartpole/

import gym
import numpy as np
import matplotlib.pyplot as plt

def run_episode(env, parameters):
    observation = env.reset()
    totalreward = 0
    for _ in range(200):
        action = 0 if np.matmul(parameters,observation) < 0 else 1
        # print("params: ", parameters)
        # print("pre obs: ", observation)

        observation, reward, done, info = env.step(action)
        # print("pos obs:", observation)

        totalreward += reward
        if done:
            break
    return totalreward

env = gym.make('CartPole-v0')
# env.monitor.start('cartpole-experiments/', force=True)

counter = 0
bestparams = None  
bestreward = 0  
for _ in range(10000):  
    counter += 1
    parameters = np.random.rand(4) * 2 - 1
    reward = run_episode(env,parameters)
    if reward > bestreward:
        bestreward = reward
        bestparams = parameters
        # considered solved if the agent lasts 200 timesteps
        if reward == 200:
            break
            print("solved at: ", counter)