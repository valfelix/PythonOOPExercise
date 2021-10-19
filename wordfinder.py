"""Word Finder: finds random words from a dictionary."""
from random import choice

class WordFinder:
    """Machine for finding random words from dictionary.
    
    >>> wf = WordFinder("words.txt")
    235886 words read
    """

    def __init__(self, path):
        """Read dictionary and report number of items read."""

        dict_file = open(path) # instantiated with a path to a file

        self.words = self.parse(dict_file) # calls parse method to make an attribute of a list of words in file

        print(f"{len(self.words)} words read") # then prints number of words in file

    def parse(self, dict_file):
        """Parse dict_file -> list of words."""

        return [w.strip() for w in dict_file] # remove leading/trailing characters from file and return as a list of words 

    def random(self):
        """Return random word."""

        return choice(self.words) # return random item from list of words

class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines and comments."""

    def parse(self, dict_file):
        """Parse dict_file -> list of words, skipping blanks and comments."""

        return [w.strip() for w in dict_file if w.strip() and not w.startswith("#")] # add a conditional for leading/trailing characters and comments
