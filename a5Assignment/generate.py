left = [[0 for i in range(0,5)] for j in range(0,5)]
right = [[0 for i in range(0,5)] for j in range(0,5)]

for i in range(0,5):
    if i is 0:
        # take care for left
        left[i][i] = 0.75
        left[i][i+1] = 0.25
        # take care for right
        right[i][i+1] = 0.75
        right[i][i] = 0.25
    elif i is 4:
        # take care for left
        left[i][i-1] = 0.75
        left[i][i] = 0.25
        # take care for right
        right[i][i] = 0.75
        right[i][i-1] = 0.25
    elif i is not 0 and i is not 4:
        left[i][i-1] = 0.75
        left[i][i+1] = 0.25

        right[i][i+1] = 0.75
        right[i][i-1] = 0.25

for i in range(0,5):
    for j in range(0,5):
        print(left[i][j],end="|")
    print()


print()
print()


for i in range(0,5):
    for j in range(0,5):
        print(right[i][j],end="|")
    print()

tr = [[] for i in range(2)]
tr[0] = left
tr[1] = right

init_state = [[0 for i in range(0,5)]]
init_state[0][0] = init_state[0][1] = init_state[0][4] = 1/3
import sys
roll_num = int(sys.argv[1][-3:])
print("OLL" + str(roll_num))

x = 1 - ((roll_num % 40) + 1)/100
y = roll_num % 3
print(x,y)

table = [[0 for i in range(2)] for j in range(3)]
table[0] = [0.9,0.85]
table[1] = [0.8,0.95]
table[2] = [0.85,0.9]

# 0,1 for Left, Right
act = [1,0,0]

# 0,1 for Red,Green
obs = [0,1,1]

states = [0,0,1,1,0]
import numpy as np
# Take action

n = "\n"
p = " "
file = open(sys.argv[1] + ".txt","w")
file.write(sys.argv[1] + n)
file.write(str(x) + p + str(y) + n)


def mult(A,B):
    result = [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]
    return result

for a in range(3):
    print(init_state)
    print(tr[act[a]])
    num = mult(init_state,tr[act[a]])
    for i in range(len(num[0])):
        print("BEF" + str(table[y][states[i]]))
        print(num[0][i])
        num[0][i] =  table[y][states[i]]*num[0][i] if states[i] is obs[a] else (1 - table[y][states[i]])*num[0][i]
        print(num[0][i])
    print(num)
    total = 0
    for i in range(len(num[0])):
        total += num[0][i]
    normal = 1/total
    for i in range(len(num[0])):
        num[0][i] *= normal
    print(normal)
    print("NORMAL")
    init_state = num
    print(init_state)
    for jj in range(len(init_state[0])-1):
        file.write(str(init_state[0][jj]) + p)
    file.write(str(init_state[0][len(init_state[0])-1]) + n)
    

print(init_state)
