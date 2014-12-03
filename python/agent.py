#Agent

from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from config import *
import numpy
import random
from pybrain.tools.customxml.networkwriter import NetworkWriter
from pybrain.tools.customxml.networkreader import NetworkReader

#The learning agent for pong game
class Agent:
    def __init__(self, loadWeightsFromFile, filename):
        #neural network as function approximator
        #Initialize neural network
        if loadWeightsFromFile:
	    self.nn = NetworkReader.readFrom(filename)
	else:
	    self.nn = buildNetwork(NODE_INPUT, NODE_HIDDEN, NODE_OUTPUT, bias = True)
    
    def updateNN(self, state, action, reward, state_new):
	#learning target
      	if reward == REWARD_WIN or reward == REWARD_LOSS: #terminal states
	    yi = reward
	else: #transition states
	    yi = reward + GAMMA * max(self.nn.activate(state_new))
      	dataSet = SupervisedDataSet(NODE_INPUT,NODE_OUTPUT)
	learn_target = self.nn.activate(state)
	learn_target[action] = yi
  	dataSet.addSample(state, learn_target) 
  	
  	trainer = BackpropTrainer(self.nn, dataSet)
  	trainer.train()

  	dataSet.clear()

    def greedyAct(self,state): 
        return numpy.argmax(self.nn.activate(state))
 
    def eGreedyAct(self, state):
      	#e-greedy action selection
	if random.random() > EPSILON:
	    action = self.greedyAct(state)
  	else:
	    action = random.choice(ACTION_SET)
       	return action

    def reflexAct(self,state):
	#state[1] is relBallY
#	if abs(state[1] - 0) < 2:
#	    action = 0 #NOOP
	if state[1] < 0:
	    action = RIGHT
	else:
	    action = LEFT 
        return action
    
def process_state(old_state, raw_state):
    #get the relative position between ball and player
    #ignore opponent now
    playerX, playerY = 0, 0 
    ballX, ballY, ballVX, ballVY = 0, 0, 0, 0
    oppX, oppY, oppVX, oppVY = 0, 0, 0, 0
    valid_obj_count = 0
    is_valid_frame = False
    
    for i in range(len(raw_state.objects)):
        x,y = raw_state.objects[i].box.center()
	velX, velY = raw_state.objects[i].vel_x, raw_state.objects[i].vel_y
	#The player: playerX should be near 140 and velX should be 0
	if abs(x - 140) <= 1 and velX == 0: #empirical values
	    playerX, playerY = x, y
	    valid_obj_count += 1    	
	#The ball: velX should be non zero
	elif velX != 0:
	    ballX, ballY, ballVX, ballVY = x, y, velX, velY
	    valid_obj_count += 1
	#The opponent: oppX should be near 17 and velX should be 0
	else: pass
	
    if valid_obj_count < 2:
	return is_valid_frame, old_state
    else:
	is_valid_frame = True
	new_state = [(ballY - playerY)/MAX_REL_Y]#, (ballVY)/MAX_BALL_VY]
	#new_state = [(ballX - playerX)/MAX_REL_X, (ballY - playerY)/MAX_REL_Y, (ballVX)/MAX_BALL_VX, (ballVY)/MAX_BALL_VY]
    	return is_valid_frame, new_state
