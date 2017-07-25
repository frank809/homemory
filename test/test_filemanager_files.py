#! /usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from filemanager.files import filemanager

file = "./resource/test.jpg"

class TestStringMethods(unittest.TestCase):

    def test_getinfo(self):
        tt = filemanager()
        jpginfo=tt.get_info(file)

if __name__ == '__main__':
    unittest.main()
