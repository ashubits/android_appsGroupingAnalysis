# Grouping decompressed apks on the basis of permissions they access.
```
usage:
python android_permission.py -d input location -o output location

input location is the absolute path of the directory which contains decompressed apks. Output location is the absolute path of the directory where we want all the 10 folders to be created and also there corrosponding smali file is copied to some of the 10 folders depending upon the permissions they use.

```
# Decompress any app using apktool
```
usage:
python apkcompression.py -d input location -o output location

It decompress any .apk file using apktool at the desired location. It also generates a .csv file having a value of 0 if there is no error on decompression else has a value 256 in case of any error.

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
python smali_opcodes_to_frequency.py

Output a csv file containing the frequency of all opcodes present in smali file.

```
