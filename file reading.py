f = open("time.py")  # file name
c = f.read()  # read the whole file
c = f.readline()  # read the filr line by line
c = f.readlines()  # make the file as a list
print(c)
f.close()
f = open("rough.py")
c = f.read(3)  # read only 3 word of 1st line of the file
print(c)
f.close()
f = open("abc pattern.py")
c = f.read(56789)
print("1.", c)
c = f.read(56789)
print("2.", c)

f.close()
