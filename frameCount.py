import numpy as np
import glob
import os
import argparse
import cv2

# Creating a parser
parser = argparse.ArgumentParser()

# Parameter passing from command line
parser.add_argument('--list', type=str, default='')
parser.add_argument('--delimiter', type=str, default=',')

# parser.add_argument('')
args = parser.parse_args()

fileList = args.list
delimiter = args.delimiter

fileName = np.genfromtxt(fileList, delimiter=delimiter, usecols=0, dtype=None, encoding='utf-8')
frameList = ()

for i in range (len(fileName)):
    cap = cv2.VideoCapture(fileName[i])
    frameNumber = int(cap.get(7)) # get the number of frames
    frameList = np.append(frameList, frameNumber)
    print(fileName[i]+' has '+str(frameNumber)+' frames')

print(str(len(frameList)))
np.savetxt('./result/framelist.csv', frameList, '%s', delimiter=delimiter)


