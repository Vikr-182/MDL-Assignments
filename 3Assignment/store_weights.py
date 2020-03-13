#======================================================================================#
# File to store weights and errors. #
# Picle file format [[[weight1, error1], [[weight2], [error2]]...]
#======================================================================================#

import pickle
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
    
    with open('weights_errors.pkl', 'wb') as f:
        pickle.dump(array, f)
    
    print(array, " is added successfully!")
    
#======================================================================================#
