from enum import Enum


class CaseType(Enum):
    """
    An enumeration to define different text case transformations.
    """

    UPPER = 0
    LOWER = 1
    INVERSE = 2
    CAPITALIZED = 3
    TITLE = 4
    SENTENCE = 5
