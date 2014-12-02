'''Project: reinforcement learning on Atari'''
'''config file: libraries, constants, and parameters'''

#libraries





#agent parameters
RIGHT = 3
LEFT = 4
NOOP = 0
ACTION_SET = [NOOP, RIGHT, LEFT] #for pong there are only two actions: 3: right, 4: left; 0: noop





#reinforcement learning parameters
NUM_EPISODE = 3
GAMMA = 0.9
EPSILON = 0.1
ALPHA = 0.3

REWARD_LOSS = -1.0
REWARD_WIN = 1.0
