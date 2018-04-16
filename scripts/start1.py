import os,shutil,subprocess

path = os.getcwd()
dirs = os.listdir(path)

for item in dirs:
    if os.path.isdir(path+"/"+item):
        shutil.copyfile("/root/dataset/scripts/automate.sh",path+"/"+item+"/automate.sh")
        os.chdir(path+"/"+item)
        try:
            s = subprocess.check_output(["/bin/bash","-c","sh automate.sh"])
        except:
            print("Problem in subprocess")
        os.chdir(path)
