import numpy as np
from client import get_errors, submit
from set_cur_state import set_current_state, get_current_state
import random

overfit_state = [-0.00016927573251173823, 0.0010953590656607808, 0.003731869524518327, 0.08922889556431182, 0.03587507175384199, -0.0015634754169704097,
                    -7.439827367266828e-05, 3.7168210026033343e-06, 1.555252501348866e-08, -2.2215895929103804e-09, 2.306783174308054e-11]



iter = 1000
for i in range(iter) :
    cur_state = get_current_state()
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
    print(errs)
    num_state = 0
    for j in range(2) :
        for k in range(j+1, 4):
            for x in range(11) :
                cross_prob = random.uniform(0, 1)
                mutation_prob = random.uniform(0, 1)
                mutated = random.uniform(-0.00000000001, 0.00000000001)
                if cross_prob < 0.8 :
                    new_state[num_state][x] = cur_state[errs[j][1]][x]
                else :
                    new_state[num_state][x] = cur_state[errs[k][1]][x]
                
                if mutation_prob < 0.3 :
                    new_state[num_state][x] = mutated
            num_state += 1
    # print("Old State", cur_state)
    # print("New state : ", new_state)
    set_current_state(new_state)
    
# print(err)
