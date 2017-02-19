'''
types.py - provider of specific types

Types defined in this module:

PrecisionAction(argparse.Action)
'''
import argparse
import logging
import multiprocessing as mp
import multiprocessing.pool as pool

def check_positive(value):
    '''Predicate which checks if the argument can be treated as positive int'''
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError('invalid positive int value: %s' % ivalue)
    return ivalue


class NoDaemonProcess(mp.Process):
    ''' Just like multiprocessing.Process, only non-daemonic'''
    @property
    def daemon(self):
        return False

    @daemon.setter
    def daemon(self, value):
        pass

class NoDaemonPool(pool.Pool):
    Process = NoDaemonProcess
