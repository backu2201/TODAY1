import task2 as ta
import os
def search_file(n,t):
    #f=[]
    for i in t:
        for r,d,f in os.walk(i):
            for j in f:
                 #f.append(j)
                 if j==n:
                    print("file found")
                    break
    else:
        print("not found")
n=input("enter")
t=ta.GetDrives()
search_file(n,t)
''