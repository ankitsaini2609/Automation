from PIL import Image
import os

path = os.getcwd()
dirs = os.listdir(path)
os.makedirs("black_n_white")
for item in dirs:
    if '.py' in item:
        continue
    if os.path.isfile(path+'/'+item):
        image_file = Image.open(path+'/'+item)
        image_file = image_file.convert('1')
        image_file.save(path+'/black_n_white/to_invert' + item)
