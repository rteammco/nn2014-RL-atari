# Game state object

class State():
    """State object of the state-action-reward set."""
    
    def __init__(self, t):
        """Initialize the current state at time t."""
        self.t = t
        self.objects = []

    def add_object(obj):
        """Adds a new ALEObject to the current state."""
        self.objects.append(obj)
