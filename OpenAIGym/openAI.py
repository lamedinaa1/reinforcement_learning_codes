#Every environment specifies the format of valid actions and observations
#with the env.action_space and env.observation_space attributes

import gymnasium as gym 
import time
env = gym.make("LunarLander-v2", render_mode="human")

observation,info = env.reset()
#env.action_space and env.observation_space attributes

print(observation,info)

for i in range(1000): 
    action = env.action_space.sample()
    print(i,action)
    observation,reward,terminated,truncated,info = env.step(action)
    time.sleep(1)
    if terminated or truncated:
        print('terminated') 
        observation,info = env.reset()

