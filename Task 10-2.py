class Shape:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'


class Point(Shape):
    pass

class Circle(Shape):

    def __init__(self, x, y, radius):
        super(Circle, self).__init__(x,y)
        self.radius = radius

    def check_point_in_circle(self, point):
        if (point.x - self.x)**2 + (point.y - self.y)**2 < self.radius**2:
            print(f'Point {point} is inside the circle with the center ({self.x}, {self.y}) and radius {self.radius}')
            return True
        else:
            print(f'Point {point} is not inside the circle with the center ({self.x}, {self.y}) and radius {self.radius}')
            return not True

circle = Circle(4, 4, 2)
point = Point(5,5)
circle.check_point_in_circle(point)
