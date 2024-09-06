# CartPole
import time
import gymnasium as gym 

env = gym.make('CartPole-v1',render_mode='human')

observation,_ = env.reset()

print(observation)


# for i in range(100):

#     env.render()
#     time.sleep(0.1)
#     action = env.action_space.sample()
#     print(i,action)
#     observation,reward,terminated,truncated, info = env.step(action)
#     if terminated:
#         print(f'terminated: {terminated}, truncated:{truncated}') 
#         print('terminated')
#         observation,info = env.reset()



for episode in range(100):
    env.reset()
    done = False

    while not done: 
        env.render()
        time.sleep(0.1)
        action = env.action_space.sample()
        print(f'episode:{episode}, action: {action}')
        observation,reward,terminated,truncated,info = env.step(action)
        if terminated or truncated: 
            done = True