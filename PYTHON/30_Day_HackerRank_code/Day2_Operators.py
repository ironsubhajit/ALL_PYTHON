##@ironsubhajit
##HackerRank:
##Day2_problem:
##Task: Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.
##Note: Be sure to use precise values for your calculations, or you may end up with an incorrectly rounded resulttax_percent = int(input())

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip_percent=(meal_cost*tip_percent)/100
    tax_percent=(meal_cost*tax_percent)/100
    totalCost=(meal_cost+tip_percent+tax_percent)
    return(print(int(round(totalCost))))

if __name__ == '__main__':
    meal_cost = float(input()) 
    tip_percent = int(input())
    tax_percent = int(input())
    solve(meal_cost, tip_percent, tax_percent)
