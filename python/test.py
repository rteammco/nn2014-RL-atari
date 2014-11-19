# Test the ALEInterface object.

import random
from ALEInterface import ALEInterface


#game = "space_invaders"
game = "asteroids"
interface = ALEInterface(game)
actions = interface.get_valid_actions()
for i in range(3000):
    s, r = interface.get_state_and_reward()
    if i % 100 == 0:
        print s
    a = random.choice(actions)
    interface.do_action(a)
