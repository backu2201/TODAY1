import task2 as ta
import os
def search_file(n,t):
    k=[]
    for i in t:
        for r,d,f in os.walk(i):
            for j in f:
                if j==n:
                    print("file found in {}".format(i))
                    k.append(i)
                    print()
                    break
    for i in range(len(t)):
        if t[i] not in k:
            print("not found in {}".format(t[i]))
n=input("enter")
t=ta.GetDrives()
search_file(n,t)
