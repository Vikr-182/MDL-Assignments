import numpy as np
from client import get_errors, submit
from set_cur_state import set_current_state, get_current_state, state_range
import random
import time

overfit_state = [-0.00016927573251173823, 0.0010953590656607808, 0.003731869524518327, 0.08922889556431182, 0.03587507175384199, -0.0015634754169704097,
                    -7.439827367266828e-05, 3.7168210026033343e-06, 1.555252501348866e-08, -2.2215895929103804e-09, 2.306783174308054e-11]



iter = 40
mut_state = [[0 for x in range(11)] for y in range(5)]
temp_err = [[[1000000000000000000, 1000000000000000000], 0] for x in range(5)]
temp_state = None
for i in range(iter) :
    cur_state = get_current_state()
    # print("Old State ", cur_state)
    print("Generation : ", i+1)
    print("\nCurrent Vectors : ")
    for x in cur_state :
        print("Vector  :", x)
    
    new_state = [[0 for x in range(11)] for y in range(5)]
    count = 0
    errs = []
    

    for state in cur_state :
        err = get_errors('4wbRlSOEbHj0HmuzgNcnNc6KeW9ERzSsccXuswFyGlkn7bUMol',
                            list(state))
        errs.append([err, count])
        count += 1
    for err in errs:
    #     train_err.append(err[0][0])
        tmp = err[0][1]
        err[0][0] = (err[0][0])
        err[0][1] = tmp
    # Comparision between cur_state and temp_states
    # if temp_err != None:
    #     for x in range(0, 2) :
    #         if errs[x][0][0] > temp_err[x+1][0][0] :
    #             # print("Err : ", temp_err[x+1][0][0])
    #             cur_state[x] = temp_state[temp_err[x+1][1]]
    #             errs[x][0] = temp_err[x+1][0]
    #
    #     if errs[4][0][0] > temp_err[3][0][0] :
    #         cur_state[4] = temp_state[temp_err[3][1]]
    #         errs[4][0] = temp_err[3][0]
    #     elif errs[4][0][0] > temp_err[4][0][0] :
    #         cur_state[4] = temp_state[temp_err[4][1]]
    #         errs[4][0] = temp_err[4][0]
    
    # Comparision ends here !
        
    
    # train_err =[]
    # train_err.sort()

    errs.sort()
    

    
    # print(errs)
    # Crossover 0-1, 0-2, 0, 1-2, 0 with mutations
    # print()
    # print("Iter : ", i)
    # print(train_err)
    print("\n\nErrors : \n", errs)
    print()
    num_state = 0
    for j in range(2) :
        for k in range(j+1, 4):
            if j == 0:
                cross_keep_prob = 0.8
                mutation_keep_prob = 0.2
            else :
                cross_keep_prob = 0.6
                mutation_keep_prob = 0.2
            for x in range(11) :
                cross_prob = random.uniform(0, 1)
                mutation_prob = random.uniform(0, 1)
                
                    
                if cross_prob < cross_keep_prob :
                    new_state[num_state][x] = cur_state[errs[j][1]][x]
                else :
                    new_state[num_state][x] = cur_state[errs[k][1]][x]
                current = new_state[num_state][x]
                
                if current > 0 :
                    mutated = random.uniform(max(-1, current*0.95), min(1, current*1.05))
                    # mutated = random.uniform(-10**-state_range[x], 10**-state_range[x])
                else :
                    mutated = random.uniform(max(-1, current*1.05), min(1, current*0.95))
                    # mutated = random.uniform(-10**-state_range[x], 10**-state_range[x])
                if mutation_prob < mutation_keep_prob :
                    new_state[num_state][x] = mutated
                    
            num_state += 1
    for x in range(11):
        new_state[2][x] = cur_state[errs[0][1]][x]
    for x in range(11) :
        mutated_keep_prob = 0.1
        current = cur_state[errs[0][1]][x]
        if current > 0 :
            mutated = random.uniform(max(-1, current*0.95), min(1, current*1.05))
            # mutated = random.uniform(-10**-state_range[x], 10**-state_range[x])
        else :
            mutated = random.uniform(max(-1, current*1.05), min(1, current*0.95))
            # mutated = random.uniform(-10**-state_range[x], 10**-state_range[x])
        if mutated <= -10 or mutated >= 10 :
            mutated = random.uniform(-10**-state_range[x], 10**-state_range[x])
            
        sample = random.uniform(0, 1)
        if sample < mutated_keep_prob :
            new_state[4][x] = mutated
        else :
            new_state[4][x] = cur_state[errs[0][1]][x]
    
    if iter %10 == 0 :
        min_err = 1000000000000000000
        pos = 0
        for x in range(4) :
            if errs[x][0][1] < min_err :
                min_err = errs[x][0][1]
                pos = x
        # print(new_state[errs[pos][1]])
        submit('4wbRlSOEbHj0HmuzgNcnNc6KeW9ERzSsccXuswFyGlkn7bUMol', new_state[2])
    
        
        
        
    set_current_state(new_state)
    temp_err = errs
    temp_state = cur_state
    time.sleep(0.1)
    # x = input()
min_err = 1000000000000000000
pos = 0
for x in range(4) :
    if errs[x][0][1] < min_err :
        min_err = errs[x][0][1]
        pos = x
print(new_state[errs[pos][1]])
submit('4wbRlSOEbHj0HmuzgNcnNc6KeW9ERzSsccXuswFyGlkn7bUMol', new_state[2])
# print(err)
