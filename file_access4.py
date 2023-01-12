import os
def find_files(filename,path):
    for root,dirs,files in os.walk(path):
        for name in files:
            if name==filename:
                print("exist")
                break
            else:
                print("not exist")
name=input()
dir="c://HCL"
find_files(name,dir)