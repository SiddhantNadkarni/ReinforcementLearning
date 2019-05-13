import gym
import matplotlib.pyplot as plt

videosDir = './RLvideos/'
env = gym.make('CartPole-v1')
num_episodes = 1000
env = gym.wrappers.Monitor(env, videosDir) #creates videos

steps_total = [] #to put step

for i_episodes in range(num_episodes):
	state = env.reset() #reset before each environment
	step = 0
	# for step in range(100): take 100 moves, never really reaches 100 moves
	while True:
		step +=1
		action = env.action_space.sample() #chooses random move of agent
		new_state, reward, done, info = env.step(action) #exectuting action
		# print(new_state) #prints 4 different numbers, refer wiki
		# print(info) #it is empty
		env.render()


		if done:
			steps_total.append(step)
			print("Episode finished after %s"%step)
			break #until episode is finished, run episode

print("Average number of steps %.2f"%((sum(steps_total))/num_episodes))
plt.plot(steps_total)
plt.show()