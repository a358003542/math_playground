print('hello world.\n')

import sys
print(sys.prefix)
# test library
from pywander.math import gen_prime
print(list(gen_prime(10)))
