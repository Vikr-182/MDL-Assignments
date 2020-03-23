#======================================================================================#
# Test  #
#======================================================================================#
import numpy as np
from client import get_errors

state = np.zeros(11)
state[10] = 10**-14
err = get_errors('4wbRlSOEbHj0HmuzgNcnNc6KeW9ERzSsccXuswFyGlkn7bUMol',
                    list(state))
print()
print("State : ", state)
print("Error : ", err)
#======================================================================================#
