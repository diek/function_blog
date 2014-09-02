def get_age(current_year, birth_year):
    ''' (num, num) -> num
    Determine age by substraction

    >>> get_age(2014, 1985)
    29
    >>> get_age(2014, 1966)
    48
    >>> get_age(2014, 1980)
    34
    '''
    return current_year - birth_year
