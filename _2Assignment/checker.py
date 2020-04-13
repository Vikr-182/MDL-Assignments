import json 
import numpy

with open("./outputs/output.json") as f:
    dic = json.load(f)

with open("./sharma.json") as f1:
    gic = json.load(f1)

with open("./report/rara.json") as f2:
    gic = json.load(f2)

for i in dic["policy"]:
    print(i)
    for j in gic["policy"]:
        if i[0] is j[0]:
            if i[1] is not j[1]:
                print("SHIIIT")

for i in range(60):
    for j in range(100):
        print(dic["a"][i][j],gic["a"][i][j])
