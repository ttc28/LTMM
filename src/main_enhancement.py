# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 11:42:58 2016

@author: utkarsh
"""

import numpy as np
from numpy.lib.shape_base import column_stack
#import cv2
#import numpy as np;

import scipy.ndimage
import sys
import cv2
from scipy.ndimage.filters import minimum_filter

import skimage.morphology
import skimage
from time import sleep
from getTerminationBifurcation import getTerminationBifurcation
from removeSpuriousMinutiae import removeSpuriousMinutiae
from image_enhance import image_enhance

def main(nameimage):
    if(len(sys.argv)<2):
        print('loading sample image');
        img_name = str(nameimage)
        img = scipy.ndimage.imread('../images/'+img_name);
    elif(len(sys.argv) >= 2):
        img_name = sys.argv[1];
        img = scipy.ndimage.imread(sys.argv[1]);
        
    if(len(img.shape)>2):
        # img = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
        img = np.dot(img[...,:3], [0.299, 0.587, 0.114]);

    rows,cols = np.shape(img);
    aspect_ratio = np.double(rows)/np.double(cols);

    new_rows = 540;             # randomly selected number
    new_cols = new_rows/aspect_ratio;

    #img = cv2.resize(img,(new_rows,new_cols));
    img = scipy.misc.imresize(img,(np.int(new_rows),np.int(new_cols)));

    enhanced_img = image_enhance(img);    

        
    #img = cv2.imread('../enhanced/enhanced.bmp',0);
    #img = scipy.ndimage.imread('../images/'+img_name);
    #img = np.uint8(img>78);
    img =  enhanced_img

    skel = skimage.morphology.skeletonize(img)
    #skel = skimage.morphology.thin(img)
    skel = np.uint8(skel)*255;
    
    mask = img*255;
    (minutiaeTerm, minutiaeBif) = getTerminationBifurcation(skel, mask);
    
    minutiaeTerm = skimage.measure.label(minutiaeTerm, 8);
    RP = skimage.measure.regionprops(minutiaeTerm)
    minutiaeTerm = removeSpuriousMinutiae(RP, np.uint8(img), 23);
    
    BifLabel = skimage.measure.label(minutiaeBif, 8);
    TermLabel = skimage.measure.label(minutiaeTerm, 8);

    
    
    minutiaeBif = minutiaeBif * 0;
    minutiaeTerm = minutiaeTerm * 0;
    
    (rows, cols) = skel.shape
    DispImg = np.zeros((rows,cols,3), np.uint8)
    DispImg[:,:,0] = skel; DispImg[:,:,1] = skel; DispImg[:,:,2] = skel;
    
    
    RP = skimage.measure.regionprops(BifLabel)
    for i in RP:
        (row, col) = np.int16(np.round(i['Centroid']))
        minutiaeBif[row, col] = 1;
        (rr, cc) = skimage.draw.circle_perimeter(row, col, 3);
        skimage.draw.set_color(DispImg, (rr,cc), (255,0,0));
    
    
    RP = skimage.measure.regionprops(TermLabel)
    for i in RP:
        (row, col) = np.int16(np.round(i['Centroid']))
        minutiaeTerm[row, col] = 1;
        (rr, cc) = skimage.draw.circle_perimeter(row, col, 3);
        skimage.draw.set_color(DispImg, (rr,cc), (0, 0, 255));
    
        (rows, cols) = img.shape;
    file1 = open("x.txt","a")
    file2 = open("y.txt","a")
    arr_X = []
    arr_Y = []
    for i in range(1,rows-1):
        for j in range(1,cols-1):
            if(minutiaeTerm[i][j] == 1):
                file1.write(str(i)+"\r\n")
                file2.write(str(j)+"\r\n")
                arr_X.append(int(i))
                arr_X.append(int(j))
                #print(arr)           
            elif(minutiaeBif[i,j] == 1):
                file1.write(str(i)+"\r\n")
                file2.write(str(j)+"\r\n")
                arr_X.append(int(i))
                arr_X.append(int(j))
    file1.close()
    file2.close()
    scipy.misc.imsave('../enhanced/Minutiae.bmp' ,DispImg)
    sleep(7)
    leng_key = len(arr_X)
    #print(leng_key)

    #a = hex(arr_X[0])
    #a = a.replace('0x','')
    #print('hex',a)
    arr_Key = []
    for i in range(0, len(arr_X)):
        a = hex(arr_X[i])
        a = a.replace('0x','')
        arr_Key.append(a)
    #print(arr_Key)
    #print(type(arr_Key[0]))
    import string
    key = ''.join(arr_Key)
    origin_key  = key
    #print(key[79], key[108])
    #print(key)
    #print(type(key))
    #print(len(key))

    NP = len(key)*4
    Rem = NP % 128
    #print(Rem)
    NP = NP - Rem
    j = NP / 128
    j = int(j)
    key_128bits = ""
    for i in range(0,j):
        key_128bits= ""
        for k in range(16, len(key)-16):
            key_128bits =  key_128bits + key[k]
        key = key_128bits
    #print(len(key_128bits))
    #print(key_128bits)
    #check 128bits
    if len(key_128bits) < 32:
        a = 32 - len(key_128bits)
        t = int(a/2)
        key_word = ""
        for i in range(0,int(a/2)):
            key_word  = key_word + origin_key[int(16*j-a/2+i)]
        key_word = key_word + key_128bits
        for i in range(0,int(a/2)):
            key_word  = key_word + origin_key[int(16*j+len(key_128bits)+i)]
    #print(key_word)


    K128bis = ""
    #swap key
    for i in range(16,len(key_word)):
        K128bis = K128bis + key_word[i]
    for i in range(0,int(len(key_word)/2)):
        K128bis = K128bis + key_word[i]
    
    #print(key_128bits)
    #print(len(key_128bits))
    #print(K128bis)
    return K128bis

#main('11.bmp')