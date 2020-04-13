import json 
import numpy

with open("./outputs/output.json") as f:
    dic = json.load(f)

print(dic["a"])
