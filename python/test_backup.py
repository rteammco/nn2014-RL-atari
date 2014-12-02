# Test the ALEInterface object.

import sys
import random
from ALEInterface import ALEInterface


#game = "space_invaders"
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

while True:
    s, r = interface.get_state_and_reward()
    #pass s,r to agent


    if not interface.game_running:
        break
    if frame % 100 == 0:
        print s
    
    #agent make decisions
    a = random.choice(actions)
    interface.do_action(a)
    frame += 1

interface.close()
