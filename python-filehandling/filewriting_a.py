txt="hello"
file="examplea.txt"
a=0
with open(file,"a") as file:#we can print what we as many times as we like and new file creates not exist.
    file.write(txt+"\n")
    print("done")