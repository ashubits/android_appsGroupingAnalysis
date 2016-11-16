#Grouping decompressed apks on the basis of permissions they access.
```
usage:
python android_permission.py

Copies the decompressed apk folder to some already created folders on the basis of permission they
access. It also creates a csv file containing name of apk and with the value 0 or 1 depending upon
whether that apk requires that specific permission or not.

```
**opcodeList.txt** contains all the opcodes which we will scan.                                       

**opcodes_frequency.csv** contains frequency of occurance of opcodes in opcodeList in all the smali files present.  

**size_of_apks.csv** contains range of size of apks with the factor of 200KB.

**permission_frequency.csv** contains frequency of permissions accessed by the apk along with their sum.
#Frequency scanner for size of apks
```
usage:
python size_of_apk_frequency.py

Output a csv file containing the frequency range of size of apks with a factor of 200KB present
in a specific folder.


```
#Extracting smali files from different apks
```
usage:
python smali_extreact.py

Output txt files in an already specified folder with title as name of the apk and contains all 
the smali files of that apk concatenated in it.

```
#Opcode frequency scanner for smali files present in apks

```
usage:
python smali_opcodes_to_frequency.py

Output a csv file containing the frequency of all opcodes present in smali file.

```
