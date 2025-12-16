import os
import random
import shutil


def check(dir1, dir2):
    textfile = [f for f in os.listdir(dir1) if f.endswith('.txt')]
    text = [os.path.splitext(file)[0] for file in textfile]
    imgsfile = [f for f in os.listdir(dir2) if f.endswith('.jpg')]
    img = [os.path.splitext(file)[0] for file in imgsfile]

    for i in img:
        if i not in text:
            os.remove(os.path.join(dir2, i+'.jpg'))

dir2 = './train/images'
dir1 = './train/labels'
check(dir1, dir2)
