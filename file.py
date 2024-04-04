f = open("Demo.txt", "w")  # Open "Demo.txt" in write mode, creates/overwrites the file
f.write("welcome to python class\n")
f.write("hello world\n")
f = open("Demo.txt", "r")# Reopen "Demo.txt" in read mode
data = f.read()
print(data)
print(type(data))
f.close()
f = open("Demo.txt", "r")
data = f.readlines()
print(data)  # Read and print the file's content
for l in data:
    a=input("enter the word")
    if a in l:
        print("yes")
        break
    else:
        print("not")
        continue

