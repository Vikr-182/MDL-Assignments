#======================================================================================#
# Function to set the current state #
#======================================================================================#
import pickle
import numpy as np
# state = [list(np.zeros(11)) for x in range(5)]
dim_state = 5

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

# set_current_state(state)
#======================================================================================#
