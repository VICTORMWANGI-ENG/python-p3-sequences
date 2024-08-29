#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    if length == 0:
        print([])
    elif length == 1:
        print([0]) 
    elif length == 2:
        print(fibonacci_list[0:2])
    elif length == 10:
        print(fibonacci_list[0:10])       

print_fibonacci(2)