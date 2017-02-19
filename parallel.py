'''
parallel.py - functions for parallel calculations

Functions defined here:
task_size(range, nodes)
'''

def task_size(range, nodes):
    ''' Number of tasks for each node '''
    return range // nodes + 1

def get_ranges(range, nodes):
    '''generator which yields intervals as 2-tuples: (start, end).
    Those intervals don't intersect (except for end of one interval might equal
    to the start of the other).
    Those intervals are enough to do the computation on one node.
    '''
    size = task_size(range, nodes)
    for idx in range(nodes):
        left = idx*task_size
        right = (idx+1) * task_size
        right = right if right <= range else range
        yield (left, right)


def process_interval(interval):
    import pi
    left, right = interval
    return sum(map(pi.bbp_term, range(left, right)))
