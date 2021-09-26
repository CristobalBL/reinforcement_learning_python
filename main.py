# Based on https://www.learndatasci.com/tutorials/reinforcement-q-learning-scratch-python-openai-gym/

import gym # How to install gym with conda?

env = gym.make("Taxi-v3").env # Create environment
env.reset() # reset environment

env.render() # render environment

# Show # of action and state space
print("Action Space {}".format(env.action_space))
print("State Space {}".format(env.observation_space))

# encode state
state = env.encode(3, 1, 2, 0) # (taxi row, taxi column, passenger index, destination index)
print("State:", state)

env.s = state
env.render()

# Reward table for state
for key in env.P[328]:
    # {action: [(probability, nextstate, reward, done)]}
    reward_row = env.P[328][key]
    print(key, reward_row)