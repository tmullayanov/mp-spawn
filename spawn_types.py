'''
types.py - provider of specific types

Types defined in this module:

PrecisionAction(argparse.Action)
'''
import argparse
import logging

class PrecisionAction(argparse.Action):
    '''
    Special type for parsing precision of calculation out of cmd args
    '''
    __default__ = 1000
    __negative_prec_warn__ = 'precision cannot be negative({}), using default value of {}'

    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError('nargs is not allowed')
        super(PrecisionAction, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_strings=None):
        logging.debug('values={}'.format(values))
        if values < 0:
            logging.warning(__negative_prec_warn__.format(values, __default__))
            values = __default__
        setattr(namespace, self.dest, values)
