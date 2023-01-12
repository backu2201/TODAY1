import os
import task2 as ta
def search_file(n,t):
    for i in t:
        for r,d,f in os.walk(i):
            for j in f:
                if j==n:
                    print("file found")
                    print(r)
                    break
    else:
        print("not found")
n=input("enter")
t=ta.GetDrives()
search_file(n,t)



