# Python interface with the ALE C++ simulator code.

import subprocess
import Protocol
from ALEObject import ALEObject
from State import State


class ALEInterface():
    """Provides an interface to the C++ code through IPC."""
    
    def __init__(self, rom):
        """
        Tries to open up a subprocess for IPC with the C++ program.
        If successful, interaction will begin with initial data transaction.
        Also sets up the state, time, and reward variables.
        """
        cmd = "./proj " + rom
        try:
            self.proc = subprocess.Popen(cmd.split(),
                stdout = subprocess.PIPE, stdin = subprocess.PIPE)
            self.connect()
        except:
            self.proc = None
            print "Error: failed to run command '" + cmd + "'"
        self.t = 0
        self.valid_actions = []
        self.cur_state = None
        self.last_reward = None

    def writeline(self, msg):
        """Writes a single line out through the pipe."""
        if self.proc is None:
            return
        self.proc.stdin.write(msg + "\n")
        self.proc.stdin.flush()

    def readline(self):
        """Returns a line from the pipe with the trailing newline removed."""
        if self.proc is None:
            return ""
        return self.proc.stdout.readline().rstrip()

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

    def connect(self):
        """Establishes connection with the C++ code and receives valid actions."""
        greeting = self.get_next_message()
        print '\n'.join(greeting)
        actions = self.get_next_message()
        print actions

    def send(self):
        """Sends the current frame."""
        pass

    def get_valid_actions(self):
        """Returns a list of valid actions."""
        self.valid_actions

    def do_action(self, action):
        """Selects the chosen action ."""
        if action in self.valid_actions and self.ready:
            self.send(action)

    def get_state_and_reward(self):
        """
        Returns the current game state at time t and the reward at previous
        time t-1 as a tuple.
        """
        return self.cur_state, self.last_reward
