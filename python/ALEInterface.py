# Python interface with the ALE C++ simulator code.

import subprocess
import Protocol
from ALEObject import ALEObject
from State import State

EXEC = "../proj"


class ALEInterface():
    """Provides an interface to the C++ code through IPC."""
    
    def __init__(self, rom, disp_screen = False):
        """
        Tries to open up a subprocess for IPC with the C++ program.
        If successful, interaction will begin with initial data transaction.
        Also sets up the state, time, and reward variables.
        """
        self.t = 0
        self.valid_actions = []
        self.game_running = False
        self.cur_state = None
        self.last_reward = None
        self.disp_screen = disp_screen
        self.screen_width = 0
        self.screen_height = 0
        cmd = EXEC + " " + rom
        try:
            self.proc = subprocess.Popen(cmd.split(),
                stdout = subprocess.PIPE, stdin = subprocess.PIPE)
            self.connect(disp_screen)
        except:
            self.proc = None
            print "Error: failed to run command '" + cmd + "'"
        print "Running", rom, "(screen = " + str(disp_screen) + ")"

    def writeline(self, msg):
        """Writes a single line out through the pipe."""
        if self.proc is not None:
            self.proc.stdin.write(msg + "\n")
            self.proc.stdin.flush()

    def readline(self):
        """Returns a line from the pipe with the trailing newline removed."""
        if self.proc is not None:
            return self.proc.stdout.readline().rstrip()
        else:
            return ""

    def get_next_message(self):
        """
        Returns the next message sent by the C++ code as a list of lines.
        Any output received before the message is ignored.
        """
        line = self.readline()
        while line != Protocol.MESSAGE_START:
            line = self.readline()
        message = []
        line = self.readline()
        while line != Protocol.MESSAGE_END:
            message.append(line)
            line = self.readline()
        return message

    def send_message(self, messages):
        """
        Sends the given list of messages to the C++ code.
        If you're only sending one message, pass it as a list anyway.
        """
        self.writeline(Protocol.MESSAGE_START)
        for msg in messages:
            self.writeline(msg)
        self.writeline(Protocol.MESSAGE_END)

    def connect(self, disp_screen):
        """Establishes connection with the C++ code and receives valid actions."""
        greeting = self.get_next_message()
        print '\n'.join(greeting)
        self.send_message(str(disp_screen))
        actions = self.get_next_message()
        self.valid_actions = map(int, actions)
        if disp_screen:
            self.screen_width = int(self.get_next_message()[0])
            self.screen_height = int(self.get_next_message()[0])

    def recv_state(self):
        """Reads a state from C++ and returns the State object."""
        obj_params = self.get_next_message()
        if Protocol.END_GAME in obj_params:
            self.game_running = False
            return False
        self.cur_state = State(self.t)
        num_objs = len(obj_params)/9 # TODO - define 9 elsewhere
        print obj_params, num_objs
        for i in range(num_objs):
            obj_indx = i*9 # TODO - also same as above
            print "obj:", obj_params[obj_indx:obj_indx+9]
            obj = ALEObject(obj_params[obj_indx:obj_indx+9]) # TODO - again (+9)
            self.cur_state.add_object(obj)
        self.t += 1
        return True

    def send_action_get_reward(self, action):
        """Sends the selected action and gets the reward."""
        self.send_message([str(action)])
        self.last_reward = self.get_next_message()

    def get_valid_actions(self):
        """Returns a list of valid actions."""
        return self.valid_actions

    def do_action(self, action):
        """Selects the chosen action ."""
        if action in self.valid_actions:
            self.send_action_get_reward(action)
        else:
            raise "Invalid Action!"

    def get_state_and_reward(self):
        """
        Returns the current game state at time t and the reward at previous
        time t-1 as a tuple.
        """
        if not self.recv_state():
            return None, None
        else:
            return self.cur_state, self.last_reward
    
    def get_screen_dimensions(self):
        """Returns the width and height of the ALE screen."""
        return self.screen_width, self.screen_height

    def get_pixels(self):
        """
        If screen is enabled, reads pixel values from the C++ code and
        returns the pixel list. If not enabled, returns None.
        """
        if not self.disp_screen:
            return None
        pix_str = self.get_next_message()[0]
        pixels = map(int, pix_str.split())
        return pixels

    def start_new_game(self):
        """Tells the C++ code to start a new game (until game over)."""
        self.send_message([Protocol.START_GAME])
        self.game_running = True

    def close(self):
        """Closes the pipe (if it exists) and cleans up."""
        if self.proc is not None:
            self.send_message([Protocol.END_GAME])
            self.proc.terminate()
            self.proc = None
            self.game_running = False
