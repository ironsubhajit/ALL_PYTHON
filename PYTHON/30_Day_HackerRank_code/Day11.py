#!/bin/python3
##HackerRank 30 Day Code:
##sub: 2D Array HourGlass_Sum

import math
import os
import random
import re
import sys

def _get_hourglass_sum(grid, i, j):
    sum = 0
    sum += grid[i-1][j-1]
    sum += grid[i-1][j]
    sum += grid[i-1][j+1]
    sum += grid[i][j]
    sum += grid[i+1][j-1]
    sum += grid[i+1][j]
    sum += grid[i+1][j+1]
    return sum

if __name__ == '__main__':
    arr = []
    max_hourglass_sum = -63 #-9<A|i||j|<9

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split(" ")))) #The "rstrip()" removes characters from the right based on the argument 
    for i in range(1,5): #0'th &n'th index isn't count on hourGlass_sum So 1 to (n-1)=5
        for j in range(1,5):
            current_hourglass_sum = _get_hourglass_sum(arr, i, j)
            if current_hourglass_sum > max_hourglass_sum:
                max_hourglass_sum = current_hourglass_sum
    print(max_hourglass_sum)
