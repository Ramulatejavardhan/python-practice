txt="hello created this file with filewritings"
file="examples.txt"
with open(file,"w") as file:#"w" mode is used to create a file and write the data on file.
    file.write(txt)
    print("added the text to examp.txt")