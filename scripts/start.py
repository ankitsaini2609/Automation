import os,shutil,subprocess

path = os.getcwd()
dirs = os.listdir(path)
scripts = []
for item in dirs:
    if os.path.isdir(path+"/"+item):
        shutil.copyfile("/root/dataset/scripts/automate.sh",path+"/"+item+"/automate.sh")
        os.chdir(path+"/"+item)
        try:
            s = subprocess.check_output(["/bin/bash","-c","sh automate.sh"])
            final_path = path+'/'+item+'/resized/black_n_white/changed/'
            f = open(final_path+'script.py','r')
            content = f.read()
            f.close()
            #calculate no of folders
            nr_of_dirs = str(len(os.listdir(final_path))-1)
            print("#dirs in "+item+" : "+nr_of_dirs)
            f = open(final_path+'script.py','w')
            f.write(content.replace('$',nr_of_dirs))
            f.close()
            scripts.append(final_path)
        except Exception as e:
            print(e)
            break
        os.chdir(path)
for fPath in scripts:
    try:
    	os.chdir(fPath)
        s = subprocess.check_output(["/bin/bash","-c","python script.py"])
        print("Done : "+fPath)
    except Exception as e:
    	print(e)
    	break
