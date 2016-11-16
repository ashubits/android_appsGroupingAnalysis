#! /usr/bin python2
from __future__ import print_function

import re,os,sys

per_calender=['READ_CALENDAR','WRITE_CALENDAR']

per_camera=['CAMERA']

per_contacts=['READ_CONTACTS','WRITE_CONTACTS','GET_ACcounterS']

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

,'READ_CONTACTS','WRITE_CONTACTS','GET_ACcounterS',

'ACCESS_FINE_LOCATION','ACCESS_COARSE_LOCATION',

'RECORD_AUDIO'

,'READ_PHONE_STATE','CALL_PHONE','READ_CALL_LOG','WRITE_CALL_LOG','ADD_VOICEMAIL','USE_SIP','PROCESS_OUTGOING_CALLS',

'BODY_SENSORS',

'SEND_SMS','RECEIVE_SMS','READ_SMS','RECEIVE_WAP_PUSH','RECEIVE_MMS',

'READ_EXTERNAL_STORAGE','WRITE_EXTERNAL_STORAGE'
]




os.mkdir("CALENDER",0711)
os.mkdir("CAMERA",0711)
os.mkdir("LOCATION",0711)
os.mkdir("OTHERS",0711)
os.mkdir("SENSOR",0711)
os.mkdir("PHONE",0711)
os.mkdir("SMS",0711)
os.mkdir("MICROPHONE",0711)
os.mkdir("STORAGE",0711)
os.mkdir("CONTACTS",0711)

folderLoc='/home/utkarsh/Documents/android'

directory=[]
for f_name in os.listdir(folderLoc):
    directory.append(f_name)

orig_stdout = sys.stdout
f = file('permissions_frequency.csv', 'w')
sys.stdout = f

s = " ,CALANDER,CAMERA,CONTACTS,LOCATION,MICROPHONE,PHONE,SENSOR,SMS,STORAGE,OTHERS,TOTAL"
fal=0

print(s,end='')

for f_name in directory:
	x = [0]*10
	total = 0
	j = 0
	fLoc=folderLoc+'/'+f_name

	rel_path =f_name+ "/AndroidManifest.xml"
	abs_fpath = os.path.join(folderLoc, rel_path)
	
	try:

		with open(abs_fpath, 'r') as f:
			next(f)
			permission_app=[]
			for line in f:
				a=line.split()
				if a[0]=="<uses-permission":
					for perm in all_permissions:
						if perm in a[1]:
							permission_app.append(perm)

				
			xloc  = '/home/utkarsh/Documents'
			fileLoc=folderLoc+"/"+f_name
			flag = [0]*10
			counter = 0
			for app_per in permission_app:
				
				if app_per in per_calender:
					dst=xloc+"/CALENDER"
					x[0] = 1
					if flag[0]==0:
						counter = counter+1
						flag[0] = 1
						total = total+1
					os.system("cp -r \"" +fileLoc+ "\" \"" + dst+"\"")

				if app_per in per_camera:
					dst=xloc+"/CAMERA"
					x[1] = 1					
					if flag[1] == 0:
						counter = counter+1
						flag[1] = 1
						total = total+1
					os.system("cp -r \"" +fileLoc+ "\" \"" + dst+"\"")
				if app_per in per_contacts:
					dst=xloc+"/CONTACTS"
					x[2] = 1
					if flag[2] == 0:
						counter = counter+1
						flag[2] = 1
						total = total+1
					os.system("cp -r \"" +fileLoc+ "\" \"" + dst+"\"")
				if app_per in per_location:
					dst=xloc+"/LOCATION"
					x[3] = 1					
					if flag[3] == 0:
						counter = counter+1
						flag[3] = 1
						total = total+1
					os.system("cp -r \"" +fileLoc+ "\" \"" + dst+"\"")
				if app_per in per_microphone:
					dst=xloc+"/MICROPHONE"
					x[4] = 1
					if flag[4] == 0:
						counter = counter+1
						flag[4] = 1
						total = total+1
					os.system("cp -r \"" +fileLoc+ "\" \"" + dst+"\"")
				if app_per in per_phone:
					dst=xloc+"/PHONE"
					x[5] = 1
					if flag[5] == 0:
						counter = counter +1
						flag[5] = 1
						total = total+1
					os.system("cp -r \"" +fileLoc+ "\" \"" + dst+"\"")
				if app_per in per_sensor:
					dst=xloc+"/SENSOR"
					x[6] = 1
					if flag[6] == 0:
						counter = counter+1
						flag[6] = 1
						total = total+1
					os.system("cp -r \"" +fileLoc+ "\" \"" + dst+"\"")
				if app_per in per_sms:
					dst=xloc+"/SMS"
					x[7] = 1					
					if flag[7] == 0:
						counter = counter+1
						flag[7] = 1
						total = total+1
					os.system("cp -r \"" +fileLoc+ "\" \"" + dst+"\"")
				if app_per in per_storage:
					dst=xloc+"/STORAGE"
					x[8] = 1
					
					if flag[8] == 0:
						counter = counter+1
						flag[8] = 1
						total = total+1
					os.system("cp -r \"" +fileLoc+ "\" \"" + dst+"\"")
			if counter==0:
				dst=xloc+"/OTHERS"
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






sys.stdout = orig_stdout
sys.stdout.close()

