# ALE Object representation.


class BoundingBox():
    """A simple bounding box defined by 2D bounding values."""

    def __init__(self, min_x, max_x, min_y, max_y):
        """Initializes the bounding region from parameters."""
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y

    def center(self):
        """Returns the center of this bounding box."""
        center_x = (self.min_x + self.max_x) / 2
        center_y = (self.min_y + self.max_y) / 2
        return center_x, center_y

    def width(self):
        """Returns the width of this object."""
        return abs(self.max_x - self.min_x)

    def height(self):
        """Returns the height of this object."""
        return abs(self.max_y - self.min_y)

    def area(self):
        """Returns the area of this box."""
        return self.width() * self.height()
    
    def __str__(self):
        return "[{}, {}, {}, {}]".format(
            self.min_x, self.max_x, self.min_y, self.max_y)



class ALEObject():
    """Defines an object from the ALE emulator with object detection."""
    
    def __init__(self, params):
        """
        Stores all parameters as fields.
        The min/max boundaries are stored as a BoundingBox object.
        """
        self.unique_id = int(params[0])
        self.vel_x = int(params[1])
        self.vel_y = int(params[2])
        self.box = BoundingBox(int(params[3]),
                               int(params[4]),
                               int(params[5]),
                               int(params[6]))
        self.frames_since_last_movement = int(params[7])
        self.age = int(params[8])

    def __str__(self):
        return "Object " + str(self.unique_id) + ": " + str(self.box) + \
            " -> (" + str(self.vel_x) + ", " + str(self.vel_y) + ")" + \
            " age = " + str(self.age)
