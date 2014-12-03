'''Project: reinforcement learning on Atari'''
'''config file: libraries, constants, and parameters'''

#Neural Net
nnFileName = 'train_00.xml'
loadWeightsFromFile = True
TRAINNING = False
NODE_INPUT = 1 #equivalent to state dimension
NODE_HIDDEN = 3
NODE_OUTPUT = 2



#agent parameters
RIGHT = 0
LEFT = 1
ACTION_SET = [RIGHT, LEFT] 
#for pong there are only two actions: 3: right, 4: left
OFFSET = 3
#Do not use noop since object detector won't detect static objects


#reinforcement learning parameters
NUM_EPISODE = 200
GAMMA = 0.9
EPSILON = 0.1
ALPHA = 0.3

REWARD_LOSS = -1.0
REWARD_WIN = 1.0

#To normalize state input
MAX_REL_X = 160.0 #max relative position X
MAX_REL_Y = 210.0
MAX_BALL_VX = 2.0
MAX_BALL_VY = 2.0
