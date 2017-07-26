#! /usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from filemanager.files import filemanager, ROOTPATH
import os.path
import hashlib
import shutil

file = "./resource/test.jpg"


class TestStringMethods(unittest.TestCase):

    def test_getinfo(self):
        tt = filemanager()
        jpginfo=tt.get_info(file)

    def test_movefiletoraw(self):
        filemove = "./resource/testmove.jpg"
        shutil.copy(file, filemove)
        tt = filemanager()
        tt.movefiletoraw(filemove)
        hasvalue = hashlib.sha256(filemove).hexdigest()
        self.assertTrue(os.path.exists(ROOTPATH+os.sep+"raw"+os.sep+hasvalue+".jpg"))
        shutil.rmtree(ROOTPATH+os.sep+"raw")

    def test_createthumbfile(self):
        tt = filemanager()
        tt.createthumbfile(file)
        hasvalue = hashlib.sha256(file).hexdigest()
        self.assertTrue(os.path.exists(ROOTPATH+os.sep+"thumb"+os.sep+hasvalue+".jpg"))
        shutil.rmtree(ROOTPATH + os.sep + "thumb")

    def test_tidy(self):
        tt = filemanager()
        tt.tidy("./resource")


if __name__ == '__main__':
    unittest.main()
