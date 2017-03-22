#!/bin/bash

echo -n "CALENDER " >>a.txt
ls /home/user/Downloads/category/CALENDER | wc -l >> a.txt
echo -n "CAMERA " >> a.txt
ls /home/user/Downloads/category/CAMERA | wc -l >> a.txt
echo -n "CONTACTS ">>a.txt
ls /home/user/Downloads/category/CONTACTS | wc -l >> a.txt
echo -n "LOCATION ">>a.txt
ls /home/user/Downloads/category/LOCATION | wc -l >> a.txt
echo -n "MICROPHONE ">>a.txt
ls /home/user/Downloads/category/MICROPHONE | wc -l >> a.txt
echo -n "PHONE ">>a.txt
ls /home/user/Downloads/category/PHONE | wc -l >> a.txt
echo -n "SENSOR ">>a.txt
ls /home/user/Downloads/category/SENSOR | wc -l >> a.txt
echo -n "SMS ">>a.txt
ls /home/user/Downloads/category/SMS | wc -l >> a.txt
echo -n "STORAGE ">>a.txt
ls /home/user/Downloads/category/STORAGE | wc -l >>a.txt
echo -n "OTHERS ">>a.txt
ls /home/user/Downloads/category/OTHERS | wc -l >>a.txt

