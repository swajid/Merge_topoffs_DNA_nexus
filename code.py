import pandas as pd
import os
import re

files = pd.read_csv(r'R:\***\BioInfoProjects\temp_SW\JNJ-WO346B_Topoffs\merge_files\ls.txt')

def grep(l, s):
    return [i for i in l if s in i]

print("#!/bin/bash")
for i, val in enumerate(topoff_list_R1):
    topoff_R1 = topoff_list_R1[i]
    sample_name_R1 = topoff_R1.split("_")[0]
    sample_list_R1 = grep(grep(files['dxfiles'], sample_name_R1), "R1")
    new_file_name_R1 = sample_name_R1+"_merged_L001_R1_001_2.fastq.gz"
    print("cat ",end="")
    for j, val in enumerate(sample_list_R1):
        print(sample_list_R1[j]," ",sep="",end="")
    print("> ",new_file_name_R1 ,sep = "")

    for k, val in enumerate(sample_list_R1):
        print("mv ",sample_list_R1[k]," ","trashables/",sample_list_R1[k],sep="")
        print("dx mv ",sample_list_R1[k]," ","trashables/",sample_list_R1[k],sep="")    

    print("dx upload ", new_file_name_R1, sep = "")
    print(" ")files = pd.read_csv(r'R:\***\BioInfoProjects\temp_SW\JNJ-WO346B_Topoffs\merge_files\ls.txt')

for i, val in enumerate(topoff_list_R2):
    topoff_R2 = topoff_list_R2[i]
    sample_name_R2 = topoff_R2.split("_")[0]
    sample_list_R2 = grep(grep(files['dxfiles'], sample_name_R2), "R2")
    new_file_name_R2 = sample_name_R2+"_merged_L001_R2_001_2.fastq.gz"
    print("cat ",end="")
    for j, val in enumerate(sample_list_R2):
        print(sample_list_R2[j]," ",sep="",end="")
    print("> ",new_file_name_R2 ,sep = "")

    for k, val in enumerate(sample_list_R2):
        print("mv ",sample_list_R2[k]," ","trashables/",sample_list_R2[k],sep="")
        print("dx mv ",sample_list_R2[k]," ","trashables/",sample_list_R2[k],sep="")    

    print("dx upload ", new_file_name_R2, sep = "")
    print(" ")
