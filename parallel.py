'''
parallel.py - functions for parallel calculations

Functions defined here:
task_size(range, nodes)
'''
__all__ = ['get_ranges', 'get_worker_callback']

def task_size(range, nodes):
    ''' Number of tasks for each node '''
    return range // nodes + 1


def get_ranges(interval, nodes):
    '''generator which yields intervals as 2-tuples: (start, end).
    Those intervals don't intersect (except for end of one interval might equal
    to the start of the other).
    Intervals are enough to do the computation on one node.
    '''
    start, finish = interval
    size = task_size(finish-start, nodes)

    for idx in range(nodes):
        left = start + idx * size
        right = start + (idx+1) * size
        right = right if right <= finish else finish
        yield (left, right)


def process_interval_seq(interval):
    '''
    worker function which applies pi.bbp_term to every value
    inside of the interval sequentially.
    Returns the sum of map
    '''
    import pi
    left, right = interval
    return sum(map(pi.bbp_term, range(left, right)))


def process_interval_mp(interval, spawn=4):
    '''
    worker function which applies pi.bbp_term to every value
    inside of the interval in parallel.
    Return the sum of that map
    '''
    import pi
    from spawn_types import NoDaemonPool as Pool

    left, right = interval
    ranges = get_ranges(interval, spawn)
    pool = Pool(spawn)
    r = pool.map(process_interval_seq, ranges)
    return sum(r)


def get_worker_callback(spawn_rate):
    return process_interval_seq if spawn_rate == 1 else process_interval_mp
