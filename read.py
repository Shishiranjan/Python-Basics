readMe = open('exampleFile.txt', 'r').read()
print(readMe)

readMe2 = open('exampleFile.txt', 'r').readlines()
print(readMe2)

splitMe = readMe.split('\n')
print(splitMe)
