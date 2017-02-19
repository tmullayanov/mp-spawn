'''
types.py - provider of specific types

Types defined in this module:

PrecisionAction(argparse.Action)
'''
import argparse
import logging
import pdb

def check_positive(value):
    '''Predicate which checks if the argument can be treated as positive int'''
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError('invalid positive int value: %s' % ivalue)
    return ivalue
