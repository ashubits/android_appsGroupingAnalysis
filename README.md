# Shell script for all the work
```
usage:
./copy_har_disk.sh
1st argument = location of apk's folder in hard disk
2nd argument = location where we want apks to copy in main memory
3rd argument = location of unzipped folder
4th argument = same as 2nd argument/*.apk
5th argument  = make directory in hard disk
6th argument =  same as 5th argument
7th argument = copy location from main memory.
8th argument = destination to hdd
9th argument = same as 7th
10th argument = same as 8th
11th argument  = location of android_permissions code
12th, 13th, 14th, 15th argument = instructions on android_permissions github readme
16th argument = see code of x.sh

order of arguments is accordance with the code.

```

# Grouping decompressed apks on the basis of permissions they access.
```
usage:
python android_permission.py -d input location -o output location

input location is the absolute path of the directory which contains decompressed apks.It requires
opcodeList.txt to be present in the same folder as that of the code folder. Output location is the
absolute path of the directory where we want all the 10 folders to be created. Corrosponding smali
file is copied to some of the 10 folders depending upon the permissions they use. copy of smali file
is also created at the same location. 

```
# Decompress any app using apktool
```
usage:
python apkcompression.py -d input location -o output location

It decompress any .apk file using apktool at the desired location. It also generates a .csv file having
a value of 0 if there is no error on decompression else has a value 256 in case of any error.

```

**opcodeList.txt** contains all the opcodes which we will scan.                                       

**opcodes_frequency.csv** contains frequency of occurance of opcodes in opcodeList in all the smali files present.  

**size_of_apks.csv** contains range of size of apks with the factor of 200KB.

**permission_frequency.csv** contains frequency of permissions accessed by the apk along with their sum.
# Frequency scanner for size of apks
```
usage:
python size_of_apk_frequency.py -d input location -o output location

Output a csv file containing the frequency range of size of apks with a factor of 200KB present
in a specific folder.


```
# Extracting smali files from different apks
```
usage:
python smali_extreact.py

Output txt files in an already specified folder with title as name of the apk and contains all 
the smali files of that apk concatenated in it.

```
# Opcode frequency scanner for smali files present in apks

```
usage:
python smali_opcodes_to_frequency.py -d input location -o output location

input location = location of directory where smali files are present.
output location = location where we want our csv file.

Output a csv file containing the frequency of all opcodes present in smali file.

```
