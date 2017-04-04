#! /usr/bin python2
from __future__ import print_function
import argparse
import re,os,sys



per_calender=['READ_CALENDAR','WRITE_CALENDAR']

per_camera=['CAMERA']

per_contacts=['READ_CONTACTS','WRITE_CONTACTS','GET_ACCOUNTS']

per_location=['ACCESS_FINE_LOCATION','ACCESS_COARSE_LOCATION']

per_microphone=['RECORD_AUDIO']

per_phone=['READ_PHONE_STATE','CALL_PHONE','READ_CALL_LOG','WRITE_CALL_LOG','ADD_VOICEMAIL','USE_SIP','PROCESS_OUTGOING_CALLS'] 

per_sensor=['BODY_SENSORS']

per_sms=['SEND_SMS','RECEIVE_SMS','READ_SMS','RECEIVE_WAP_PUSH','RECEIVE_MMS']

per_storage=['READ_EXTERNAL_STORAGE','WRITE_EXTERNAL_STORAGE']

all_permissions=[
'READ_CALENDAR','WRITE_CALENDAR'
,
'CAMERA'

,'READ_CONTACTS','WRITE_CONTACTS','GET_ACCOUNTS',

'ACCESS_FINE_LOCATION','ACCESS_COARSE_LOCATION',

'RECORD_AUDIO'

,'READ_PHONE_STATE','CALL_PHONE','READ_CALL_LOG','WRITE_CALL_LOG','ADD_VOICEMAIL','USE_SIP','PROCESS_OUTGOING_CALLS',

'BODY_SENSORS',

'SEND_SMS','RECEIVE_SMS','READ_SMS','RECEIVE_WAP_PUSH','RECEIVE_MMS',

'READ_EXTERNAL_STORAGE','WRITE_EXTERNAL_STORAGE'
]
parser = argparse.ArgumentParser(description='Output several text files of smali files combined, corrosponding to each apk')
parser.add_argument('-d','--director', help='Location of Directory(folder) to scan for apk files', required=True)
parser.add_argument('-o','--flocation', help='Location of the final folders', required=True)

args = vars(parser.parse_args())

folderLoc = args['director']

floc = args['flocation']


if not os.path.isdir(floc + "CALENDER"):
	os.mkdir(floc + "CALENDER",0711)
if not os.path.isdir(floc + "CAMERA"):
	os.mkdir(floc + "CAMERA",0711)
if not os.path.isdir(floc + "SMS"):
	os.mkdir(floc + "SMS",0711)
if not os.path.isdir(floc + "CONTACTS"):
	os.mkdir(floc + "CONTACTS",0711)
if not os.path.isdir(floc + "MICROPHONE"):
	os.mkdir(floc + "MICROPHONE",0711)
if not os.path.isdir(floc + "PHONE"):
	os.mkdir(floc + "PHONE",0711)
if not os.path.isdir(floc + "LOCATION"):
	os.mkdir(floc + "LOCATION",0711)
if not os.path.isdir(floc + "STORAGE"):
	os.mkdir(floc + "STORAGE",0711)
if not os.path.isdir(floc + "OTHERS"):
	os.mkdir(floc + "OTHERS",0711)
if not os.path.isdir(floc + "SENSOR"):
	os.mkdir(floc + "SENSOR",0711)






directory=[]
for f_name in os.listdir(folderLoc):
    directory.append(f_name)

orig_stdout = sys.stdout
f = file('out.csv', 'w')
sys.stdout = f

s = " ,CALANDER,CAMERA,CONTACTS,LOCATION,MICROPHONE,PHONE,SENSOR,SMS,STORAGE,OTHERS,TOTAL "
fal=0

print(s,end='')

for f_name in directory:
	x = [0]*10
	total = 0
	j = 0
	fLoc=folderLoc+'/'+f_name
	# fLoc = fLoc[:-4]

  #   if not os.path.exists(fLoc):
  #   	print "f_name doesn't exist for ", f_name
		# break

	rel_path =f_name+ "/AndroidManifest.xml"
	abs_fpath = os.path.join(folderLoc, rel_path)

	try:

		with open(abs_fpath, 'r') as f:
			# #os.system("aapt d permissions "+ abs_fpath)
			
			next(f)
			permission_app=[]
			for line in f:
				a=line.split()
				if a[0]=="<uses-permission":
					for perm in all_permissions:
						if perm in a[1]:
							permission_app.append(perm)

			
					# permission_app.append(re.search('.permission.(.*?)"/>', a[1]).group(1))

	
			fileLoc=folderLoc+"/"+f_name
			flag = [0]*10
			counter = 0
			for app_per in permission_app:
				
				

				if app_per in per_calender:
					dst=floc + "CALENDER"
					x[0] = 1
					counter = counter+1
					if flag[0]==0:
						
						flag[0] = 1
						total = total+1
					os.system("cp -r \"" +fileLoc+ "\" \"" + dst+"\"")

				if app_per in per_camera:
					dst=floc + "CAMERA"
					x[1] = 1
					counter = counter+1
					if flag[1] == 0:
						flag[1] = 1
						total = total+1
					os.system("cp -r \"" +fileLoc+ "\" \"" + dst+"\"")
				if app_per in per_contacts:
					dst=floc + "CONTACTS"
					x[2] = 1
					counter = counter+1
					if flag[2] == 0:
						flag[2] = 1
						total = total+1
					os.system("cp -r \"" +fileLoc+ "\" \"" + dst+"\"")
				if app_per in per_location:
					dst=floc + "LOCATION"
					x[3] = 1
					counter = counter+1
					if flag[3] == 0:
						flag[3] = 1
						total = total+1
					os.system("cp -r \"" +fileLoc+ "\" \"" + dst+"\"")
				if app_per in per_microphone:
					dst=floc + "MICROPHONE"
					x[4] = 1
					counter = counter+1
					if flag[4] == 0:
						flag[4] = 1
						total = total+1

					os.system("cp -r \"" +fileLoc+ "\" \"" + dst+"\"")
				if app_per in per_phone:
					dst=floc+"PHONE"
					x[5] = 1
					counter = counter+1
					if flag[5] == 0:
						flag[5] = 1
						total = total+1
					os.system("cp -r \"" +fileLoc+ "\" \"" + dst+"\"")
				if app_per in per_sensor:
					dst=floc + "SENSOR"
					x[6] = 1
					counter = counter+1
					if flag[6] == 0:
						flag[6] = 1
						total = total+1
					os.system("cp -r \"" +fileLoc+ "\" \"" + dst+"\"")
				if app_per in per_sms:
					dst=floc + "SMS"
					x[7] = 1
					counter = counter+1
					if flag[7] == 0:
						flag[7] = 1
						total = total+1
					os.system("cp -r \"" +fileLoc+ "\" \"" + dst+"\"")
				if app_per in per_storage:
					dst=floc + "STORAGE"
					x[8] = 1
					counter = counter+1
					if flag[8] == 0:
						flag[8] = 1
						total = total+1
					os.system("cp -r \"" +fileLoc+ "\" \"" + dst+"\"")
			if counter==0 :
				dst=floc + "OTHERS"
				x[9] = 1
				if flag[9] == 0:
					flag[9] = 1
					total = total+1
				os.system("cp -r \"" +fileLoc+ "\" \"" + dst+"\"")
		if fal==0:
			print()
			fal=fal+1
		print(f_name,end=',')
		print(",".join(str(l) for l in x),end="")
		print(",",end='')
		print(total)
	

			
	except:
		pass




# sys.stdout = open('%s' % out_file, 'w')

sys.stdout = orig_stdout
sys.stdout.close()

