from random import randint
from random import seed
from random import choice
import numpy as np

seed(1767673)

def int_to_roman(num):
    num = abs(num)
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    roman_num = ''
    idx = 0
    while  num > 0:
        for _ in range(num // val[idx]):
            roman_num += syb[idx]
            num -= val[idx]
        idx += 1
    return roman_num
    
def most_frequent(List): 
    return max(set(List), key = List.count) 

def least_frequent(List):
    return min(set(List), key = List.count)

def rotate_list(nums, u):
  return nums[u:] + nums[:u]



b = []
for c in range(19612):
    b.append(randint(37, 569))
