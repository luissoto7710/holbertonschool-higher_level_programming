#!/usr/bin/python3
class Square:
    """Defines a square by size and provides area calculation."""
    
    def __init__(self, size=0):
        """Initialize the square with a given size, defaulting to 0.
        
        Args:
            size (int): The side length of the square.
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2
