'''
from statistics import mean, stdev

Nikhil = [14, 17, 9, 6, 5, 21, 18, 33, 12]

print(mean(Nikhil))
print(stdev(Nikhil))

It is the one way of importing only something from statistics.



# Another way of importing only something from statistics is given below.

from statistics import mean as m, stdev as s

Nikhil = [14, 17, 9, 6, 5, 21, 18, 33, 12]

print(m(Nikhil))
print(s(Nikhil))

'''

# Another way of importing all from statistics


from statistics import *

Nikhil = [14, 17, 9, 6, 5, 21, 18, 33, 12]

print(mean(Nikhil))
print(stdev(Nikhil))







