import json
import numpy as np
import math

def toCelcius(F):
    C = round(float((F-32)*(5/9)),2)
    return C
data = open('data.txt', 'r')
temp_dict = data.read().split()[24:]
lst = list(map(float, temp_dict))
temp2 ={}
for line in lst:
    lst[0] = int(lst[0])
    year = lst[0]
    lst.pop(0)
    lst = list(map(toCelcius, lst))
    temp2 = temp2.update({year:lst})
    print(temp2)
def avgTempYear():
    1