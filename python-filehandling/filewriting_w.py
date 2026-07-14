txt="hello created this file with filewriting"
file="example.txt"
with open(file,"w") as file:#"w" mode is used to create 
    file.write(txt)
    print("added the text to example.txt")