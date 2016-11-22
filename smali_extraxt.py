import fnmatch
import os
import argparse
parser = argparse.ArgumentParser(description='Output several text files of smali files combined, corrosponding to each apk')
parser.add_argument('-d','--directory', help='Location of Directory(folder) to scan for apk files', required=True)
parser.add_argument('-o','--txtfile', help='Location of the text file', required=True)
args = vars(parser.parse_args())

folderLoc = args['directory']
directorys=[]

for f_name in os.listdir(folderLoc):
    directorys.append(f_name)

for folders in directorys:
	absoluteLoc  = os.path.join(folderLoc,folders)
	matches = []
	for root, dirnames, filenames in os.walk(absoluteLoc):
	    for filename in fnmatch.filter(filenames, '*.smali'):
	        matches.append(os.path.join(root, filename))
	textFileLoc = args['txtfile'] + folders +".txt"
	with open(textFileLoc, 'w') as outfile:
	    for fname in matches:
	        with open(fname) as infile:
	            for line in infile:
	                outfile.write(line)


