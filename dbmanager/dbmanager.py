#! /usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3


class dbmanager(object):

    def __init__(self, db="./init.db"):
        '''
        SELECT count(*) FROM sqlite_master WHERE type='table' AND name='要查询的表名';
        :param db:
        '''
        self.conn = sqlite3.connect(db)
        self.initphototable()
        self.initeventable()

    def initphototable(self):
        '''
        CREATE TABLE photos (id string , rawfilepath string, glancefilepath string, createtime string,
         gps string, eventid string, persons string, PRIMARY KEY('id'))
        :return:
        '''
        pass

    def initeventable(self):
        pass

    def get_photoinfo(self, photoid="all"):
        '''
        method used for getting photo infomation. all informations include (rawfilepath, glancefilepath, createtime,
        gps, eventid, persons) would be return. param photoid is all by default. means it will return all stored file.
        TODO: think about if too many photos and get in separate pages?
        :param photoid:all=get all photos informatin. specific id means get one.
        :return:
        '''
        pass

    def put_photoinfo(self, photoid, rawfilepath, glancefilepath, createtime="", gpsinfo="", eventid="", persons=""):
        '''
        :param photoid:
        :param rawfilepath:
        :param glancefilepath:
        :param createtime:
        :param gpsinfo:
        :param eventid:
        :param persons:
        :return:
        '''
        pass

    def update_photoinfo(self, photoid, rawfilepath="", glancefilepath="", createtime="", gpsinfo="", eventid="", persons=""):
        '''

        :param photoid:
        :param rawfilepath:
        :param glancefilepath:
        :param createtime:
        :param gpsinfo:
        :param eventid:
        :param persons:
        :return:
        '''
        pass

    def __del__(self):
        pass





