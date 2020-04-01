import numpy as np
from client_moodle_anna import get_errors, submit
from set_cur_state import set_current_state, get_current_state, state_range
import random
import time

overfit_state = [-0.00016927573251173823, 0.0010953590656607808, 0.003731869524518327, 0.08922889556431182, 0.03587507175384199, -0.0015634754169704097,
                    -7.439827367266828e-05, 3.7168210026033343e-06, 1.555252501348866e-08, -2.2215895929103804e-09, 2.306783174308054e-11]



iter = 2
mut_state = [[0 for x in range(11)] for y in range(5)]
temp = None
for i in range(iter) :
    cur_state = get_current_state()
    # print("Old State ", cur_state)
    print()
    print()
    print(cur_state)
    print()
    print()
    new_state = [[0 for x in range(11)] for y in range(5)]
    count = 0
    errs = []
    print("Iter:" + str(i))
    for state in cur_state :
        # err = get_errors('4wbRlSOEbHj0HmuzgNcnNc6KeW9ERzSsccXuswFyGlkn7bUMol',list(state))
        err = 0
        print(state,end="?")
        print()
        errs.append([err, count])
        count += 1
    print()
    errs.sort()
    num_state = 0
    for j in range(2) :
        for k in range(j+1, 4):
            if j == 0:
                cross_keep_prob = 0.65
                mutation_keep_prob = 0.2
            else :
                cross_keep_prob = 0.5
                mutation_keep_prob = 0.2
            for x in range(11) :
                cross_prob = random.uniform(0, 1)
                mutation_prob = random.uniform(0, 1)
                current = cur_state[errs[0][1]][x]
                
                if current > 0 :
                    mutated = random.uniform(max(-1, current*-0.1), min(1, current*1.25))
                else :
                    mutated = random.uniform(max(-1, current*1.25), min(1, current*-0.1))
                    
                if cross_prob < cross_keep_prob :
                    new_state[num_state][x] = cur_state[errs[j][1]][x]
                else :
                    new_state[num_state][x] = cur_state[errs[k][1]][x]
                
                if mutation_prob < mutation_keep_prob :
                    new_state[num_state][x] = mutated
                    
            num_state += 1
    for x in range(11):
        new_state[2][x] = cur_state[errs[0][1]][x]
    for x in range(11) :
        mutated_keep_prob = 0.3
        current = cur_state[errs[0][1]][x]
        if current > 0 :
            mutated = random.uniform(max(-1, current*-0.1), min(1, current*1.25))
        else :
            mutated = random.uniform(max(-1, current*1.25), min(1, current*-0.1))
        if mutated <= -1 or mutated >= 1 :
            mutated = random.uniform(-10**-state_range[x], 10**-state_range[x])
            
        sample = random.uniform(0, 1)
        if sample < mutated_keep_prob :
            new_state[4][x] = mutated
        else :
            new_state[4][x] = cur_state[errs[0][1]][x]
            
    # print("Old State ", cur_state)
    # print("New state : ", new_state)
    set_current_state(new_state)
    temp = new_state
    time.sleep(0.1)
    # x = input()

# print(temp[2])

# print(err)
