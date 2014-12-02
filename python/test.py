# Test the ALEInterface object.

import sys
import random
from ALEInterface import ALEInterface
import agent
from config import *

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


interface = ALEInterface(game, disp_screen)
actions = interface.get_valid_actions()

interface.start_new_game()
frame = 0
#A new agent here
pongAgent = agent.Agent()

#Training episodes
for eps in range(NUM_EPISODE):
    #Initialize s
    s, r = interface.get_state_and_reward()
    
    #Training steps
    while True:
        if not interface.game_running:
            break
        if frame % 10 == 0:
            print(s)
#	    print r
        #agent chooses action according to e-greedy
        action = random.choice(actions)
	#action = pongAgent.selectAction(s)        
        interface.do_action(action)
		

        s, r = interface.get_state_and_reward()
        #update Q values
	#pongAgent.updateNN()
	
  	
        #s <- s_

   	

        frame += 1

interface.close()
