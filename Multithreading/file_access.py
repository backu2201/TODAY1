import os
print(os.getcwd())
for root,dir,file in os.walk("c:/HCL"):
    print(root,dir,file)