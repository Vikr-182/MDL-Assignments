import numpy as np
from client import get_errors, submit


init_state = np.random.uniform(low = -1, high=1, size=(11,))
err = get_errors('4wbRlSOEbHj0HmuzgNcnNc6KeW9ERzSsccXuswFyGlkn7bUMol', list(np.zeros(11)))
print(err)
