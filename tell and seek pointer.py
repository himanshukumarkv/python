f = open("rough3.py", "w")
f.write("aman is a good boy\n")
f.write("he is working in a company")
f.close()
f = open("rough3.py")
print(f.tell())  # This tells you where the line starts.
print(f.readline())
print(f.tell())
f.close()
f = open("rough3.py")
f.seek(3)  # this tells you where you want to start the line
print(f.readline())
f.close()
