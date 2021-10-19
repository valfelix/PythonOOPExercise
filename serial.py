"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=0):
        """Make a new generator, starting at start."""
        self.start = self.next = start # to begin with, the given start is the start and the next element 
    
    def __repr__(self):
        """Return representation string."""
        return f"<SerialGenerator start={self.start} next={self.next}>"
    
    def generate(self):
        """Generate unique serial number incremented by one."""
        self.next += 1 # next should be incremented by one
        return self.next 
    
    def reset(self):
        """Reset serial number back to start"""
        self.next = self.start # next value is reset to equal back to start value

