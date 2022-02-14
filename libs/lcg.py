# Python random module is not random enough to be used in sudoku solving nor generation.
# We started working on two linera congruential generators to generate (x, y) coordinates but
# using time as a seed is enough for our use case.

# LCGs are still found in our recursive algorithms.
# We do not use them anymore so we did not update them.

import time
import libs.config as config
from typing import Generator

# Returns a random number generator based on parameters.
# Parameters m and a will allow us to have different generators, seed will remain time_ns in our case.
def lcg(m, a, c, seed) -> Generator[int, None, None]:
    while True:
        seed = (a*seed + c) % m
        yield seed

def randrange(a, b):
    if config.get_random_generator_type() == 0:
        return randrange_light(a, b)
    elif config.get_random_generator_type() == 1:
        return randrange1(a, b)
    else:
        return randrange2(a, b)

# We need two randrange functions to generate non-related (x, y) coordinates.
def randrange1(a, b):
    return next(lcg((1<<16) + 1, 75, 74, time.time_ns()))%b + a #ZX81 LCG arguments.

def randrange2(a, b):
    return next(lcg(1 << 24, 0x43FD43FD, 0xC39EC3, time.time_ns()))%b + a #Microsoft Visual Basic LCG arguments.

# A simpler randrange function with no LCG.
def randrange_light(a, b):
    return time.time_ns()%b + a