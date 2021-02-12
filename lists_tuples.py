#Lists and tuples
# Tuple are immutable i.e. it cannot be changed further
'''
def example():
    return 14, 16

a, b = example()

print(a)
print(b)
'''

Ccranjan = [6, 5, 9, 1, 7, 13, 15, 17]

print(Ccranjan)
print(Ccranjan[5])

Ccranjan.append(16)
print(Ccranjan)

Ccranjan.insert(4,23)
print(Ccranjan)

Ccranjan.remove(9)
print(Ccranjan)

print(Ccranjan.index(5))
print(Ccranjan.count(1))

Ccranjan.sort()
print(Ccranjan)

Ccranjan.reverse()
print(Ccranjan)
