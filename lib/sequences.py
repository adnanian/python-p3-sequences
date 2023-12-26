#!/usr/bin/env python3

def print_fibonacci(length):
    pass
    fibonacci_sequence = []
    x = 0
    for x in range(length):
        if x == 0:
            fibonacci_sequence.append(0)
        elif x == 1:
            fibonacci_sequence.append(1)
        else:
            next = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next)
    print(fibonacci_sequence)