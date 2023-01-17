import pandas as pd
import os
import re

def grep(l, s):
    return [i for i in l if s in i]
  
files = pd.read_excel(r'R:\***\BioInfoProjects\temp_SW\WO368\files.xlsx', dtype = str)
fastqc_files = pd.read_csv(r'R:\***\BioInfoProjects\temp_SW\WO368\fastqcfilesall.txt', dtype = str)
topoffs_files = pd.read_csv(r'R:\***\BioInfoProjects\temp_SW\WO368\topoffs.txt', dtype = str)
sample_list_R1 = grep(grep(files['dxfiles'], topoff_sample), "R1")


R1_topoffs_list = grep(topoffs_files["dxfiles"],"R1")
for j, val in enumerate(R1_topoffs_list):
    topoff_filename = R1_topoffs_list[j]
    topoff_sample = R1_topoffs_list[j].split("-")[2].split("_")[0]
    #print(topoff_sample)

    for i, val in enumerate(files["File"]):
        listoffiles = []
        if files["File"][i].find(topoff_sample) > 0 and files["File"][i].find("R1") > 0:
            run = files["Run"][i]
            merged_name_R1 = files["File"][i]
            new_file_name_R1 = merged_name_R1+"2"
            dx_topoffs_folder_name = "project-***:/WO368_WholeBlood/TOP_OFF/MERGED_TOP_OFF_FASTQ/"
            dx_run_folder_name = "project-***:/WO368_WholeBlood/"+run+"/MERGED_FASTQ/"
            dx_fastqc_folder_name = "project-***:/WO368_WholeBlood/"+run+"/FASTQC/"
            #fastqc_file = grep(grep(fastqc_files["dxfiles"], topoff_sample), "R1")[0]
            listoffiles.append(merged_name_R1)
            #print(run)
            print("dx cd",dx_run_folder_name)
            print("dx download",merged_name_R1)
            print("dx cd",dx_topoffs_folder_name)
            print("dx download",topoff_filename)
            print("cat ",end="")
            print(merged_name_R1, end=" ")
            print(topoff_filename, end="")
            print(" > ",new_file_name_R1 ,sep = "")
            print("mv ",merged_name_R1, " trash/",merged_name_R1,sep="")
            print("mv ",new_file_name_R1, " ", merged_name_R1,sep="")
            print("dx cd",dx_run_folder_name)
            print("dx mv ",merged_name_R1, " ../trashables/",merged_name_R1,sep="")
            print("dx cd project-***/WO368_WholeBlood/TOP_OFF/MERGED_ORIGINAL_plus_TOP_OFF")
            print("dx upload ", merged_name_R1, sep = "")
            #print("dx cd",dx_fastqc_folder_name)
            #print("dx mv ",fastqc_file, " trashables/",fastqc_file,sep="")
            #print("dx cd",dx_run_folder_name)
            #print("dx run fastqc -ireads="+merged_name_R1+" --yes --destination=../FASTQC/;done")
            print(" ")
            
R2_topoffs_list = grep(topoffs_files["dxfiles"],"R2")
for j, val in enumerate(R2_topoffs_list):
    topoff_filename = R2_topoffs_list[j]
    topoff_sample = R2_topoffs_list[j].split("-")[2].split("_")[0]
    #print(topoff_sample)

    for i, val in enumerate(files["File"]):
        listoffiles = []
        if files["File"][i].find(topoff_sample) > 0 and files["File"][i].find("R2") > 0:
            run = files["Run"][i]
            merged_name_R2 = files["File"][i]
            new_file_name_R2 = merged_name_R2+"2"
            dx_topoffs_folder_name = "project-***:/WO368_WholeBlood/TOP_OFF/MERGED_TOP_OFF_FASTQ/"
            dx_run_folder_name = "project-***:/WO368_WholeBlood/"+run+"/MERGED_FASTQ/"
            dx_fastqc_folder_name = "project-***:/WO368_WholeBlood/"+run+"/FASTQC/"
            #fastqc_file = grep(grep(fastqc_files["dxfiles"], topoff_sample), "R2")[0]
            listoffiles.append(merged_name_R2)
            #print(run)
            print("dx cd",dx_run_folder_name)
            print("dx download",merged_name_R2)
            print("dx cd",dx_topoffs_folder_name)
            print("dx download",topoff_filename)
            print("cat ",end="")
            print(merged_name_R2, end=" ")
            print(topoff_filename, end="")
            print(" > ",new_file_name_R2 ,sep = "")
            print("mv ",merged_name_R2, " trash/",merged_name_R2,sep="")
            print("mv ",new_file_name_R2, " ", merged_name_R2,sep="")
            print("dx cd",dx_run_folder_name)
            print("dx mv ",merged_name_R2, " ../trashables/",merged_name_R2,sep="")
            print("dx cd project-***:/WO368_WholeBlood/TOP_OFF/MERGED_ORIGINAL_plus_TOP_OFF")
            print("dx upload ", merged_name_R2, sep = "")
            #print("dx cd",dx_fastqc_folder_name)
            #print("dx mv ",fastqc_file, " trashables/",fastqc_file,sep="")
            #print("dx cd",dx_run_folder_name)
            #print("dx run fastqc -ireads="+merged_name_R2+" --yes --destination=../FASTQC/;done")
            print(" ")
