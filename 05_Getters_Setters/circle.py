class Circle:

    VALID_COLORS = ('Red', 'Blue', 'Green')

    def __init__(self, radius, color):
        self._radius = radius
        self._color = color

    def get_radius(self):
        return self._radius
    
    def set_radius(self, new_radius):
        if isinstance(new_radius, int) and new_radius > 0:
            self._radius = new_radius
        else:
            print('Invalid format, please input an int data types and greater than 0.')
    
    radius = property(get_radius, set_radius)

    def get_color(self):
        return self._color
    
    def set_color(self, new_color):
        if new_color in Circle.VALID_COLORS:
            self._color = new_color
        else:
            print('Not a valid color.')
    
    color = property(get_color, set_color)


my_circle = Circle(3, 'Blue')
print(my_circle.radius)

my_circle.radius = 16
print(my_circle.radius)

print(my_circle.color)
my_circle.color = 'Red'
print(my_circle.color)
