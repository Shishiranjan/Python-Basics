#Lecture: Input and statistics
'''
name = input('What is your name?: ')
print('Hello', name)
'''


# Statistics
# From python 3.4 onwards u will be able to calculate the standard deviation, mean, mode, median etc.

import statistics

ccRanjan = [7, 4, 9, 1, 5, 2, 8, 6, 3]

Pankaj = statistics.mean(ccRanjan)
print(Pankaj)

Pankaj = statistics.median(ccRanjan)
print(Pankaj)

Pankaj = statistics.variance(ccRanjan)
print(Pankaj)

Pankaj = statistics.stdev(ccRanjan)
print(Pankaj)













