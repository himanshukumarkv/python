f = open("rough.py", "w")  # it will delete the particular content of the file and rewrite content
f.write("once upon a time ")
f = open("rough2.py", "a")  # it will simply add the content to a particular file
a = f.write("once upon a time ")  # it will give
print(a)  # length of sentence
f.close()
f = open("rough.py", "r+")  # it means you can read or write in same file
a = f.read()
print(a)
f.write("there was a king")
f.close()
