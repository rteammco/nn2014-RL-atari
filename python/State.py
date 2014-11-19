# Game state object

class State():
    """State object of the state-action-reward set."""
    
    def __init__(self, t):
        """Initialize the current state at time t."""
        self.t = t
        self.objects = []

    def add_object(self, obj):
        """Adds a new ALEObject to the current state."""
        self.objects.append(obj)

    def __str__(self):
        rep = "State at time t=" + str(self.t)
        for obj in self.objects:
            rep += "\n" + str(obj)
        return rep.rstrip()
