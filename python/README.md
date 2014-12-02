test.py
----------
An example implementation of a random agent. Run using `python test.py game_name` where `game_name` is the name of the game you want to run (for example, `space_invaders`).

ALEInterface
----------
Provides an interface to the C++ code. The constructor takes two parameters: the name of the game (e.g. `space_invaders`) and whether or not you wish to show the display. Pixels data not be transferred if display is turned off. To interact with the emulator, call the following functions IN THIS ORDER:

Use `actions = interface.get_valid_actions()` before doing anything else. This will return a list of integers that identify all possible actions the agent can take.

If you have enabled the screen, call `width, height = interface.get_screen_dimensions()` to get the screen size of the emulator. If screen is not enabled, this will return `0, 0`.

To start a new game, call `interface.start_new_game()`. Do this only to start the first game, or after a game ends to play another one.

Each frame, first get the state and reward by calling `s, r = interface.get_state_and_reward()`. NOTE: the reward is `None` for the first frame. If the state is `None`, something probably went wrong.

If you are displaying the screen, call `pixels = interface.get_pixels()` to get the raw pixel data from the emulator for this frame. If the screen is not enabled, this will just return `None`.

Figure out which action in the list of valid actions to take, and then call `interface.do_action(a)` with action `a` to execute that action. At this point, the frame ends.

If at any point `interface.game_running` is `False`, then the game is over. You can at this point choose to start another game.

When you are done (i.e. after all the games you wanted to play are over), call `interface.close()` to clean up and exit.

FrameImage
----------
This object provides a means of displaying the raw grayscale pixels (obtained by calling `interface.get_pixels()` as described above) in a GUI window. The constructor takes two parameters: the screen width and height (again, obtained by calling `interface.get_screen_dimensions()`). To display an image, use the `FrameImage.display(pixels)` function, where `pixels` is the array of raw pixels obtained from the ALEInterface. The dimensions of this image are automatically adjusted using the provided screen width and height. When you're finished with the display, call `FrameImage.close()` to close any lingering GUI windows.

State
----------
This is the "`s`" part of the `get_state_and_reward` value (`r` is just a numerical reward value). The state provides a time `t` and a list `objects` of `ALEObject` types (see below).

ALEObject
----------
This provides a description for every object that the game's Visual Processor sees. The `ALEObject` has the following parameters: `unique_id`, `vel_x`, `vel_y`, `box`, `frames_since_last_movement`, `age` (age is how many frames this object was seen). `box` is a `BoundingBox` object (see below).

BoundingBox
----------
Used to describe the location of each object. The bounding box is defined by `min_x`, `max_x`, `min_y`, and `max_y`. You can also call functions `width`, `height`, `area`, and `center` (returns x, y location of the object).
