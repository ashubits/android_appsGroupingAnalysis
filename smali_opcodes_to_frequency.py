#!/usr/bin python2
from __future__ import print_function
import os
import sys

f1 = open('opcodeList.txt', 'r')
opcodes=[]
for eachLine in f1:
	opcodes.extend(eachLine.split()) 			#adding all opcodes in an array
f1.close()

folderLoc= '/home/utkarsh/Documents/textFileApk'
files=[]
for filer in os.listdir(folderLoc):
    if filer.endswith(".txt"):
    	files.append(filer)
    
orig_stdout = sys.stdout
f = file('out.txt', 'w')
sys.stdout = f

for filer in files:
	f1 = open(os.path.join(folderLoc, filer), 'r')
	number=[0]*257
	for line in f1:
		splitter = line.split()
		if splitter: 											#checking for null
			a=splitter[0]										#saving first word
			if not(a.startswith('#')): 		#detecting comment or a function
				if a in opcodes:								
					number[opcodes.index(a)]+=1					#increase freq if a is in opcodes
					

	
	f1.close()
for x in range(0,256):
	print(opcodes[x],end=',')
	print(number[x],end='')
	print()


sys.stdout = orig_stdout
sys.stdout.close()

# print "Done! Saved to file",out_file