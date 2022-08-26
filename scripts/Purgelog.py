from fileinput import filename
import shutil   #for copy file
import os   # for get file size and check if file exist
import sys  # for cli arguments

if(len(sys.argv)< 4):
    print("Missing arguments! Usage is script.py")
    exit(1)
    
file_name = sys.argv[1]
limit_size = int(sys.argv[2])
logsnumber = int(sys.argv[3])

if(os.path.isfile(file_name)==True):
    logfile_size = os.stat(file_name).st_size   #Get filesize in BYTES
    logfile_size = logfile_size / 1024  #Convert from BYTES to KILLOBYTES
    
    if(logfile_size >= limit_size):
        if(logsnumber > 0):
            for currentFileNum in range(logsnumber, 1, -1):
                src = file_name + "_" + str(currentFileNum-1)
                dst = file_name + "_" + str(currentFileNum)
                if(os.path.isfile(src)==True):
                    shutil.copyfile(src, dst)
                    print("Copied: " + src + " to " + dst)
                
                shutil.copyfile(file_name, file_name + "_1")
                print("Copied: " + file_name + " to " + filename + "_1")
        myfile = open(file_name, 'w')
        myfile.close()
    