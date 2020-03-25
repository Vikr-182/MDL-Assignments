#======================================================================================#
# File to store weights and errors. #
# Picle file format [[[weight1, error1], [[weight2], [error2]]...]
#======================================================================================#

import pickle
from set_cur_state import get_current_state

AppendList = []
weights = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
errors = [4297934.878906351, 11920515.787599135]


def store_weights(weights, errors):
    AppendList = []
    AppendList.append(weights)
    AppendList.append(errors)
    
    if len(weights) != 11 :
        print("Weights dimension not right!")
        return
    elif len(errors) != 2 :
        print("Error dimension not right!")
        return
    pickle_in = open("weights_errors.pkl","rb")
    array = pickle.load(pickle_in)
    array.append(AppendList)
    print(array)
    with open('weights_errors.pkl', 'wb') as f:
        pickle.dump(array, f)
    
    print(array, " is added successfully!")

# errors = [216122.32772690017, 345245.9944283677]
# weights = get_current_state()[2]
# array = []
# array.append([weights, errors])
# with open('weights_errors.pkl', 'wb') as f:
#     pickle.dump(array, f)
# store_weights(weights, errors)

#======================================================================================#
