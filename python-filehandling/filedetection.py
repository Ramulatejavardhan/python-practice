import os
file_path="examp.txt"
if os.path.exists(file_path):
    print("file exists")
else:
    print("not found")