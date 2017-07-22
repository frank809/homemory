#! /usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image

class filemanager(object):

    def __init__(self):
        pass

    def __del__(self):
        pass

    def tidy(self,inputfolder):
        """
        for item in inputfolder:
            if folder then recurrence.
            if jpeg files then dill with get_exifinfo() and then save info to db. id should be SHA256 of photo files.
                moveRAWfile()
                createThumbfile()
        :param inputfolder:
        :return:
        """
        pass

    def get_info(self,file):
        """

        :param file:
        :return:
        """
        shavalue=""
        createtime=""
        gps=""
        img = Image.open(file)


        return (shavalue, createtime, gps)