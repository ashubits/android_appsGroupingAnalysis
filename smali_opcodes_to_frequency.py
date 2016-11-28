#!/usr/bin python2
from __future__ import print_function
import os
import sys
import argparse

parser = argparse.ArgumentParser(description='Output csv file with frequency of each opcode ')
parser.add_argument('-d','--directory', help='Location of Directory(folder) to scan for smali text files', required=True)
args = vars(parser.parse_args())



f1 = open('opcodeList.txt', 'r')
opcodes=[]
for eachLine in f1:
	opcodes.extend(eachLine.split()) 			#adding all opcodes in an array
f1.close()

folderLoc= args['directory']
# outputLoc  = args['csvfile']
files=[]
for filer in os.listdir(folderLoc):
    if filer.endswith(".txt"):
    	files.append(filer)
    
outputFile  = 'freq.csv'
outfile= open(outputFile, 'w')
outfile.write(' ')
outfile.write(',')
for codes in opcodes:
	outfile.write(codes)
	outfile.write(',')
outfile.write('\n')
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
	
	outfile.write(filer)
	
	for x in range (0,256):
		outfile.write(',')
		outfile.write('%d'%number[x])
		
	outfile.write('\n')
	f1.close()
		
	
outfile.close()


# print "Done! Saved to file",out_file
