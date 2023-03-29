import os
import shutil
from os import path
def main():
    if path.exists("file1.txt"):
        src = path.realpath("file.txt")    #get the path

        head,tail = path.split(src)  #seprate the path fro the filter
        print("path:" + head)
        print("file:" +tail)

        dst = src+ ".bak"      # make backup copy
        shutil.copy(src,dst)   #make a copy
        shutil.copy(src,dst)   #copy permision modification