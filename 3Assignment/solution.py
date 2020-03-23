import numpy as np
from client import get_errors, submit
from set_cur_state import set_current_state, get_current_state, state_range
import random
import time

overfit_state = [-0.00016927573251173823, 0.0010953590656607808, 0.003731869524518327, 0.08922889556431182, 0.03587507175384199, -0.0015634754169704097,
                    -7.439827367266828e-05, 3.7168210026033343e-06, 1.555252501348866e-08, -2.2215895929103804e-09, 2.306783174308054e-11]



iter = 70
mut_state = [[0 for x in range(11)] for y in range(5)]
for i in range(iter) :
    cur_state = get_current_state()
    # print("Old State ", cur_state)
    # print(cur_state)
    new_state = [[0 for x in range(11)] for y in range(5)]
    count = 0
    errs = []
    for state in cur_state :
        err = get_errors('4wbRlSOEbHj0HmuzgNcnNc6KeW9ERzSsccXuswFyGlkn7bUMol',
                            list(state))
        errs.append([err, count])
        count += 1
    errs.sort()
    # print(errs)
    # Crossover 0-1, 0-2, 0-3, 1-2, 1-3
    print()
    print("Iter : ", i)
    print(errs)
    num_state = 0
    for j in range(2) :
        for k in range(j+1, 4):
            cross_keep_prob = 0.6
            mutation_keep_prob = 0.4
            for x in range(11) :
                cross_prob = random.uniform(0, 1)
                mutation_prob = random.uniform(0, 1)
                current = cur_state[errs[0][1]][x]
                
                mutated = random.uniform(max(-1, current*0.5), min(1, current*1.5))
                if mutated >= 1 or mutated <= -1 :
                    mutated = random.uniform(-10**-state_range[x], 10**-state_range[x])
                    
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
        mutated_keep_prob = 0.6
        current = cur_state[errs[0][1]][x]
        mutated = random.uniform(max(-1, current*0.5), min(1, current*1.5))
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
    time.sleep(0.1)
    # x = input()


# print(err)
