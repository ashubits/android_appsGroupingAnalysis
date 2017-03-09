#!/usr/bin python2

import os,argparse,sys,shutil

parser = argparse.ArgumentParser(description='input location')
parser.add_argument('-d','--directory', help='input location', required=True)

args = vars(parser.parse_args())

folderLoc=args['directory']

if not os.path.exists(folderLoc):
	print "Directory doesn't exist"
	sys.exit()

orig_stdout = sys.stdout
f = file('out.txt', 'w')
sys.stdout = f
files=[]
for file in os.listdir(folderLoc):
    files.append(file)




for file in files:
	source = folderLoc+'/'+file
	
	test="apktool d " + source 
	print file,
	print os.system(test)

sys.stdout = orig_stdout
sys.stdout.close()
 	
