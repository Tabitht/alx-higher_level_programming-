#!/usr/bin/python3

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """ An inherited class from Rectangle """
    def __init__(self, size):
        """ instantiate a new class """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)