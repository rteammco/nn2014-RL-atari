# Test the ALEInterface object.

import sys
import random
from ALEInterface import ALEInterface

import agent
from config import *

import cv2
from FrameImage import FrameImage

from copy import deepcopy

game = "pong"
if len(sys.argv) > 1:
    game = sys.argv[1]
    if len(sys.argv) > 2 and "disp" in sys.argv[2]:
        disp_screen = True
    else:
        disp_screen = False
else:
    print "Use: $ python test.py game_name [disp]"
    exit(0)


#A new agent here
pongAgent = agent.Agent()

for eps in range(NUM_EPISODE):
    interface = ALEInterface(game, disp_screen)
    actions = interface.get_valid_actions()
    if disp_screen:
        width, height = interface.get_screen_dimensions()
        fi = FrameImage(width, height)
    interface.start_new_game()   
   #Initialize s
    state = [0, 0, 0, 0]
    raw_state, reward = interface.get_state_and_reward()
    is_valid_frame, state = agent.process_state(state, raw_state)
    if reward == None: reward = 0
    frame = 0 
    #Training steps
    while int(reward) == 0:
	print("Training Episode:", 0, "Frame:", frame)
#        if frame % 1 == 0:
#	    print(state)
#	    print(reward)
        if disp_screen:
            pixels = interface.get_pixels()
            fi.display(pixels)
	print(state)
        #agent chooses action according to e-greedy
        action = random.choice(ACTION_SET)
	#action = pongAgent.reflexAct(state)        
        interface.do_action(action)
		
        raw_state, reward = interface.get_state_and_reward()
  	is_valid_frame, state_new = agent.process_state(state, raw_state)
  	
        #update Q values
#	pongAgent.updateNN(state, action, reward, state_new)
	
	state = deepcopy(state_new)
        frame += 1

    interface.close()

if disp_screen:
    fi.close()
#        if not interface.game_running:
#            break
 
