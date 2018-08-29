import numpy as np

filelist = '/datahdd/workdir/donghyun/filelist/result/filelist.csv'
framelist = '/datahdd/workdir/donghyun/filelist/result/framelist.csv'
newFilePath = '/datahdd/workdir/donghyun/filelist/result/'
delimiter = ','

fileName = np.genfromtxt(filelist, delimiter=delimiter, usecols=0, dtype=None, encoding='utf-8')
frameList = np.genfromtxt(framelist, delimiter=delimiter, usecols=0, dtype=None, encoding='utf-8')

print(str(len(fileName)))
fileName= np.reshape(fileName, (len(fileName),1))
frameList= np.reshape(frameList, (len(frameList),1))

fileList = np.insert(fileName, 1, values=0, axis=1)
fileList = np.append(fileList, frameList, axis=1)

np.savetxt(newFilePath+'FileList.csv', fileList, '%s', delimiter=delimiter)