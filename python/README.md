test.py
----------
An example implementation of a random agent. Run using `python test.py game_name` where `game_name` is the name of the game you want to run (for example, `space_invaders`).

ALEInterface
----------
Provides an interface to the C++ code. The constructor takes two parameters: the name of the game (e.g. `space_invaders`) and whether or not you wish to show the display. The display doesn't really work anyway, so the parameter defaults to False.

Use `actions = interface.get_valid_actions()` before starting a game. This will return a list of integers that identify all possible actions the agent can take.

To start a new game, call `interface.start_new_game()`

Each frame, first get the state and reward by calling `s, r = interface.get_state_and_reward()`. NOTE: the reward is `None` for the first frame.

Figure out which action in the list of valid actions to take, and then call `interface.do_action(a)` with action `a` to execute that action. At this point, the frame ends.

State
----------
This is the "`s`" part of the `get_state_and_reward` value (`r` is just a numerical reward value). The state provides a time `t` and a list `objects` of `ALEObject` types (see below).

ALEObject
----------
This provides a description for every object that the game's Visual Processor sees. The `ALEObject` has the following parameters: `unique_id`, `vel_x`, `vel_y`, `box`, `frames_since_last_movement`, `age` (age is how many frames this object was seen). `box` is a `BoundingBox` object (see below).

BoundingBox
----------
Used to describe the location of each object. The bounding box is defined by `min_x`, `max_x`, `min_y`, and `max_y`. You can also call functions `width`, `height`, `area`, and `center` (returns x, y location of the object).
