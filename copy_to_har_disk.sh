#!/bin/bash
cd /home/user/Downloads/sample_apk
for folder in */;
do
	NUMBER=$(echo $folder | tr -dc '0-9')
	echo $NUMBER
	cd /media/user/utkarsh
	mkdir $NUMBER
	cp /home/user/Downloads/sample_apk/"$NUMBER"/AndroidManifest.xml /media/user/utkarsh/"$NUMBER"
	cp -r /home/user/Downloads/sample_apk/"$NUMBER"/smali /media/user/utkarsh/"$NUMBER"
done
