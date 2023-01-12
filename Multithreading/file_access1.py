import os
dir=os.getcwd()
file=os.listdir(dir)
files=[f for  f in file if os.path.isfile(dir+'/'+f)]
print(files)
'''fpython=[ f for f in file if f.endswith(".py)]
print(python)'''