#!/usr/bin python2

import os,argparse,sys,shutil

parser = argparse.ArgumentParser(description='input location')
parser.add_argument('-d','--directory', help='input location', required=True)
# parser.add_argument('-o','--directory2', help='Location of the text file', required=True)
args = vars(parser.parse_args())

folderLoc=args['directory']
# folderLoc2 = args['directory2']

if not os.path.exists(folderLoc):
	print "Directory doesn't exist"
	sys.exit()

orig_stdout = sys.stdout
f = file('out.txt', 'w')
sys.stdout = f
files=[]
for file in os.listdir(folderLoc):
    files.append(file)



# folderLoc2=folderLoc+'/objdump_error'
# if not os.path.exists(folderLoc2):
# 	os.system("mkdir \""+ folderLoc2+"\"")

# folderLoc3=folderLoc+'/apk_codes'
# if not os.path.exists(folderLoc3):
#  	os.system("mkdir \""+ folderLoc3+"\"")


for file in files:
	source = folderLoc+'/'+file
	# dest=folderLoc+'/'+file
	
	test="apktool d " + source 
	print file,
	print os.system(test)



sys.stdout = orig_stdout
sys.stdout.close()
# 	f1=open('out.txt','r')
# 	a=f1.readline()
# 	if a:
# 		b=a.split()
# 		# print b
# 		if b[0]=="sh:":
# 			os.system("rm " + dest + ".asm")
# 			destination = folderLoc2+'/'
# 			# print source,destination
# 			shutil.move(source, destination)
# 	f1.close()

# os.system("rm error_file")
