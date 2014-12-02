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
        self.nn = buildNetwork(4,20,2, bias = True)
    
    def updateNN(self, state, reward):
	#learning target
      	yi = reward + GAMMA #TBD
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
	    action = random.choice(ACTION_SET)#TBD
       	return action

    def reflexAct(self,state):
        return action
    
def validState(raw_state):
    #see if object detector is giving sufficient information, if not, do not do anything
    flag = True
    if len(raw_state.objects) < 2:
    	flag = False

    return flag

def process_state(raw_state):
    #get the relative position between ball and our pedal
    #ignore enemy now
    playerX, playerY = 0, 0 #positions of our own pedal
    ballX, ballY, ballVX, ballVY = 0, 0, 0, 0
    oppX, oppY, oppVX, oppVY = 0, 0, 0, 0
    for i in range(len(raw_state.objects)):
        x,y = raw_state.objects[i].box.center
	velX, velY = raw_state.objects[i].vel_x, raw_state.objects[i].vel_y
	#The pedal: pedalX should be near 140 and velX shold be 0
	if abs(x - 140) <= 2 and abs(velX - 0) <= 2: #empirical values
	    playerX, playerY = x, y    	
	#The ball: velX should be non zero
	elif abs(velX - 0) > 20:
	    ballX, ballY, ballVX, ballVY = x, y, velX, velY
	else:
    return
