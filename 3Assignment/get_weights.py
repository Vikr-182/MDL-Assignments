#======================================================================================#
# get_weights function to get all the weights and errors. #
#======================================================================================#
import pickle

def get_weights():
    pickle_in = open("weights_errors.pkl","rb")
    array = pickle.load(pickle_in)
    # print(array)
    return array
array = get_weights()
# print(array)
for i in array:
    for j in i:
        for k in j:
            print(k,end="|")
            print()
        print()
        print()
    print()
    print()
    print()
#======================================================================================#
