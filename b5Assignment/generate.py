from varname import varname
import sys
discount = [0.5]
values = ["reward"]
xlim = 3
ylim = 3
xr = xlim*xlim
yr = ylim*ylim
c = 2
rew = 1 - ((int(sys.argv[1]) + 1) % 40)/100
states = [xr * yr * c]
actions = ["up","right","down","left","stay"]
call_actions = [0,1]
agent_init = [1,1]
target_init = []

observations = [("o" + str(i)) for i in range(7)]
order = ["discount:","values:","states:","actions:","observations:","start include:"]
start = []
target_un = [[0,0],[2,0],[0,2],[2,2]]
agent_un = [[1,1]]
call_un = [0,1]
x = 1 - rew
jaag = int(sys.argv[1])%100 + 10
sexy = 0


def function():
    return varname()

def num_agent(agent_pos):
    return ylim*agent_pos[0] + agent_pos[1]

def num_target(target_pos):
    return ylim*target_pos[0] + target_pos[1]

def get_state(num):
    return [num//3,num%3]

def overall_get_state(num):
    return [ get_state(num//18),get_state((num%18)//2),num%2]

def space(arr):
    s = ""
    for i in range(len(arr)-1):
        s += str(arr[i])
        s += " "
    s += str(arr[len(arr)-1])
    return s

def get_overall_num(agent_pos,target_pos,call):
    return num_agent(agent_pos)*xlim*ylim*c + num_target(target_pos)*c + call;

## prepare initial belief state
def init():
    for i in range(len(agent_un)):
        for j in range(len(target_un)):
            for k in range(len(call_un)):
                start.append(get_overall_num((agent_un[i]),(target_un[j]),call_un[k]))

def right(x,y,key):
    key = -1 * (not key) + 1 * key
    if x == xlim - 1:
        if key is 1:
            key = 0
    elif x == 0 and key is -1:
        key = 0
    return [x + key*1,y]

def left(x,y,key):
    key = -1 * (not key) + 1 * key
    if x == 0:
        if key is 1:
            key = 0
    elif x == xlim - 1 and key is -1:
        key = 0
    return [x-key*1,y]

def cn(c,key):
    return c^key;

def up(x,y,key):
    key = -1 * (not key) + 1 * key
    if y == ylim - 1:
        if key is 1:
            key = 0
    elif y == 0 and key is -1:
        key = 0
    return [x,y + key*1]

def down(x,y,key):
    key = -1 * (not key) + 1 * key
    if y == 0:
        if key is 1:
            key = 0
    elif y == ylim - 1 and key is -1:
        key = 0
    return [x,y - key*1]

def stay(x,y,key):
    return [x,y]

def take_action(x,y,action,key):
    return globals()[action](x,y,key)


print(get_overall_num([2,0],[0,2],0))
print(num_agent([0,2]))
call_trans = [0.4,0.6]
another = [0.2,0.8]
## prepare transition matrix
def init_matrix():
    sexy = 0
    ra=2
    for p in range(len(actions)):
        globals()["matrix_" + actions[p]] = [[0 for i in range(162)] for j in range(162)]
    for i in range(states[0]):
        for ag_ac in range(len(actions)):# Agent take action
            for tar_ac in range(len(actions)):# Target take action
                for cal_ac in range(len(call_actions) - 1):# Call action
                    for ag_un in range((2)):# Agent may or may not acheive the desired outcome
                        for call_un in range((2)):# Call may or may not acheive the desired outcome
                            if actions[ag_ac] == "stay" and ag_un == 0:# if stay action and not desired condition
                                continue
                            agent_state = overall_get_state(i)[0]
                            target_state = overall_get_state(i)[1]
                            call_state = overall_get_state(i)[2]
                            agent_prob = x*(1 - ag_un) +  (1 - x)*(ag_un)
                            target_prob = 0.15
                            call_prob = 0.4*(call_state ^ 1)*( call_un) + 0.6*(call_state ^ 1)*(1  - call_un) + 0.2 * (call_state ^ 0) * (call_un) + 0.8 * (call_state ^ 0) * ( 1 - call_un)
                            if actions[ag_ac] == "stay":
                                agent_prob = 1
                            if actions[tar_ac] == "stay":
                                target_prob = 0.4
                            #try:
                            j = get_overall_num(take_action(agent_state[0],agent_state[1],actions[ag_ac],ag_un),take_action(target_state[0],target_state[1],actions[tar_ac],1) ,cn(call_state,call_un))
                            af = overall_get_state(j)[0]
                            tf = overall_get_state(j)[1]
                            if agent_state == target_state and call_state == 1: #agent and target are in same place and call is on
                                call_state = 0
                                call_prob = 0.4*( 1)*(call_un) + 0.6*( 1)*(1  - call_un)

                            prob = agent_prob * target_prob * call_prob
                            try:
                                j = get_overall_num(take_action(agent_state[0],agent_state[1],actions[ag_ac],ag_un),take_action(target_state[0],target_state[1],actions[tar_ac],1) ,cn(call_state,call_un))
                                globals()["matrix_" + actions[ag_ac]][i][j] += prob
                            except:
                                print("J = " + str(j) + str((agent_state[0],agent_state[1],actions[ag_ac],ag_un)) + str(take_action(agent_state[0],agent_state[1],actions[ag_ac],ag_un)) + "action" + actions[ag_ac] + "y" + str(ag_un)) 
                            if i is 1 and actions[ag_ac] == "stay" :
                                print("RARARARARA")
                                print( "J = " + str(j) + "\tag = " + str(agent_state) + "|" + "tar = " + str(target_state) + "cal" + str(call_state) + "|" + "agent_ac = " + str(actions[ag_ac]) + "|" + "target_ac = " + str(actions[tar_ac]) + "|\t"
                                        + "agent_un = " + str(ag_un) + "| " + "call_nu - " + str(call_un)  + "|\t" + "agent_prob = " + str(agent_prob) + "|target_rpob = " + str(target_prob) + "|" 
                                        + "call_prob = " + str(call_prob) + "\t" + str(overall_get_state(j)) + "okna " + str(take_action(agent_state[0],agent_state[1],actions[ag_ac],ag_un)) +"\n" +  str(take_action(target_state[0],target_state[1],actions[tar_ac],1)) + str("call ") + str(cn(call_state,call_un))
                                        )
                                print("oh lala" + str(prob))
                                sexy += prob
    print(sexy)

init()
init_matrix()
T="2"

f = open(sys.argv[1] + ".pomdp","w")

for i in range(len(order)):
    f.write(order[i] + " " + space( globals()[order[i].split(" ")[0].split(":")[0]]) )
    f.write("\n")

def add_t():
    for j in range(len(actions)):
        f.write("T: " + str(actions[j]) + "\n")
        matrix = globals()["matrix_" + actions[j]]
        for k in range(len(matrix)):
            for m in range(len(matrix[k])):
                '''
                if k is m:
                    f.write(str(1))
                else:
                    f.write(str(0))
                '''
                f.write(str(matrix[k][m]))
                f.write(" ")
            f.write("\n")
        f.write("\n")
    f.write("\n")

'''
● o1 is observed when the target is in the same cell as the agent.
● o2 is observed when the target is in the cell to the right of the agent's cell.
● o3 is observed when the target is in the cell below agent's cell
● o4 is observed when the target is in the cell to the left of agent's cell
● o5 is observed when the target is in the cell above the agent's cell.
● o6 is observed when the target is not in the 1 cell neighbourhood of the
agent.
'''
add_t()
def add_r():
    for j in range(states[0]):
        af = overall_get_state(j)[0]
        tf = overall_get_state(j)[1]
        call = overall_get_state(j)[2]
        if af == tf and call == 1:
            f.write("R: " + "stay" + " :  * " + " : " + str(j) + " : * " + str(jaag) + "\n")
        else:
            f.write("R: " + "stay" + " :  * " + " : " + str(j) + " : * " + str(0) + "\n")
        for p in range(len(actions)):
            if(actions[p] != "stay"):
                if af == tf and call == 1:
                    f.write("R: " + actions[p] + " : * " + " : " + str(j) + " : * " + str(jaag-1) + "\n")
                else:
                    f.write("R: " + actions[p] + " : * " + " : " + str(j) + " : * " + str(-1) + "\n")

def prepare_anna(g):
    g -= 1
    sp = "\n"
    for i in range(7):
        if i == g:
            sp += " 1.0 "
        else:
            sp += " 0.0"
    return sp + "\n"

def add_o():
    for i in range(states[0]):
        ai = overall_get_state(i)[0]
        ti = overall_get_state(i)[1]
        if ai == ti:
            f.write("O: * :"+ str(i) +  prepare_anna(1))# + str(jaag) + "\n")
        elif left(ai[0],ai[1],1)  == ti:
            # target to left of agent
            f.write("O: * :"+ str(i) + prepare_anna(4))#": o4 1\n")# + str(jaag) + "\n")
        elif right(ai[0],ai[1],1)  == ti:
            # target to right of agent
            f.write("O: * :"+ str(i) + prepare_anna(2))#": o2 1\n")# + str(jaag) + "\n")
        elif up(ai[0],ai[1],1)  == ti:
            # target to up of agent
            f.write("O: * :"+ str(i) + prepare_anna(5))#": o5 1\n")# + str(jaag) + "\n")
        elif down(ai[0],ai[1],1)  == ti:
            # target to down of agent
            f.write("O: * :"+ str(i) + prepare_anna(3))#": o3 1\n")# + str(jaag) + "\n")
        else:
            # target not around of agent
            f.write("O: * :"+ str(i) + prepare_anna(6))#": o6 1\n")# + str(jaag) + "\n")



'''
add_t()
add_r()
add_o()
f.close()
vart = [1,3]
rt = [1,3]
for i in range(len(matrix_up)):
    s = 0
    for j in range(len(matrix_up[i])):
        s += matrix_up[i][j]
    #print(i,s)
'''
add_r()
add_o()
#f.write("O: * : * : *  o1")
