#! /usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image
import hashlib
import os

class photo (object):

    def __init__(self):
        pass

    def getfromjpeg(self,file):
        """
        get the EXIF informations (Create time, hash value(SHA256), GPS informations include attitude.
        :param file:
        :return:
        """
        photofile = Image.open(file, 'r')
        exifinfo = photofile._getexif()

        #get photo create time
        try:
            createtime = exifinfo[0x9003]
        except:
            createtime = ""

        try:
            #get photo GPS, 0x8825 is GPS informations in EXIF format.
            #GPS information used like "N:36,46,5133327;E:104,36,458898;438".
            latitude = "%s:%s,%s,%s" % (exifinfo[0x8825][1], exifinfo[0x8825][2][0][0], exifinfo[0x8825][2][1][0], exifinfo[0x8825][2][2][0])
            longitude = "%s:%s,%s,%s" % (exifinfo[0x8825][3], exifinfo[0x8825][4][0][0], exifinfo[0x8825][4][1][0], exifinfo[0x8825][4][2][0])
            attitude = exifinfo[0x8825][6][0]

            GPSinfo = "%s;%s;%s" % (latitude, longitude, attitude)
        except:
            GPSinfo = ""

        #get hash value of file
        hashvalue = hashlib.sha256(file).hexdigest()

        return {"hash": hashvalue, "createtime": createtime, "gps": GPSinfo}


    def createthumb(self, file, outputfolder):
        """
        Create thumbnail file and store it in outputfolder.  thumbnail file should not greater 500X500.
        :param file:
        :return:
        """
        size = 500, 500
        hashvalue = hashlib.sha256(file).hexdigest()
        photofile = Image.open(file, 'r')
        photofile.thumbnail(size)
        if not os.path.exists(outputfolder):
            os.makedirs(outputfolder)
        photofile.save(outputfolder+os.sep+hashvalue+'.jpg', "JPEG")
