#!/usr/bin/python
'''
A little experiment on multiprocessing module.
The goal is to have the ability to spawn processes from multiprocessing.Process
By default that leads to AssertionError with the following text:
"Non-daemonic processes are not allowed to have children"

Requirements:
Python 3.5+ (though the method should work on python 2.7 as well)

As a modeling task, the calculation of PI with BBP algorithm was used.
'''
# STL
import multiprocessing as mp
import os, sys, re
import argparse
import logging
import decimal

# proj specific
import pi
import spawn_types
from spawn_types import check_positive
import parallel


def worker(arg):
    pass


def parse_args(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--processes', help='number of 1st level processes to spawn',
                        action='store', default=2, type=check_positive)
    parser.add_argument('--spawn-by', help='number of 2nd level processes to spawn',
                        action='store', default=2, type=check_positive)
    parser.add_argument('--pi-prec', help='number of hex digits of pi that would be calculated',
                        action='store', type=check_positive, default=500)
    parser.add_argument('--sequential', help='if set, program performs sequential calculation',
                        action='store_true', default=False)
    return parser.parse_args(args=args)


def main():
    args = parse_args()
    logging.debug('args: {}'.format(args))
    decimal.getcontext().prec = args.pi_prec*2  #XXX: check the dec. digits precision
    
    if args.sequential:
        print('pi(prec=%s) = %s' % (args.pi_prec, pi.calculate_pi_sequentially(args.pi_prec)))
        return

    p = spawn_types.NoDaemonPool(args.processes)
    callback = parallel.get_worker_callback(args.spawn_by)
    result = p.map(callback, parallel.get_ranges((0, args.pi_prec), args.processes))
    print(sum(result))

if __name__ == '__main__':
    main()
