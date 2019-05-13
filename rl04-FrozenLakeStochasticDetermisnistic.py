import gym
import matplotlib.pyplot as plt
import time

from gym.envs.registration import register
register(
    id='FrozenLakeNotSlippery-v0',
    entry_point='gym.envs.toy_text:FrozenLakeEnv',
    kwargs={'map_name' : '4x4', 'is_slippery': False}, #set slippery flag to false
    max_episode_steps=100,
    reward_threshold=0.78, # optimum = .8196
)
env = gym.make('FrozenLakeNotSlippery-v0')
num_episodes = 1000

steps_total = [] #to put step

for i_episodes in range(num_episodes):
	state = env.reset() #reset before each environment
	step = 0
	# for step in range(100): take 100 moves, never really reaches 100 moves
	while True:
		step +=1
		action = env.action_space.sample() #chooses random move of agent
		new_state, reward, done, info = env.step(action) #exectuting action
		time.sleep(0.4)

		env.render()
		print(new_state) #prints 4 different numbers, refer wiki
		print(info) #it is empty

		


		if done:
			steps_total.append(step)
			print("Episode finished after %s"%step)
			break #until episode is finished, run episode

print("Average number of steps %.2f"%((sum(steps_total))/num_episodes))
plt.plot(steps_total)
plt.show()