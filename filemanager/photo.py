#! /usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image

class photo (object):

    def __init__(self):
        pass

    def getfromjpeg(self,file):
        """
        获取jpeg文件的exif信息。只需要返回sha256值，创建时间，GPS信息构成的字典
        :param file:
        :return:
        """
        pass

    def createthumb(self, file, outputfolder):
        """
        创建文件对应的thumb文件。并存放都某个特定目录
        :param file:
        :return:
        """
        pass