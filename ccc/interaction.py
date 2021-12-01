"""
power x , N
"""

import datetime

def power(x, N):
    return x**N


def power_memory(x, N):
    lastResult = 1
    def g(x):
        nonlocal lastResult
        lastResult *= x
        return lastResult

    for i in range(N):
        lastResult = g(x)

    return lastResult

# test
def test_power_memory(x, N):
    start = datetime.datetime.now()
    result = power_memory(x,N)
    print(result)
    end = datetime.datetime.now()
    print(f'power_memory({x},{N})')
    print(f'time escaped: {end-start}\n')


def test_power(x, N):
    start = datetime.datetime.now()
    result = power(x,N)
    print(result)
    end = datetime.datetime.now()
    print(f'power({x},{N})')
    print(f'time escaped: {end-start}\n')

# main
test_power_memory(3,5)
test_power(3,5)

