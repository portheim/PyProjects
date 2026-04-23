import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.width * 2) + (self.height * 2)

    def get_diagonal(self):
        return math.sqrt(pow(self.width, 2) + pow(self.height, 2))

    def get_picture(self):
        picture = ''
        if self.height > 50 or self.width > 50:
            return 'Too big for picture.'

        for h in range(0, self.height):
            for w in range(0, self.width-1):
                picture += '*'
            picture += '*\n'
        return picture            
    
    def get_amount_inside(self, shape):
        print(shape.width)
        print(shape.height)

    
        return math.floor(((self.width / shape.width) * (self.height / shape.height)))
    
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def __str__(self):
        return f'Square(side={self.side})'

    def set_side(self, value):
        self.side = value
        self.width = value
        self.height = value
    
    def set_width(self, width):
        self.set_side(width)
        
    def set_height(self, height):
        self.set_side(height)
    
    def get_picture(self):
        picture = ''
        for h in range(0, self.side):
            for w in range(0, self.side-1):
                picture += '*'
            picture += '*\n'
        return picture