filepath="examp.txt"
with open(filepath,"r")as file:
    content=file.read()
    print(f"The content present in the file is:{content}")