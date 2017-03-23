#!/usr/bin python2
#paste this code where you want your uncompressed apk
import os,argparse,sys,shutil

parser = argparse.ArgumentParser(description='input location') #location where apks are present
parser.add_argument('-d','--directory', help='input location', required=True)

args = vars(parser.parse_args())

folderLoc=args['directory']

if not os.path.exists(folderLoc):
	print "Directory doesn't exist"
	sys.exit()

orig_stdout = sys.stdout
f = file('out.txt', 'w') #this file will have a value 0 if there is no error, else it will have a value of 256 for that apk
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
 	
