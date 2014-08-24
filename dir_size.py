#!/usr/local/bin/python3

import os, sys
'''
This script will find the files bigger than ....
v1.0
'''
def check_dir():
  try:
    folder=input("Please enter the directory name: ")
    if not os.path.exists(folder):
      raise
    else:
      return folder
  except:
    print("\n \t Error!!! Incorrect directory name \n")
    sys.exit(1)


def file_size():
  try:
    fsize=int(input("Please insert the minimal file size(MB) : "))*1024
    return fsize
  except:
     print("\n \t Error!!! The number must be integer.\n")
     sys.exit(1)


def find_files(x,y):
  print("Starting to search ..... ")
  dir_size=0
  for(path, dirs, files) in os.walk(x):
    for file in files:
      thefile=os.path.join(path,file)
      dir_size += os.path.getsize(thefile)
      if os.path.getsize(thefile) >= y :
        print("The file %s size: --> %0.2f MB" % (thefile,os.path.getsize(thefile)/(1024*1024)))
  print("\n\tThe total directory size is: %0.1f MB " % (dir_size/(1024*1024)))



if __name__ == '__main__':
  find_files(check_dir(),file_size())

