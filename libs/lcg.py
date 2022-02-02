# Python random module is not random enought to be used in sudoku solving nor generation.
# We need our own random number generator and we need to be able to apply different seeds to it.
# A linear congruential generator is well suited for our application.

import time
from typing import Generator

# Returns a random number generator based on parameters.
# Parameters m and a will allow us to have different generators, seed will remain time_ns in our case.
def lcg(m, a, c, seed) -> Generator[int, None, None]:
    while True:
        seed = (a*seed + c) % m
        yield seed


#We need two randrange functions to generate non-related (x, y) coordinates.
def randrange(a, b):
    return lcg((2<<16) + 1, 75, 74, time.time_ns()).__next__()%b + a #ZX81 LCG arguments
    return time.time_ns() % b + a

def randrange2(a, b):
    #return lcg(2 << 24, 0x43FD43FD, 0xC39EC3, time.time_ns()).__next__()%b + a #Microsoft Visual Basic LCG arguments
    return time.time_ns() % b + a