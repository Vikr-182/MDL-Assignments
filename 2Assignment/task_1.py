import numpy as np 



#####################################################################################################################################################
##############################################  TASK 1    ##########################################################################################            
#####################################################################################################################################################            

enemy_health = [0,1,2,3,4]
num_arrows = [0,1,2,3]
stamina = [0,1,2]
util = [[[0 for k in range(3)] for i in range (4)] for j in range(5)]
gamma = 0.99
delta = 0.001

penalty = -5

file1 = open('./outputs/task_1_trace.txt','w')
actions = ["SHOOT","DODGE","RECHARGE"]

key = True
num = 0
line = ""
req = delta
reward = 10


for i in range(5):
    for j in range(4):
        for k in range(3):
            print(util[i][j][k],end="|")
            print(i,j,k,end="]")
        print(">>>>>")
    print("\n")
mini = -1e11
while key:
    # do it for every state
    key = False
    line += "iteration="
    line += str(num)
    line += "\n"
    print(num)
    print("............................................")
    # for i in range(5):
    #     for j in range(4):
    #         for k in range(3):
    #             print(util[i][j][k],end="|")
    #             print(i,j,k,end="]")
    #         print(">>>>>")
    #     print("\n")

    old_util = [[[util[j][i][k] for k in range(3)] for i in range (4)] for j in range(5)]
    for i in range(60):
        stam = i%3
        enemy = i//12
        anna = (i % 12)//3
        arrows = (i%12)//3
        
        line += "("
        line += str(enemy)
        line += ","
        line += str(arrows)
        line += ","
        line += str(stam)
        line += "):"
        if enemy is not 0:    
            final = [-1e11 for i in range(3)]
            
            if stam > 0 and anna > 0: 
                # SHOOT
                final[0] = 0.5*(util[enemy-1][anna-1][stam-1]) + 0.5*(util[enemy][anna-1][stam-1])
                final[0] = final[0]*gamma + 0.5*(reward + penalty) + 0.5*(penalty)
            if stam > 0:
                # DODGE
                if stam is 2:
                    # 100 points
                    final[1] = 0.8*(0.8*util[enemy][(anna+1)%4][stam-1] + 0.2*util[enemy][anna][stam-1]) + 0.2*(0.8*util[enemy][(anna+1)%4][stam-2] + 0.2*util[enemy][anna][stam-2])
                    final[1] = final[1]*gamma + penalty
                else:
                    final[1] = 0.8*util[enemy][(anna+1)%4][stam-1] + 0.2*util[enemy][anna][stam-1]
                    final[1] = final[1]*gamma + penalty

                # RECHARGE
            final[2] = 0.8*util[enemy][anna][(stam+1)%3] + 0.2*util[enemy][anna][stam]
            final[2] = final[2]*gamma + penalty

            # CALCULATE MAX UTILITY 
            policy = max(final[0],final[1],final[2])
            ind = 0
            if policy is final[1]:
                ind = 1
            elif policy is final[2]:
                ind = 2

            line += actions[ind]
            line += "=["
            line += '%.3f' %(policy)
            line += "]\n"
            if policy > mini:
                mini = policy
            
            # UPDATE EQUATION
            if abs(policy - old_util[enemy][anna][stam]) >= delta:
                key = True
            old_util[enemy][anna][stam] = policy

        else:
            line += "-1=[0.000]\n"

    num = num + 1
    util = old_util

# print(line)
print(mini)
file1.write(line)
file1.close()
            
            
#####################################################################################################################################################
#####################################################################################################################################################            
#####################################################################################################################################################            


#####################################################################################################################################################
##############################################  TASK 2 PART 1   #####################################################################################            
#####################################################################################################################################################            

enemy_health = [0,1,2,3,4]
num_arrows = [0,1,2,3]
stamina = [0,1,2]
util = [[[0 for k in range(3)] for i in range (4)] for j in range(5)]
gamma = 0.99
delta = 0.001

penalty = -2.5

file1 = open('./outputs/task_2_part_1_trace.txt','w')
actions = ["SHOOT","DODGE","RECHARGE"]

key = True
num = 0
line = ""
req = delta
reward = 10


for i in range(5):
    for j in range(4):
        for k in range(3):
            print(util[i][j][k],end="|")
            print(i,j,k,end="]")
        print(">>>>>")
    print("\n")
