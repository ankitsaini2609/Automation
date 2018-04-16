import os,PIL,sys
from PIL import Image

path = os.getcwd()
dirs = os.listdir(path)
os.makedirs(path+"/resized")
#print(dirs)
def resize():
    #print("inside resize")
    for item in dirs:
        #print(path+'/'+item)
        if ".py" in item or ".sh" in item:
            continue
        if os.path.isfile(path+'/' + item):
            #print('inside isfile function')
            im = Image.open(path+'/'+item)
            #print(im)
            f,e = os.path.splitext(path+'/'+item)
            width,height = im.size
            #print("getting size: "+ str(width) + " " + str(height))
            if width >= 50 and height >= 50:
                imResize = im.resize((50,50), Image.ANTIALIAS)
		print(f)
                imResize.save(path+"/resized/"+item+ ' resized.png','PNG',quality=90)

resize()

