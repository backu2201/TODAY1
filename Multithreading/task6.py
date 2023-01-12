import os
d="C://hcl"
di={}
for root,dir,files in os.walk(d):
    for d in dir:
        di[d]=os.listdir(root+"/"+d)
print(di)