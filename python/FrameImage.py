import cv2
import numpy as np
import random
import time


class FrameImage():

    FPS = 30
    WINDOW_NAME = "frame"

    def __init__(self, width, height):
        self.width = width
        self.height = height
        cv2.namedWindow(self.WINDOW_NAME)
        print "Initialized window with dimensions", width, "X", height

    # src: http://stackoverflow.com/questions/9710520/opencv-createimage-function-isnt-working
    def create_blank_image(self, rgb_color=(0, 0, 0)):
        """Create new image(numpy array) filled with certain color in RGB"""
        # Create black blank image
        image = np.zeros((self.height, self.width, 3), np.uint8) # TODO - need 3-channel?
        # Since OpenCV uses BGR, convert the color first
        color = tuple(reversed(rgb_color))
        # Fill image with color
        image[:] = color
        return image

    def get_image_from_pixels(self, pixels):
        image = self.create_blank_image()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        for y in range(self.height):
            for x in range(self.width):
                image.itemset((y, x), pixels[y*self.width + x])
        return image

    # for debugging
    def get_rand_pixels(self):
        pixels = []
        for i in range(self.width*self.height):
            pixels.append(random.randint(0, 255))
        return pixels

    def wait(self):
        cv2.waitKey()

    def snooze(self):
        cv2.waitKey(1)

    def display(self, pixels):
        if pixels is None:
            return
        image = self.get_image_from_pixels(pixels)
        # resize
        w = image.shape[1] * 3
        h = image.shape[0] * 3
        image = cv2.resize(image, (w, h))
        # invert color
        image = cv2.merge(np.subtract(255, cv2.split(image)))
        cv2.imshow(self.WINDOW_NAME, image)
        self.snooze() # needs to call to update correctly

    def close(self):
        cv2.destroyAllWindows()


if __name__ == "__main__":
    # test
    width = 100
    height = 50
    fi = FrameImage(width, height)
    fi.display(fi.get_rand_pixels())
    fi.wait()
    fi.close()
