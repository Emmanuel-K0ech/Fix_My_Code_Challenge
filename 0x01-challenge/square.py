#!/usr/bin/python3
"""This is the Square Class Module """


class Square():
    """ Square class 
        Arguments:
            width: int
            height: int
    """
    width = 0
    height = 0

    
    def __init__(self, *args, **kwargs):
        """ Instantiation method """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """ Method that finds perimeter of my square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Prints string representation """
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    """ Creating square object """
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
