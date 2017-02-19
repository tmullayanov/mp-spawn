'''
types.py - provider of specific types

Types defined in this module:

PrecisionAction(argparse.Action)
'''
import argparse
import loggings

class PrecisionAction(argparse.Action):
    '''
    Special type for parsing precision of calculation out of cmd args
    '''
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError('nargs is not allowed')
        super(PrecisionAction, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_strings=None):
        logging.debug('values={}'.format(values))
        logging.debug('type(values)={}'.format(type(values)))
        setattr(namespace, self.dest, values)
