import os
#               |_relative path_|
# file_path="examp.txt"
# if os.path.exists(file_path):
#     print("file exists")
# else:
#     print("not found")


file="name/text.txt"
if os.path.exists(file):
    print("exists")

files="C:/Users/user/Desktop/tests"
if os.path.exists(files):
    print("absoulte file found")