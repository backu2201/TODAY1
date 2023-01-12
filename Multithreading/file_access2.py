import os,fnmatch
def find(filename, path):
    result = []
    for root,dirs, files in os.walk(path):
        for name in files:
            if name==filename:
                print("File exist")
                break
            else:
                print("Not exist")
name=input("Enter the file name")
dir="C://"
find(name,dir)