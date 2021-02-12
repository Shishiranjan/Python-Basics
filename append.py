appendMe = ' how are u'
saveFile  = open('exampleFile.txt', 'a')
saveFile.write('\n')
# Here a is for appending the file
saveFile.write(appendMe)
saveFile.close()
