#!/usr/bin/python

# -*- coding: utf-8 -*-


import dbmanager
import unittest


class TestStringMethods(unittest.TestCase):

    def test_dbcreate(self):
        dbs = dbmanager.dbmanager.dbmanager()

    def test_put_photosinfo(self):
        db = dbmanager.dbmanager.dbmanager("./memory/init.db")
        db.put_photoinfo("fffffffffffffffff", "./rawfile/f", "./glancefile/path/f", "2017-07-21 07:56:32", "(E34,S56,443)","12,45,32","5,3,4,2")

    def test_photoexit(self):
        db = dbmanager.dbmanager.dbmanager("./memory/init.db")
        db.isphotoexist("fffffffffffffffff")
        print("done")


if __name__ == '__main__':
    unittest.main()
