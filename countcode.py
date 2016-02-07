#!/usr/bin/python
import sys
import fnmatch
import os

def searchfolder(folder,filemask):
    filelist=[]
    for root,subFolders,files in os.walk(folder):
        for file in files:
            buildpath=os.path.join(root,file)
            if os.path.isfile(buildpath):            
                if fnmatch.fnmatch(buildpath,filemask):
                    filelist.append(buildpath)
    return filelist
    


def Countlines(filename):
    #counts the lines in filename.
    linecount = sum(1 for line in open(filename))
    return linecount
    
searchfor = sys.argv[1]
searchin = sys.argv[2]
print("examining files matching " + searchfor + " in directory " + searchin)
totalcount=0
for countthese in searchfolder(searchin,searchfor):
    #print Countlines(countthese)
    totalcount = totalcount + Countlines(countthese)

print("total line count:" + str(totalcount))




