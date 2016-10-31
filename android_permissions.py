#! /usr/bin python2
from __future__ import print_function

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

# print per_all

folderLoc='/home/utkarsh/Downloads/ando'

directory=[]
for f_name in os.listdir(folderLoc):
    directory.append(f_name)

orig_stdout = sys.stdout
f = file('out.txt', 'w')
sys.stdout = f

s = " ,CALANDER,CAMERA,CONTACTS,LOCATION,MICROPHONE,PHONE,SENSOR,SMS,STORAGE,TOTAL "
fal=0

print(s,end='')

for f_name in directory:
	x = [0]*9
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
			flag = [0]*9
			for app_per in permission_app:
				
			
				if app_per in per_calender:
					dst=folderLoc+"/CALENDER"
					x[0] = 1
					if flag[0]==0:
						flag[0] = 1
						total = total+1
					#os.system("cp -r \"" +fileLoc+ "\" \"" + dst+"\"")

				if app_per in per_camera:
					dst=folderLoc+"/CAMERA"
					x[1] = 1
					if flag[1] == 0:
						flag[1] = 1
						total = total+1
					#os.system("cp -r \"" +fileLoc+ "\" \"" + dst+"\"")
				if app_per in per_contacts:
					dst=folderLoc+"/CONTACTS"
					x[2] = 1
					if flag[2] == 0:
						flag[2] = 1
						total = total+1
					#os.system("cp -r \"" +fileLoc+ "\" \"" + dst+"\"")
				if app_per in per_location:
					dst=folderLoc+"/LOCATION"
					x[3] = 1
					if flag[3] == 0:
						flag[3] = 1
						total = total+1
					#os.system("cp -r \"" +fileLoc+ "\" \"" + dst+"\"")
				if app_per in per_microphone:
					dst=folderLoc+"/MICROPHONE"
					x[4] = 1
					if flag[4] == 0:
						flag[4] = 1
						total = total+1

					#os.system("cp -r \"" +fileLoc+ "\" \"" + dst+"\"")
				if app_per in per_phone:
					dst=folderLoc+"/PHONE"
					x[5] = 1
					if flag[5] == 0:
						flag[5] = 1
						total = total+1
					#os.system("cp -r \"" +fileLoc+ "\" \"" + dst+"\"")
				if app_per in per_sensor:
					dst=folderLoc+"/SENSOR"
					x[6] = 1
					if flag[6] == 0:
						flag[6] = 1
						total = total+1
					#os.system("cp -r \"" +fileLoc+ "\" \"" + dst+"\"")
				if app_per in per_sms:
					dst=folderLoc+"/SMS"
					x[7] = 1
					if flag[7] == 0:
						flag[7] = 1
						total = total+1
					#os.system("cp -r \"" +fileLoc+ "\" \"" + dst+"\"")
				if app_per in per_storage:
					dst=folderLoc+"/STORAGE"
					x[8] = 1
					if flag[8] == 0:
						flag[8] = 1
						total = total+1
					#os.system("cp -r \"" +fileLoc+ "\" \"" + dst+"\"")
		if fal==0:
			print()
			fal=fal+1
		print(f_name,end=',')
		print(",".join(str(l) for l in x),end="")
		print(",",end='')
		print(total)
	

			
	except:
		pass




#sys.stdout = open('%s' % out_file, 'w')

sys.stdout = orig_stdout
sys.stdout.close()

