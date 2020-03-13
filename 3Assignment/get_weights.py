#======================================================================================#
# get_weights function to get all the weights and errors. #
#======================================================================================#
import pickle

def get_weights():
    pickle_in = open("weights_errors.pkl","rb")
    array = pickle.load(pickle_in)
    print(array)
    return array
    
#======================================================================================#
