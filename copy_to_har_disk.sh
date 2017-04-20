#!/bin/bash

#from external to internal

cp -R /media/user/utkarsh/all_apk/ /home/user/Downloads/sample_apk #location where .apk files are present to location in internal memory where we want to copy

#apktool
cd /home/user/Downloads/sample_unzipped #location where we want decompressed apks
for file in /home/user/Downloads/sample_apk/*.apk;  
do
	
	apktool d $file
done
#transferring smali and manifest file to external disk
cd /home/user/Downloads/sample_unzipped
mkdir /media/user/utkarsh/unzipped
for folder in */;
 do
 	NUMBER=$(echo $folder | tr -dc '0-9')
 	cd /media/user/utkarsh/unzipped/ #location in harddisk where we want manifest file and smali file
	mkdir $NUMBER
 	cp /home/user/Downloads/sample_apk/"$NUMBER"/AndroidManifest.xml /media/user/utkarsh/unzipped/"$NUMBER"
 	cp -R /home/user/Downloads/sample_apk/"$NUMBER"/smali /media/user/utkarsh/unzipped/"$NUMBER"
 done

#grouping
cd /home/user/Downloads/all_codes #location where android_permission code is present
python android_permissions.py -d /media/user/utkarsh/unzipped -o /media/user/utkarsh/categorised #instructions on github

#to generate frequency csv
python smali_opcodes_to_frequency.py -d /media/user/utkarsh/categorised/CALENDER -o /media/user/utkarsh/categorised/CALENDER #instructions on github

#number of apks in each category
chmod +x x.sh #x.sh is hardcoded so we need to change locations.
./x.sh

 
#done
