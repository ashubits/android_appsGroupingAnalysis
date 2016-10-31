import fnmatch
import os
folderLoc = '/home/utkarsh/Documents/android'
directory=[]

for f_name in os.listdir(folderLoc):
    directory.append(f_name)

for folders in directory:
	absoluteLoc  = os.path.join(folderLoc,folders)
	matches = []
	for root, dirnames, filenames in os.walk(absoluteLoc):
	    for filename in fnmatch.filter(filenames, '*.smali'):
	        matches.append(os.path.join(root, filename))
	textFileLoc = "/home/utkarsh/Documents/textFileApk/" + folders +".txt"
	with open(textFileLoc, 'w') as outfile:
	    for fname in matches:
	        with open(fname) as infile:
	            for line in infile:
	                outfile.write(line)

