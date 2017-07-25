#! /usr/bin/python
# -*- coding: utf-8 -*-

import os.path
import photo
from dbmanager.dbmanager import dbmanager
import hashlib
import shutil

#set some global path for file
ROOTPATH="./memory/"



class filemanager(object):

    def __init__(self):
        #need dbmanager instance and filemanager instance.
        self.filedb = dbmanager()
        pass

    def __del__(self):
        pass

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
        for item in os.listdir(inputfolder):
            itemwithpath=inputfolder + os.sep + item
            if os.path.isdir(itemwithpath):
                self.tidy(itemwithpath)
            else:
                if self.needtidy(itemwithpath):
                    fileinfo = self.get_info(itemwithpath)
                    self.movefiletoraw(itemwithpath)
                    self.createthumbfile(itemwithpath)
                    self.filedb.put_photoinfo(fileinfo["hash"], ROOTPATH+os.sep+"raw"+os.sep+itemwithpath, ROOTPATH+os.sep+"thumb"+os.sep+itemwithpath, fileinfo["createtime"], fileinfo["gps"])

    def get_info(self, file):
        """
        if new file type should be supported. new class should be create and then add function entry here.
        :param file:
        :return:
        """
        filename, ext = os.path.splitext(file)
        fileinfo =""

        #handle JPEG file.
        if ext.upper() == ".JPG" or ext.upper() == ".JPEG":
            jpegfile = photo.photo() #init one photo instance. todo: check if this init can be in __init__
            jpeginfo = jpegfile.getfromjpeg(file)
            fileinfo = jpeginfo
        return fileinfo

    def needtidy(self, file):
        hashvalue = hashlib.sha256(file).hexdigest()
        return not self.filedb.isphotoexist(hashvalue)

    def movefiletoraw(self, file):
        #default pat for raw is ROOTPATH+os.sep+"raw". should use
        if not os.path.exists(ROOTPATH+os.sep+"raw"):
            os.makedirs(ROOTPATH+os.sep+"raw")
            shutil.move(file, ROOTPATH+os.sep+"raw"+os.sep+hashlib.sha256(file).hexdigest())

    def createthumbfile(self,file):
        #default folder for thumbnail is ROOTPATH+os.sep+"thumb"
        pass