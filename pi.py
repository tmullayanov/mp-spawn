'''
pi.py

Supplementary module providing function to calculate pi.
'''

from decimal import Decimal as Dec

def bbp_term(k):
    '''Calculates k-th hexademical digit of pi.'''
    first = Dec('4') / Dec(str(8*k+1))
    second = Dec('2') / Dec(str(8*k+4))
    third = Dec('1') / Dec(str(8*k+5))
    fourth = Dec('1') / Dec(str(8*k+6))

    return (first - second - third - fourth) / Dec(str(16**k))

def calculate_pi_sequentially(precision):
    assert precision > 0, "Cannot calculate negative precision!"
    return sum(map(bbp_term, range(precision)))
