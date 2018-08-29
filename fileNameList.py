import numpy as np
import glob
import os
import argparse

# Creating a parser
parser = argparse.ArgumentParser()

# Parameter passing from command line
parser.add_argument('--source', type=str, default='')
parser.add_argument('--format', type=str, default='*')
parser.add_argument('--depth', type=int, default=1)
parser.add_argument('--save', type=str, default='')
parser.add_argument('--delimiter', type=str, default=',')

#parser.add_argument('')

args = parser.parse_args()

sourceFolder = args.source
folderDepth = args.depth
fileFormat = args.format
saveFolder = args.save
csvDelimiter = args.delimiter

depthPath = ''
for i in range(folderDepth):
    depthPath = depthPath+'/*'

print(' Dataset is loaded from : ' +sourceFolder)
print(' Filelist will be saved at : ' +saveFolder)

dataList = glob.glob(sourceFolder+depthPath+'.'+fileFormat)
numData = len(dataList)

print('The number of your data is '+str(numData))


dataList = np.asarray(dataList)
dataList= np.reshape(dataList, (len(dataList),1))
dataList = np.insert(dataList, 1, values=0, axis=1)
dataList = np.insert(dataList, 2, values=0, axis=1)
dataList = np.insert(dataList, 3, values=0, axis=1)
# Result Directory
if not os.path.isdir(saveFolder):
    print ("Path doesn't exist. Trying to make "+saveFolder)
    os.makedirs(saveFolder)

if os.path.isfile(saveFolder+"/filelist.csv"):
    print ("File already exists")
    inputFileName = input("Give me new file name : ")
    try:
        newFilePath = saveFolder+'/'+inputFileName+'.csv'
        np.savetxt(newFilePath, dataList, '%s', delimiter=csvDelimiter)
        print("Filelist is saved at "+newFilePath)
    except:
        print("Cannot make file. Try again !")

else:
    try:
        np.savetxt(saveFolder+"/filelist.csv", dataList, '%s', delimiter=csvDelimiter)
        print("Filelist is saved at "+saveFolder)
    except:
        print("Cannot make the file... Try again !")


