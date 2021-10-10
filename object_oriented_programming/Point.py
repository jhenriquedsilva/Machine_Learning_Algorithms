import math

class Point:
    def reset(self):
        self.move(0,0)

    def move(self, x, y):
        self.x = x
        self.y = y

    def calculate_distance(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)
