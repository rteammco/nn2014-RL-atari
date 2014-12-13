'''Project: reinforcement learning on Atari'''
'''config file: libraries, constants, and parameters'''

PONG = 0
BRIDER = 1
GAME = PONG


if GAME == PONG:
    #Neural Net
    nnFileName = 'pong.xml'
    loadWeightsFromFile = False
    NODE_INPUT = 3 #equivalent to state dimension
    NODE_HIDDEN = 7
    NODE_OUTPUT = 2
    
    #agent parameters
    #for pong there are only two actions: 3: right, 4: left
    #Do not use "noop" action since object detector won't detect static objects
    RIGHT = 0
    LEFT = 1
    ACTION_SET = [RIGHT, LEFT] 
    #Action offset, the action must add this offset when passing to the emulator
    OFFSET = 3

    #reinforcement learning parameters
    NUM_EPISODE = 5000
    GAMMA = 0.99
    EPSILON = 0.1
    ALPHA = 0.4
    
    REWARD_LOSS = -1.0
    REWARD_WIN = 1.0
    
    #To normalize state input
    MAX_X = 160.0 #max relative position X
    MAX_Y = 210.0
    MAX_BALL_VX = 2.0
    MAX_BALL_VY = 2.0
    
    PLAYER_Y, BALL_X, BALL_Y = 0,1,2 #NODE_INPUT

    TEST_EPISODE = 21
