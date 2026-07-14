txt="hello"
file="example.txt"
try:
    with open(file,"x") as file:#we can create a new file with "x"
        file.write(txt)
        print("file created")
except FileExistsError:
    file="example1.txt"
    with open(file,"x") as file:
        file.write(txt)
        print("1st file already exists another file created")