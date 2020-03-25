#======================================================================================#
# Function to set and get the current state #
#======================================================================================#
import pickle
import numpy as np
import random
state = [list(np.zeros(11)) for x in range(5)]
dim_state = 5
state_range = [0, 0, 1, 1, 3, 5, 7, 8, 11, 11, 14]
mutation_range = [0.5, 0.5, 1, 2, 2, 2, 2, 2, 2, 2, 2 ]
def set_current_state(state):
    if len(state) != dim_state :
        print("Dimensions of state not right")
        return
    else :
        for i in range(dim_state):
            if len(state[i]) != 11:
                print("Inner Dimension not right at pos ", i)
                return
    with open('current_state.pkl', 'wb') as f:
        pickle.dump(state, f)
def get_current_state() :
    with open('current_state.pkl', 'rb') as f:
        array = pickle.load(f)
    return array
    
def set_initial_state() :
    overfit_state = [-0.00016927573251173823, 0.0010953590656607808, 0.003731869524518327, 0.08922889556431182, 0.03587507175384199, -0.0015634754169704097,
                        -7.439827367266828e-05, 3.7168210026033343e-06, 1.555252501348866e-08, -2.2215895929103804e-09, 2.306783174308054e-11]
    initial_state = np.random.uniform(low = -1, high = 1, size =(5, 11))
    for y in range(5):
        for x in range(11) :
            initial_state[y][x] = random.uniform(-10**-state_range[x], 10**-state_range[x])
    set_current_state(initial_state)
    return
# array = get_current_state()
# for x in array :
#     print(x)
set_initial_state()
#======================================================================================#
