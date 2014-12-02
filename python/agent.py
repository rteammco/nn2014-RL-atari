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
        self.nn = buildNetwork(8,20,2, bias = True)
        #self.stateVector = []
        pass
    
    def updateNN(self, stateVector, reward):
	#learning target
      	yi = reward + GAMMA #TBD
      	dataSet = SupervisedDataSet(len(stateVector),1)
  	dataSet.addSample(stateVector, (yi))
  	
  	trainer = BackpropTrainer(self.nn, dataSet)
  	trainer.train()

  	dataSet.clear()

    def selectAction(self, stateVector):
      	Qvalues = self.nn.activate(stateVector)
        action = numpy.argmax(Qvalues)
       	#e-greedy action selection
	if random.random() > EPSILON:
	    action = numpy.argmax(Qvalues)
  	else:
	    action = random.choice([])#TBD
       	return action

    

