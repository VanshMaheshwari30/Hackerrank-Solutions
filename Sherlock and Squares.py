#problem Statement
"""
Watson likes to challenge Sherlock's math ability. He will provide a starting and ending value that describe a range of integers, inclusive of the endpoints. 
Sherlock must determine the number of square integers within that range.
Problem_link --> https://www.hackerrank.com/challenges/sherlock-and-squares/problem
"""
from math import *
import os
import random
import re
import sys
# Complete the squares function below.
def squares(a, b):
    return (floor(sqrt(b)) - ceil(sqrt(a)) + 1)


q=int(input())
for i in range(0,q):
    a=list(map(int,input().split()))
    print(squares(a[0],a[1]))
