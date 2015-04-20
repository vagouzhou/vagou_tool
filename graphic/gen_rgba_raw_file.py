#!/usr/bin/python
#author:vagouzhou@gmail.com
#merge all dumped png files into RGBA raw data file
import sys,os,struct
from PIL import Image

def write_int_tofile(fileobj,value):
    data = struct.pack("i", value)
    fileobj.write(data)

def get_module_root():
    if(len(sys.argv)>1):
        return sys.argv[1]
    else:
        return os.getcwd()

log_root_dir = get_module_root()
os.chdir(log_root_dir)
print("current module root dir=" + log_root_dir)

file_list = []
for file in [doc for doc in os.listdir(log_root_dir) if doc.endswith(".png")]:
        file_list.append(file)
file_list.sort()

f = None
bfileopened = False
for file in file_list:
    im = Image.open(file)
    if not bfileopened:
        size = im.size
        filename = "%d_%d_%s.raw"%(size[0],size[1],im.mode)
        f = open(filename, "wb")
        f.write(im.mode)
        write_int_tofile(f,size[0])
        write_int_tofile(f,size[1])
        write_int_tofile(f,len(file_list))
        bfileopened = True
    rawdata = im.tostring()
    f.write(rawdata)
f.close()
