# Test the ALEInterface object.

import sys
import random
from ALEInterface import ALEInterface
import cv2
from FrameImage import FrameImage


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

fi = FrameImage(250, 120) # TODO w/h of window?
fi.display(fi.get_rand_pixels())
fi.wait()
while True:
    s, r = interface.get_state_and_reward()
    #pass s,r to agent

    # TODO - change to actual pixel values
    fi.display(fi.get_rand_pixels())
    fi.snooze()
    #fi.wait()

    if not interface.game_running:
        break
    if frame % 100 == 0:
        print s
    
    #agent make decisions
    a = random.choice(actions)
    interface.do_action(a)
    frame += 1

interface.close()
fi.close()
