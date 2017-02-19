#!/usr/bin/python
'''
A little experiment on multiprocessing module.
The goal is to have the ability to spawn processes from multiprocessing.Process
By default that leads to AssertionError with the following text:
"Non-daemonic processes are not allowed to have children"

Requirements:
Python 3.5+ (though the method should work on python 2.7 as well)

As a modeling task, the calculation of PI with BPP algorithm was used.
'''
# STL
import multiprocessing as mp
import os, sys, re
import argparse
import logging

# proj specific
from pi import bbp_term
from spawn_types import check_positive


def worker(arg):
    pass


def parse_args(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--processes', help='number of 1st level processes to spawn',
                        action='store', default=2, type=check_positive)
    parser.add_argument('--spawn-by', help='number of 2nd level processes to spawn',
                        action='store', default=2, type=check_positive)
    parser.add_argument('--pi-prec', help='number of hex digits of pi that would be calculated',
                        action='store', type=check_positive, default=1000)
    return parser.parse_args(args=args)


if __name__ == '__main__':
    args = parser.parse_args()
    logging.debug('args: {}'.format(args))
    logging.debug('calculating task sizes...')
    #pool = mp.Pool(args.processes)

    pass
