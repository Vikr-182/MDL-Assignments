anna="bond"
import os
import json
import numpy as np
import cvxpy as cp

#######################################################################################
############################ NOOP SHOOT DODGE RECHARGE ###############################
#######################################################################################

#######################################################################################
################ Initialisation of arrays and length ##################################
#######################################################################################
Y = -5
enemy = [0,1,2,3,4]
arrows = [0,1,2,3]
stamina = [0,1,2]
es = len(enemy)
ass = len(arrows)
ss = len(stamina)
total = es*ass*ss
init_state_enemy = 4
init_state_arr = 3
init_state_stamina = 2
r = []
policy = []
filename = "./outputs/output.json"
#######################################################################################


#######################################################################################
################ Some useful functions ################################################
#######################################################################################
def num(enem,arrows,stam):
    return 12*enem + 3*arrows + stam

def mun(numm):
    return [int(numm//12),int((numm%12)//3),int(numm%3)]

def inc_life(n):
    arr = mun(n)
    return num(arr[0],arr[1],(arr[2]+4)%3)

def dec_life(n):
    arr = mun(n)
    return num(arr[0],arr[1],(arr[2]+2)%3)

def inc_arrows(n):
    arr = mun(n)
    return num(arr[0],(arr[1]+1)%4,arr[2])

def dec_arrows(n):
    arr = mun(n)
    return num(arr[0],(arr[1]+3)%4,arr[2])

def dec_ene(n):
    arr = mun(n)
    return num((arr[0]+4)%5,arr[1],arr[2])

def recharge(dic,i,count):
    dic["a"][inc_life(i)][count] = -0.8                             #   recharge successfull-1
    dic["a"][i][count] = 0.8                                        #   recharge successfull-2

def shoot(dic,i,count):
    dic["a"][dec_arrows(dec_life(i))][count] = -0.5                 #   shoot unsuccessfull-1
    dic["a"][dec_arrows(dec_life(dec_ene(i)))][count] = -0.5        #   shoot successfull-1
    dic["a"][i][count] = 1                                          #   anna

def dodge(dic,i,count):
    arr = mun(i)
    if arr[2] is 1:                                                 #   50 point dodge
        dic["a"][dec_life(inc_arrows(i))][count] = -0.8             #   pickup arrow
        dic["a"][dec_life(i)][count] = -0.2                         #   dont pickup arrow
        dic["a"][i][count] = 1                                      #   anna
    else:                                                           #   100 point dodge
        dic["a"][dec_life(inc_arrows(i))][count] = -0.64            #   50 point less, pickup arrow
        dic["a"][dec_life(i)][count] = -0.16                        #   50 point less, no pickup arrow
        dic["a"][dec_life(dec_life(inc_arrows(i)))][count] = -0.16  #   100 point less, pickup arrow
        dic["a"][dec_life(dec_life(i))][count] = -0.04              #   100 point less, no pickup arrow
        dic["a"][i][count] = 1                                      #   anna


def noop(dic,i,count):
    dic["a"][i][count] = 1                                          #   anna
    dic["r"][count] = 0                                             #   Making it 0  

def tellmemax(dic,i,count):
    if dic["x"][count] is max(dic["x"][count],dic["x"][count+1],dic["x"][count+2]):
        return count
    if dic["x"][count+1] is max(dic["x"][count],dic["x"][count+1],dic["x"][count+2]):
        return count+1
    if dic["x"][count+2] is max(dic["x"][count],dic["x"][count+1],dic["x"][count+2]):
        return count+2
#######################################################################################


#######################################################################################
################ Prepare a array ######################################################
#######################################################################################
dic = {}
dic["alpha"] = [0.000 for i in range(total)]
dic["alpha"][num(init_state_enemy,init_state_arr,init_state_stamina)] = 1.000
dic["r"] = [Y for i in range(100)]
dic["a"] = [[0 for i in range(100)] for j in range(60)]
count = 0

for i in range(total):
    elem = 0
    arr = mun(i)
    if arr[0] is 0:                                     #   Lol Enemy not alive
        elem = 1                                        #   noop
        noop(dic,i,count)
    elif arr[0] is not 0 :                              #   Enemy Alive Ra
        if arr[2] is 0:                                 #   0 Stamina, drink Patanjali to last in bed
            elem = 1                                    #   recharge
            recharge(dic,i,count)                       #   recharge done
        elif arr[2] is 1:                               #   50 Stamina, almost there   
            if arr[1] is 0:                             #   No Arrows
                elem = 2                                #   recharge,dodge
                dodge(dic,i,count)                      #   dodge done
                recharge(dic,i,count+1)                 #   recharge done
            elif arr[2] is not 0:                       #   Arrows
                elem = 3                                #   All actions are possible
                shoot(dic,i,count)                      #   shoot done
                dodge(dic,i,count+1)                    #   dodge done
                recharge(dic,i,count+2)                 #   recharge done
        else:                                           #   100 Stamina, will make everyone proud
            if arr[1] is 0:                             #   No Arrows
                elem = 1                                #   dodge
                recharge(dic,i,count)                   #   recharge done
            elif arr[2] is not 0:                       #   Arrows
                elem = 2                                #   shoot,dodge
                shoot(dic,i,count)                      #   shoot done
                dodge(dic,i,count+1)                    #   dodge done
    count = count + elem
#######################################################################################


'''
for i in range(60):
    for j in range(100):
        print(dic["A"][i][j],end="|")
    print()
'''

######################################################################################################
################ L.P Part ############################################################################
######################################################################################################
x = cp.Variable(shape=(100,1),name="x")
A = np.array(dic["a"])
r = np.array(dic["r"]).reshape(100,1).T
alpha = np.array(dic["alpha"]).reshape(60,1)
constraints = [cp.matmul(A,x) == alpha,x>=0 ]
objective = cp.Maximize(cp.matmul(r,x))
problem = cp.Problem(objective,constraints)
solution = problem.solve()
#print(x.value)
dic["x"] = x.value.tolist()
dic["objective"] = problem.value
######################################################################################################

######################################################################################################
################ Policy Part #########################################################################
######################################################################################################
count = 0
for i in range(total):
    elem = 0
    arr = mun(i)
    if arr[0] is 0:                                     #   Lol Enemy not alive
        elem = 1                                        #   noop
        policy.append([arr,"NOOP"])
    elif arr[0] is not 0 :                              #   Enemy Alive Ra
        if arr[2] is 0:                                 #   0 Stamina, drink Patanjali to last in bed
            elem = 1                                    #   recharge
            policy.append([arr,"RECHARGE"])
        elif arr[2] is 1:                               #   50 Stamina, almost there   
            if arr[1] is 0:                             #   No Arrows
                elem = 2                                #   recharge,dodge
                if dic["x"][count] <=dic["x"][count+1]: #   dont recharge
                    policy.append([arr,"DODGE"])
                else:
                    policy.append([arr,"DODGE"])
            elif arr[2] is not 0:                       #   Arrows
                elem = 3                                #   All actions are possible
                if tellmemax(dic,i,count) is (count):   #   shoot
                    policy.append([arr,"SHOOT"])
                elif tellmemax(dic,i,count) is (count+1):   #   dodge
                    policy.append([arr,"DODGE"])
                elif tellmemax(dic,i,count) is (count+2):   #   dodge
                    policy.append([arr,"RECHARGE"])
        else:                                           #   100 Stamina, will make everyone proud
            if arr[1] is 0:                             #   No Arrows
                elem = 1                                #   dodge
                policy.append([arr,"DODGE"])            #   Okna
            elif arr[2] is not 0:                       #   Arrows
                elem = 2                                #   shoot,dodge
                if dic["x"][count] >=dic["x"][count+1]: #   dont shoot
                    policy.append([arr,"SHOOT"])
                else:
                    policy.append([arr,"DODGE"])
    count = count + elem
######################################################################################################

if not os.path.exists(os.path.dirname(filename)):
    try:
        os.makedirs(os.path.dirname(filename))
    except OSError as exc: # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise

dic["policy"] = policy
## Changing to float
### A  first ####### 
for i in range(60):
    for j in range(100):
        dic["a"][i][j] = float("{:.4f}".format(dic["a"][i][j]))
### r next ########
for i in range(len(dic["r"])):
    dic["r"][i] =float("{:.4f}".format(dic["r"][i])) 
with open("./outputs/output.json","w") as fi:
        json.dump(dic,fi)