mini = -1e11
while key:
    # do it for every state
    key = False
    line += "iteration="
    line += str(num)
    line += "\n"
    print(num)
    print("............................................")
    # for i in range(5):
    #     for j in range(4):
    #         for k in range(3):
    #             print(util[i][j][k],end="|")
    #             print(i,j,k,end="]")
    #         print(">>>>>")
    #     print("\n")

    old_util = [[[util[j][i][k] for k in range(3)] for i in range (4)] for j in range(5)]
    for i in range(60):
        stam = i%3
        enemy = i//12
        anna = (i % 12)//3
        arrows = (i%12)//3
        
        line += "("
        line += str(enemy)
        line += ","
        line += str(arrows)
        line += ","
        line += str(stam)
        line += "):"
        if enemy is not 0:    
            final = [-1e11 for i in range(3)]
            
            if stam > 0 and anna > 0: 
                # SHOOT
                final[0] = 0.5*(util[enemy-1][anna-1][stam-1]) + 0.5*(util[enemy][anna-1][stam-1])
                final[0] = final[0]*gamma + 0.5*(reward + (-0.25)) + 0.5*(-0.25)
            if stam > 0:
                # DODGE
                if stam is 2:
                    # 100 points
                    final[1] = 0.8*(0.8*util[enemy][(anna+1)%4][stam-1] + 0.2*util[enemy][anna][stam-1]) + 0.2*(0.8*util[enemy][(anna+1)%4][stam-2] + 0.2*util[enemy][anna][stam-2])
                    final[1] = final[1]*gamma + penalty
                else:
                    final[1] = 0.8*util[enemy][(anna+1)%4][stam-1] + 0.2*util[enemy][anna][stam-1]
                    final[1] = final[1]*gamma + penalty

                # RECHARGE
            final[2] = 0.8*util[enemy][anna][(stam+1)%3] + 0.2*util[enemy][anna][stam]
            final[2] = final[2]*gamma + penalty

            # CALCULATE MAX UTILITY 
            policy = max(final[0],final[1],final[2])
            ind = 0
            if policy is final[1]:
                ind = 1
            elif policy is final[2]:
                ind = 2

            line += actions[ind]
            line += "=["
            line += '%.3f' %(policy)
            line += "]\n"
            if policy > mini:
                mini = policy
            
            # UPDATE EQUATION
            if abs(policy - old_util[enemy][anna][stam]) >= delta:
                key = True
            old_util[enemy][anna][stam] = policy
            # print("=================")
            # print(enemy,arrows,stam)
            # print(final)
            # print(str(actions[ind])+":"+str(policy))
            # print("_________________")
            # print(util)
        else:
            line += "-1=[0.000]\n"

    num = num + 1
    util = old_util


file1.write(line)
file1.close()
#####################################################################################################################################################
#####################################################################################################################################################            
#####################################################################################################################################################            


#####################################################################################################################################################
##############################################  TASK 2 PART 2   #####################################################################################            
#####################################################################################################################################################            

enemy_health = [0,1,2,3,4]
num_arrows = [0,1,2,3]
stamina = [0,1,2]
util = [[[0 for k in range(3)] for i in range (4)] for j in range(5)]
gamma = 0.1
delta = 0.001

penalty = -2.5

file1 = open('./outputs/task_2_part_2_trace.txt','w')
actions = ["SHOOT","DODGE","RECHARGE"]

key = True
num = 0
line = ""
req = delta
reward = 10


for i in range(5):
    for j in range(4):
        for k in range(3):
            print(util[i][j][k],end="|")
            print(i,j,k,end="]")
        print(">>>>>")
    print("\n")
mini = -1e11
while key:
    # do it for every state
    key = False
    line += "iteration="
    line += str(num)
    line += "\n"
    print(num)
    print("............................................")
    # for i in range(5):
    #     for j in range(4):
    #         for k in range(3):
    #             print(util[i][j][k],end="|")
    #             print(i,j,k,end="]")
    #         print(">>>>>")
    #     print("\n")

    old_util = [[[util[j][i][k] for k in range(3)] for i in range (4)] for j in range(5)]
    for i in range(60):
        stam = i%3
        enemy = i//12
        anna = (i % 12)//3
        arrows = (i%12)//3
        
        line += "("
        line += str(enemy)
        line += ","
        line += str(arrows)
        line += ","
        line += str(stam)
        line += "):"
        if enemy is not 0:    
            final = [-1e11 for i in range(3)]
            
            if stam > 0 and anna > 0: 
                # SHOOT
                final[0] = 0.5*(util[enemy-1][anna-1][stam-1]) + 0.5*(util[enemy][anna-1][stam-1])
                final[0] = final[0]*gamma + 0.5*(reward + penalty) + 0.5*(penalty)
            if stam > 0:
                # DODGE
                if stam is 2:
                    # 100 points
                    final[1] = 0.8*(0.8*util[enemy][(anna+1)%4][stam-1] + 0.2*util[enemy][anna][stam-1]) + 0.2*(0.8*util[enemy][(anna+1)%4][stam-2] + 0.2*util[enemy][anna][stam-2])
                    final[1] = final[1]*gamma + penalty
                else:
                    final[1] = 0.8*util[enemy][(anna+1)%4][stam-1] + 0.2*util[enemy][anna][stam-1]
                    final[1] = final[1]*gamma + penalty

                # RECHARGE
            final[2] = 0.8*util[enemy][anna][(stam+1)%3] + 0.2*util[enemy][anna][stam]
            final[2] = final[2]*gamma + penalty

            # CALCULATE MAX UTILITY 
            policy = max(final[0],final[1],final[2])
            ind = 0
            if policy is final[1]:
                ind = 1
            elif policy is final[2]:
                ind = 2

            line += actions[ind]
            line += "=["
            line += '%.3f' %(policy)
            line += "]\n"
            if policy > mini:
                mini = policy
            
            # UPDATE EQUATION
            if abs(policy - old_util[enemy][anna][stam]) >= delta:
                key = True
            old_util[enemy][anna][stam] = policy
            # print("=================")
            # print(enemy,arrows,stam)
            # print(final)
            # print(str(actions[ind])+":"+str(policy))
            # print("_________________")
            # print(util)
        else:
            line += "-1=[0.000]\n"

    num = num + 1
    util = old_util


