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



class ALEObject():
    """Defines an object from the ALE emulator with object detection."""
    
    def __init__(self, unique_id,
                 vel_x, vel_y,
                 min_x, max_x, min_y, max_y,
                 frames_since_last_movement, age):
        """
        Stores all parameters as fields.
        The min/max boundaries are stored as a BoundingBox object.
        """
        self.unique_id = unique_id
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.box = BoundingBox(min_x, max_x, min_y, max_y)
        self.frames_since_last_movement = frames_since_last_movement
        self.age = age
