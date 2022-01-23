from encodings import utf_8

file = open('simple.txt', 'w')
file.write('Test string for writing to file')
file.close()

file = open('simple.txt', 'r')
a = file.read()
print(a)

