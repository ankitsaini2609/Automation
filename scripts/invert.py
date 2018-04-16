from PIL import Image
import numpy as np
import PIL.ImageOps, os

path = os.getcwd()
dirs = os.listdir(path)
os.makedirs(path+"/changed")
for item in dirs:
    if '.py' in item:
        continue
    if os.path.isfile(path+'/'+item):
        img = Image.open(path+'/'+item)
        img = img.convert("L")
        imgData = np.asarray(img)
        im = PIL.ImageOps.invert(img)
        im.save(path+"/changed/changed"+item)
        im.close()
        
