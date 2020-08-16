import multiprocessing
from fileinput import filename
from functools import partial
from multiprocessing.pool import ThreadPool

from timer import timer

import os

def factorize_naive(n):
    """ A naive factorization method. Take integer 'n', return list of
        factors.
    """
    if n < 2:
        return []
    factors = []
    p = 2

    while True:
        if n == 1:
            return factors

        r = n % p
        if r == 0:
            factors.append(p)
            n = n / p
        elif p * p >= n:
            factors.append(n)
            return factors
        elif p > 2:
            # Advance in steps of 2 over odd numbers
            p += 2
        else:
            # If p == 2, get to 3
            p += 1
    assert False, "unreachable"


DATA_SIZE = 1_000_000
workers = 7

### Single-threaded version
result = {}
data = [n for n in range(DATA_SIZE)]

# realization with multi processes
def factorize_number_processes(n):
    result[n] = factorize_naive(n)


def factorize_naive_run(n):
  return n, factorize_naive(n)


def save_to_file(name, input):
    with open(name+'.txt', 'w') as f:
        f.write(str(input))


with timer('Elapsed processes: {}s'):
    with multiprocessing.Pool(workers) as pool:
        input_data = [n for n in range(DATA_SIZE)]
        result = {
            n: factors
            for n, factors in pool.map(factorize_naive_run, input_data)
        }
        # save_to_file("multi_processes", result)


with timer('Elapsed threads: {}s'):
    with ThreadPool(workers) as pool:
        input_data = [n for n in range(DATA_SIZE)]
        pool.map(factorize_number_processes, input_data)
        # save_to_file("multi_threads", result)

