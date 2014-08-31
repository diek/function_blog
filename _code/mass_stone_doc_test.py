import doctest


def mass_stone(kg):
    '''(number) -> number

    Return how much you weigh in stone, based upon mass in kilogram(s).
    Note we have to convert kg to pounds.

    >>> mass_stone(22)
    3.464402857142857
    >>> mass_stone(45)
    7.086278571428571
    >>> mass_stone(56)
    8.818490464
    >>> mass_stone(65)
    10.235735714285713
    '''
    return (kg * 2.20462) / 14

doctest.testmod(verbose=True)
