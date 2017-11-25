#!/usr/bin/env python
import os
import time
import sys
import stat
import shutil





#Using the os module to get information about a file
def dump(file):
    print ("stat", file)
    st = os.stat(file)
    mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime = st
    print ("- size:", size, "bytes")
    print ("- owner:", uid, gid)
    print ("- created:", time.ctime(ctime))
    print ( "- last accessed:", time.ctime(atime))
    print ("- last modified:", time.ctime(mtime))
    print ("- mode:", oct(mode))
    print ("- inode/dev:", ino, dev)

#change current directory
def chdir(directory):
    print("Current directory:")
    cwd = os.getcwd()
    print (cwd)
    os.chdir(directory)
    cwd = os.getcwd()
    print("Changed directory:")
    print (cwd)
    

#display current directory
def cudir():
    print("Current directory:")
    cwd = os.getcwd()
    print(cwd)

#Directory changed to parent directory
def pdir():
    print("Directory changed")
    os.chdir(os.pardir)
    print (os.getcwd())

#list elements of directory
def ldir(directory):
    print("Elements of directory:" +directory)
    for file in os.listdir(directory):
        print (file)

#used to list directory elements

def fc(directory):
    os.chdir(directory)

#create directory
def mkd(directory):
    os.mkdir(directory)
    print (directory + " CREATED")

#delete directory 
def dld(directory):
    os.rmdir(directory)
    print( directory + " deleted")


#Return the real group id of the current process.
def rgid():
    
    print( os.getgid() )
 

#return the current process’s user id.
def uid():
     # id=os.getuid()
    print( os.getuid())

#Returns the real process ID of the current process.
def rpid():

    print( os.getpid())
    return  

#Return information identifying the current operating system.
def cos():
    print(os.uname())

#delete file
def df(file):
    os.remove(file)
    print(file+" deleted")
    return


#specifies OS type
def oname():
    print("OS name is "+os.name)
    return

#used to nename text files 
def rname(filename,newname):
    os.rename(filename,newname)
    print(filename + " renamed to "+ newname)
    return

def help():
    print(" dump(file) \n chdir(directory) \n cudir()  \n pdir()  \n ldir(directory) \n ldir() \n fc(directory) \n mkd(directory) \n dld(directory) \n rgid() \n uid(): \n rpid() \n cos() \n df(file) \n oname() \n rname(filename,newname)")




