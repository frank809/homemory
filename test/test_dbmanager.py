#!/usr/bin/python

# -*- coding: utf-8 -*-


import dbmanager
import unittest


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_dbcreate(self):
        db = dbmanager.dbmanager.dbmanager()

    def test_put_photosinfo(self):
        db = dbmanager.dbmanager.dbmanager()
        db.put_photoinfo("fffffffffffffffff","./rawfile/f","./glancefile/path/f","2017-07-21 07:56:32","(E34,S56,443)","12,45,32","5,3,4,2")


if __name__ == '__main__':
    unittest.main()
