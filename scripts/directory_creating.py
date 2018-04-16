import os

path = os.getcwd()
dirs = os.listdir(path)

l = len(dirs)
i = 1
for item in dirs:
    if item == "directory_creating.py":
        continue
    elif os.path.isfile(path+'/'+item):
        os.makedirs("set" + str(i))
        os.rename(path+"/"+item, path+"/set"+str(i)+"/1.png")
        i+=1