file1.write(line)
file1.close()
#####################################################################################################################################################
#####################################################################################################################################################            
#####################################################################################################################################################            


#####################################################################################################################################################
##############################################  TASK 2 PART 3   #####################################################################################            
#####################################################################################################################################################            

enemy_health = [0,1,2,3,4]
num_arrows = [0,1,2,3]
stamina = [0,1,2]
util = [[[0 for k in range(3)] for i in range (4)] for j in range(5)]
gamma = 0.1
delta = 1e-10

penalty = -2.5

file1 = open('./outputs/task_2_part_3_trace.txt','w')
actions = ["SHOOT","DODGE","RECHARGE"]

key = True
num = 0
line = ""
req = delta
reward = 10


for i in range(5):
    for j in range(4):
        for k in range(3):
            print(util[i][j][k],end="|")
            print(i,j,k,end="]")
        print(">>>>>")
    print("\n")
mini = -1e11
while key:
    # do it for every state
    key = False
    line += "iteration="
    line += str(num)
    line += "\n"
    print(num)
    print("............................................")
    # for i in range(5):
    #     for j in range(4):
    #         for k in range(3):
    #             print(util[i][j][k],end="|")
    #             print(i,j,k,end="]")
    #         print(">>>>>")
    #     print("\n")

    old_util = [[[util[j][i][k] for k in range(3)] for i in range (4)] for j in range(5)]
    for i in range(60):
        stam = i%3
        enemy = i//12
        anna = (i % 12)//3
        arrows = (i%12)//3
        
        line += "("
        line += str(enemy)
        line += ","
        line += str(arrows)
        line += ","
        line += str(stam)
        line += "):"
        if enemy is not 0:    
            final = [-1e11 for i in range(3)]
            
            if stam > 0 and anna > 0: 
                # SHOOT
                final[0] = 0.5*(util[enemy-1][anna-1][stam-1]) + 0.5*(util[enemy][anna-1][stam-1])
                final[0] = final[0]*gamma + 0.5*(reward + (penalty)) + 0.5*(penalty)
            if stam > 0:
                # DODGE
                if stam is 2:
                    # 100 points
                    final[1] = 0.8*(0.8*util[enemy][(anna+1)%4][stam-1] + 0.2*util[enemy][anna][stam-1]) + 0.2*(0.8*util[enemy][(anna+1)%4][stam-2] + 0.2*util[enemy][anna][stam-2])
                    final[1] = final[1]*gamma + penalty
                else:
                    final[1] = 0.8*util[enemy][(anna+1)%4][stam-1] + 0.2*util[enemy][anna][stam-1]
                    final[1] = final[1]*gamma + penalty

            # RECHARGE
            final[2] = 0.8*util[enemy][anna][(stam+1)%3] + 0.2*util[enemy][anna][stam]
            final[2] = final[2]*gamma + penalty

            # CALCULATE MAX UTILITY 
            policy = max(final[0],final[1],final[2])
            ind = 0
            if policy is final[1]:
                ind = 1
            elif policy is final[2]:
                ind = 2

            line += actions[ind]
            line += "=["
            line += '%.3f' %(policy)
            line += "]\n"
            if policy > mini:
                mini = policy
            
            # UPDATE EQUATION
            if abs(policy - old_util[enemy][anna][stam]) >= delta:
                key = True
            old_util[enemy][anna][stam] = policy
            # print("=================")
            # print(enemy,arrows,stam)
            # print(final)
            # print(str(actions[ind])+":"+str(policy))
            # print("_________________")
            # print(util)
        else:
            line += "-1=[0.000]\n"

    num = num + 1
    util = old_util


file1.write(line)
file1.close()
#####################################################################################################################################################
#####################################################################################################################################################            
#####################################################################################################################################################            
