#!/bin/bash

#from external to internal

cp -R /media/user/utkarsh/all_apk /home/user/Downloads/sample_apk #location where .apk files are present to location in internal memory where we want to copy
#apktool
cd /home/user/Downloads/faltu #location where we want decompressed apks
for file in /home/user/Downloads/sample_apk/*.apk;  
do
	
	apktool d $file
done
#grouping
cd /home/user/Downloads/all_codes #location where android_permission code is present
python android_permissions.py -d /home/user/Downloads/faltu -o /home/user/Downloads/sample_category #instructions on github
#to generate frequency csv
python smali_opcodes_to_frequency.py -d /home/user/Downloads/sample_category/CALENDER -o /home/user/Downloads/sample_category/CALENDER 
#number of apks in each category
chmod +x x.sh
./x.sh

#internal to external
cp -R /home/user/Downloads/sample_category /media/user/utkarsh

 
#done
