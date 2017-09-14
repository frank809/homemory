#! /usr/bin/python
# -*- coding: utf-8 -*-

import os.path
from . import photo
from dbmanager.dbmanager import dbmanager
import hashlib
import shutil

#set some global path for file
ROOTPATH=".%smemory" % os.sep

#!This should be all use lowercase for externation name.
supportimagetypeext=['.jpg', '.jpeg']



class filemanager(object):

    def __init__(self):
        #need dbmanager instance and filemanager instance.
        self.filedb = dbmanager(ROOTPATH+os.sep+"init.db")
        pass

    def __del__(self):
        pass

    def __sha256(self,file):
        f=open(file, 'rb')
        hashvalue = hashlib.sha256(f.read()).hexdigest()
        f.close()
        return hashvalue

    def tidy(self, inputfolder):
        """
        for item in inputfolder:
            if folder then recurrence.
            if files then check if dbexist. if no get_info() and then save info to db. id should be SHA256 of photo files.
                moveRAWfile()
                createThumbfile()
        :param inputfolder:
        :return:
        """
        #for create one html.
        temp_htmlstrings = "<html><title>Photo review for test</title><body>"


        print("Tidy folder:%s" % inputfolder)
        for item in os.listdir(inputfolder):
            itemwithpath=inputfolder + os.sep + item
            if os.path.isdir(itemwithpath):
                self.tidy(itemwithpath)
            else:
                filehashvalue = ""# if tidy needed then print SHA256 also. this variable only used in print.
                if self.needtidy(itemwithpath):
                    fileinfo = self.get_info(itemwithpath)

                    #file should be createthumbfile firest then move it into raw. otherwise createthumbfile can't find file.
                    #self.createthumbfile(itemwithpath)
                    #self.movefiletoraw(itemwithpath)

                    filename, ext = os.path.splitext(itemwithpath)
                    itemhash = fileinfo["hash"]
                    filehashvalue=itemhash

                    self.filedb.put_photoinfo(fileinfo["hash"], "raw"+os.sep+itemhash+ext, "thumb"+os.sep+itemhash+ext, fileinfo["createtime"], fileinfo["gps"])

                    # for html test
                    temp_htmlstrings+="<img src=\"%s\"/>" % ("thumb"+os.sep+itemhash+ext)

                print("Tidy file[%s]:%s" % (filehashvalue, itemwithpath))

        #for html test:
        temp_htmlfile = open(ROOTPATH+'/photo.html', 'w+')
        temp_htmlfile.write(temp_htmlstrings)
        temp_htmlfile.flush()
        temp_htmlfile.close()


    def get_info(self, file):
        """
        if new file type should be supported. new class should be create and then add function entry here.
        :param file:
        :return:
        """
        filename, ext = os.path.splitext(file)
        fileinfo ={"hash": "", "createtime": "", "gps": ""}

        #handle JPEG file.
        if ext.upper() == ".JPG" or ext.upper() == ".JPEG":
            jpegfile = photo.photo() #init one photo instance. todo: check if this init can be in __init__
            jpeginfo = jpegfile.getfromjpeg(file)
            fileinfo = jpeginfo
            self.createthumbfile(file)
            self.movefiletoraw(file)
        return fileinfo

    def needtidy(self, file):
        filename, ext = os.path.splitext(file)
        if ext.lower() not in supportimagetypeext:
            return False
        hashvalue = self.__sha256(file)
        return not self.filedb.isphotoexist(hashvalue)

    def movefiletoraw(self, file):
        #default pat for raw is ROOTPATH+os.sep+"raw". should use
        filename, ext = os.path.splitext(file)
        if not os.path.exists(ROOTPATH+os.sep+"raw"):
            os.makedirs(ROOTPATH+os.sep+"raw")
        shutil.move(file, ROOTPATH+os.sep+"raw"+os.sep+self.__sha256(file)+ext)

    def createthumbfile(self, file):
        #default folder for thumbnail is ROOTPATH+os.sep+"thumb"
        filename, ext = os.path.splitext(file)

        # handle JPEG file.
        if ext.upper() == ".JPG" or ext.upper() == ".JPEG":
            jpegfile = photo.photo()  # init one photo instance. todo: check if this init can be in __init__
            jpegfile.createthumb(file, ROOTPATH+os.sep+"thumb")
            return True
        return False
