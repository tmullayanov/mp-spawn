'''
parallel.py - functions for parallel calculations

Functions defined here:
task_size(range, nodes)
'''
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
    import pi
    left, right = interval
    return sum(map(pi.bbp_term, range(left, right)))
