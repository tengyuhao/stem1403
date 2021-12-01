"""
power(x , N)

sum = x + x^2 + x^3 + x^4 + ... x^N
"""

import datetime
import time


def sum_power(x, N):
    s = 0
    for i in range(1, N+1):
        s = s + x**i
    return s

def sum_power_memory(x, N):
    s = 0
    lastResult = 1
    def g(x):
        nonlocal lastResult
        lastResult *= x
        return lastResult

    for i in range(N):
        lastResult = g(x)
        s += lastResult

    return s

# test
def test_power(x, N):
    # start = datetime.datetime.utcnow()
    # print(start.strftime("%H:%M:%S.%f"))
    start = time.time_ns()
    print(start)
    result = sum_power(x,N)
    print(result)
    # end = datetime.datetime.utcnow()
    # print(end.strftime("%H:%M:%S.%f"))
    end = time.time_ns()
    print(end)
    print(f'sum_power({x},{N})')
    print(f'time escaped: {(end-start)/1000/1000:.3f}ms\n')

def test_power_memory(x, N):
    # start = datetime.datetime.now()
    # print(start.strftime("%H:%M:%S.%f"))
    start = time.time_ns()
    print(start)
    result = sum_power_memory(x,N)
    print(result)
    # end = datetime.datetime.now()
    # print(end.strftime("%H:%M:%S.%f"))
    end = time.time_ns()
    print(end)
    print(f'sum_power_memory({x},{N})')
    print(f'time escaped: {(end-start)/1000/1000:.3f}ms\n')




# main
test_power(999,9999)
test_power_memory(999,9999)

