import os,sys,argparse

parser = argparse.ArgumentParser(description='input location') #location where apks are present
parser.add_argument('-d','--directory', help='input location', required=True)
parser.add_argument('-o','--olocation', help='output location of csv', required=True)

args = vars(parser.parse_args())


folderLoc = args['directory']
outlocation = args['olocation']

apkslist = []
size=[]
orig_stdout = sys.stdout
f = file(outlocation + "size_of_apks.csv", 'w')
sys.stdout = f

for apks in os.listdir(folderLoc):
	apkslist.append(apks)
for apk in apkslist:
	size1 = os.path.getsize(os.path.join(folderLoc,apk))
	size2 = size1/1024
	size.append(size2)

# print len(size)
maxSize = int(max(size)/200)
big = [0]*(maxSize+1)
# print maxSize+1

for x in size:
	for i in range(0,maxSize+1):
		if x <200*i:
			big[i]=big[i]+1
			break

for x in range(0,maxSize+1):
	print 200*x ,',',big[x]
sys.stdout = orig_stdout
sys.stdout.close()
