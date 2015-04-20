#!/usr/bin/python
import sys,os,time,re

def get_module_root():
    if(len(sys.argv)>1):
        return sys.argv[1]
    else:
        return os.getcwd()

def merge_files_into_one(files):        
    f = open("all.txt", "w")
    for file in files:
        fileOne = open(file, "r")
        f.write(fileOne.read())

def get_time_by_file(file):
    f = open(file,"r")  
    s = f.readline()
    m = re.findall( r'\d{4}\-\d{2}\-\d{2}T\d{2}\:\d{2}\:\d{2}\.\d{1,3}', s )
    if m:
        stime = m[0]
        return time.strptime(stime, "%Y-%m-%dT%H:%M:%S.%f")
    #time.strptime("2014-10-29T04:40:44.264", "%Y-%m-%dT%H:%M:%S.%f")
    return time.localtime()

def compare_file(file1, file2):
    time1 = get_time_by_file(file1)
    time2 = get_time_by_file(file2)
    if time1>time2:
        return 1
    elif time1==time2:
        return 0
    else:
        return -1
   
def sort_files_by_date(files):
    #sorted(files, cmp=compare_file)
    files.sort(compare_file)

log_root_dir = get_module_root()
os.chdir(log_root_dir)
print("current module root dir=" + log_root_dir)
if os.path.isfile("all.txt"):
    os.remove("all.txt")

file_list = []
for file in [doc for doc in os.listdir(log_root_dir) if doc.endswith(".log")]:
        file_list.append(file)

sort_files_by_date(file_list)
merge_files_into_one(file_list)