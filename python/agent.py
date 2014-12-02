#Agent

from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from config import *
import numpy
import random
#The learning agent for pong game
class Agent():
    def __init__(self):
        #neural network as function approximator
        #Initialize neural network
        self.nn = buildNetwork(4,20,3, bias = True)
    
    def updateNN(self, state, action, reward, state_new):
	#learning target
      	if reward == REWARD_WIN or reward == REWARD_LOSS: #terminal states
	    yi = reward
	else: #transition states
	    yi = reward + GAMMA * max(self.nn.activate(state_new))
      	dataSet = SupervisedDataSet(len(state),1)
  	dataSet.addSample(state, (yi))
  	
  	trainer = BackpropTrainer(self.nn, dataSet)
  	trainer.train()

  	dataSet.clear()

    def greedyAct(self,state):
  	Qvalues = self.nn.activate(state)
        action = numpy.argmax(Qvalues)
        return action
 
    def eGreedyAct(self, state):
      	#e-greedy action selection
	if random.random() > EPSILON:
	    action = greedyAct(state)
  	else:
	    action = random.choice(ACTION_SET)
       	return action

    def reflexAct(self,state):
	#state[1] is relBallY
	if abs(state[1] - 0) < 3:
	    action = NOOP
	elif state[1] < 0:
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
        x,y = raw_state.objects[i].box.center
	velX, velY = raw_state.objects[i].vel_x, raw_state.objects[i].vel_y
	#The player: playerX should be near 140 and velX should be 0
	if abs(x - 140) <= 1 and velX == 0: #empirical values
	    playerX, playerY = x, y
	    valid_obj_count += 1    	
	#The ball: velX should be non zero
	elif VelX != 0:
	    ballX, ballY, ballVX, ballVY = x, y, velX, velY
	    valid_obj_count += 1
	#The opponent: oppX should be near 17 and velX should be 0
	else: pass
	
    if valid_obj_count < 2:
	return is_valid_frame, old_state
    else:
	is_valid_frame = True
	new_state = #TBD
    	return is_valid_frame, new_state
