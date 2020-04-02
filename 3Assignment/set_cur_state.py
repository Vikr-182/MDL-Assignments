#======================================================================================#
# Function to set and get the current state #
#======================================================================================#
import pickle
import numpy as np
import random
state = [list(np.zeros(11)) for x in range(5)]
dim_state = 5
state_range = [-1, -1, 1, 2, 4, 5, 6, 8, 10, 11, 13]
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
    overfit_state = [0.0, 0.1240317450077846, -6.211941063144333, 0.04933903144709126, 0.03810848157715883, 8.132366097133624e-05, -6.018769160916912e-05, -1.251585565299179e-07, 3.484096383229681e-08, 4.1614924993407104e-11, -6.732420176902565e-12]
    initial_state = np.random.uniform(low = -1, high = 1, size =(5, 11))
    for y in range(5):
        # initial_state[y][0] = random.uniform(-1, 1)
        for x in range(1,11) :
            initial_state[y][x] = random.uniform(-10**-state_range[x], 10**-state_range[x])
            # current = overfit_state[x]
            # if current > 0 :
            #     mutated = random.uniform(max(-1, current*0.01), min(1, current*1.2))
            # else :
            #     mutated = random.uniform(max(-1, current*1.2), min(1, current*0.01))
            # initial_state[y][x] = mutated
    # initial_state[4] = overfit_state
    set_current_state(initial_state)
    return
array = get_current_state()
# for x in array :
#     print(x)
# set_initial_state()
#======================================================================================#
