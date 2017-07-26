#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os.path
import filemanager.files


def main():
    # check if argv[1] should be folder.
    if len(sys.argv) == 2:
        inputfolder = sys.argv[1]
        if os.path.exists(inputfolder):
            fileman = filemanager.files.filemanager()
            fileman.tidy(inputfolder)
        else:
            print "Error. Can't find input folder:%s"%inputfolder
    else:
        print "Error. please give only one param: input folder."

main()
