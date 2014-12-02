# Test the ALEInterface object.

import signal
import sys
import os
import random
from ALEInterface import ALEInterface
import cv2
from FrameImage import FrameImage


# cleanup routine for when exitting the program
def cleanup(signal = None, frame = None):
    if disp_screen:
        fi.close()
    interface.close()
    print "Cleanup done."


# exit nicely if ctrl+c
signal.signal(signal.SIGINT, cleanup)


# read arguments (ROM name, and display options)
if len(sys.argv) > 1:
    game = sys.argv[1]
    disp_screen = False
    video_fname = None
    if len(sys.argv) > 2 and "disp" in sys.argv[2]:
        disp_screen = True
        if len(sys.argv) > 3:
            video_fname = sys.argv[3]
else:
    print "Use: $ python test.py game_name [disp]"
    exit(0)


# compile the c++ code
os.system("cd ..; make")


interface = ALEInterface(game, disp_screen)
actions = interface.get_valid_actions()
if disp_screen:
    width, height = interface.get_screen_dimensions()
    fi = FrameImage(width, height, video_fname)

interface.start_new_game()
frame = 0
#A new agent here

while True:
    s, r = interface.get_state_and_reward()
    #pass s,r to agent

    if disp_screen:
        pixels = interface.get_pixels()
        fi.display(pixels)

    if not interface.game_running:
        break
    if frame % 100 == 0:
        print s
        print "reward =", r
    
    #agent make decisions
    a = random.choice(actions)
    interface.do_action(a)
    frame += 1

cleanup()
