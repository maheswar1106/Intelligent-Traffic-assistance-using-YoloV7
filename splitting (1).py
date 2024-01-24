import numpy as np
import cv2 as cv
import splitfolders
import os
from random import shuffle
from glob import glob


def splitting_images(path,output_dir,t_rat):
        path=path
        for fle in files[:t_rat]:
            src_fname, ext = os.path.splitext(fle)
            im=cv.imread(src_fname+".jpg")
            p1=os.path.basename(src_fname)
            print("p1: ",p1)
            cv.imwrite(output_dir+"\\"+"train"+"\\"+"images"+"\\"+p1+".jpg",im)
        for fle in files[t_rat:]:
            src_fname, ext = os.path.splitext(fle)
            im=cv.imread(src_fname+".jpg")
            p1=os.path.basename(src_fname)
            cv.imwrite(output_dir+"\\"+"valid"+"\\"+"images"+"\\"+p1+".jpg",im)
def copying_labels(path1,path,output_dir_new):
    path1=path1
    path=path
    f1=[os.path.join(path1,fle) for fle in os.listdir(path1) if fle.endswith(".jpg")]
    for fle in f1:
        src_fname,ext=os.path.splitext(fle)
        t1=path+"\\"+os.path.basename(src_fname)+".txt"
        p1=os.path.basename(src_fname)
        with open(t1,'r') as f:
            label_list=f.readlines()
        with open(output_dir_new+"\\"+p1+".txt",'w')as f1:
            for line in label_list:
                f1.write(line)
        
    

path = r"C:\all\road signs"

output_dir=r"C:\Trash-5" #output folder dir
path1=output_dir+"\\"+"train"+"\\"+"images"#where images of train will save
path2=output_dir+"\\"+"valid"+"\\"+"images"#where images of valid will save
output_dir_new1=output_dir+"\\"+"train"+"\\"+"labels"#where lbales of train will save
output_dir_new2=output_dir+"\\"+"valid"+"\\"+"labels"#where output labels of valid will save
files = [os.path.join(path,fle) for fle in os.listdir(path) if fle.endswith(".jpg")]
shuffle(files)#doing shuffling
l=len(files)
t_rat=int(0.8*l)


splitting_images(path,output_dir,t_rat)
copying_labels(path1,path,output_dir_new1)
copying_labels(path2,path,output_dir_new2)

