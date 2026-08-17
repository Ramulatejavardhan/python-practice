import csv
filepath="csvman.csv"
with open(filepath,"r") as file:
    cont=csv.reader(file)
    for i in cont:
        print(i)