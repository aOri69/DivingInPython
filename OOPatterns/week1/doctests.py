import doctest


def check_brackets(seq: str) -> bool:
    """
    Checking the correct brackets
    >>> check_brackets("([()])")
    True
    >>> check_brackets("()[)]((]{")
    False
    """
    pass


if __name__ == '__main__':
    doctest.testmod()
