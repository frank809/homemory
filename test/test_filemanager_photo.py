#! /usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from filemanager.photo import photo
import os.path

file = "./resource/test.jpg"

class TestStringMethods(unittest.TestCase):

    def test_getfromjpeg(self):
        photoguy = photo()
        info = photoguy.getfromjpeg(file)
        self.assertEqual("8996e81ff088d052c38d56241b2df7a15cb96a75d25d850946d6baba6f5a23bd",info["hash"])
        self.assertEqual("2017:02:25 16:09:26", info["createtime"])
        self.assertEqual("N:30,46,513327;E:104,36,458898;438", info["gps"])

    def test_createthumbnail(self):
        photoguy = photo()
        outfolder= "./temp/a"
        photoguy.createthumb(file, outfolder)
        self.assertTrue(os.path.exists(outfolder+'/8996e81ff088d052c38d56241b2df7a15cb96a75d25d850946d6baba6f5a23bd.jpg'))


if __name__ == '__main__':
    unittest.main()
