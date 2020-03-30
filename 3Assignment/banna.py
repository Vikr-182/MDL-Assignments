from client import *
import numpy as np 
import requests
import json
from set_cur_state import set_current_state, get_current_state, state_range
import random
import time

array = [ 0 for i in range(10)]
print(array)
# string = 0
# for i in range(10):
#     string += 47 + array[i]
# dic = {}
# dic[string] = []
# print(dic[string])
# mse_array = get_errors("4wbRlSOEbHj0HmuzgNcnNc6KeW9ERzSsccXuswFyGlkn7bUMol",array)
# print(mse_array)
# dic[string] = mse_array
# with open("vc.txt","a") as f:
#     json.dump(dic,f)