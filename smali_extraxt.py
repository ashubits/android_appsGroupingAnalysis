import fnmatch
import os
import argparse
import shutil
parser = argparse.ArgumentParser(description='Output several text files of smali files combined, corrosponding to each apk')
parser.add_argument('-d','--directory', help='Location of Directory(folder) to scan for apk files', required=True)
parser.add_argument('-o','--txtfile', help='Location of the text file', required=True)
args = vars(parser.parse_args())
folderLoc = args['directory']
txtFileName = args['txtfile']
directorys=[]
if not (os.path.isdir(txtFileName + "/CALENDER")):
	os.mkdir(txtFileName + "/CALENDER",0711)
if not (os.path.isdir(txtFileName + "/CAMERA")):
	os.mkdir(txtFileName + "/CAMERA",0711)
if not (os.path.isdir(txtFileName + "/PHONE")):
	os.mkdir(txtFileName + "/PHONE",0711)
if not (os.path.isdir(txtFileName + "/SENSOR")):
	os.mkdir(txtFileName + "/SENSOR",0711)
if not (os.path.isdir(txtFileName + "/SMS")):
	os.mkdir(txtFileName + "/SMS",0711)
if not (os.path.isdir(txtFileName + "/CONTACTS")):
	os.mkdir(txtFileName + "/CONTACTS",0711)
if not (os.path.isdir(txtFileName + "/MICROPHONE")):
	os.mkdir(txtFileName + "/MICROPHONE",0711)
if not (os.path.isdir(txtFileName + "/LOCATION")):
	os.mkdir(txtFileName + "/LOCATION",0711)
if not (os.path.isdir(txtFileName + "/OTHERS")):
	os.mkdir(txtFileName + "/OTHERS",0711)
if not (os.path.isdir(txtFileName + "/STORAGE")):
	os.mkdir(txtFileName + "/STORAGE",0711)


for f_name in os.listdir(folderLoc):
    directorys.append(f_name)

for folders in directorys:
	absoluteLoc  = os.path.join(folderLoc,folders)
	matches = []
	for root, dirnames, filenames in os.walk(absoluteLoc):
	    for filename in fnmatch.filter(filenames, '*.smali'):
	        matches.append(os.path.join(root, filename))

	textFileLoc =folders +".txt"
	with open(textFileLoc, 'w') as outfile:
	    for fname in matches:
	        with open(fname) as infile:
	            for line in infile:
	                outfile.write(line)


	shutil.move(textFileLoc,txtFileName + "/" +os.path.basename(args['directory']))
	
