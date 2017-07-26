#! /usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import os.path


class dbmanager(object):

    def __init__(self, db="./init.db"):
        """
        SELECT count(*) FROM sqlite_master WHERE type='table' AND name='要查询的表名';
        :param db:
        """
        if os.path.exists(db):
            self.conn = sqlite3.connect(db)
            self.dbcursor = self.conn.cursor()
            self.initphototable(True)
        else:
            os.makedirs(os.path.dirname(db))
            self.conn = sqlite3.connect(db)
            self.dbcursor = self.conn.cursor()
            self.initphototable(False)  #need create tables



    def initphototable(self,isdbexist):
        """
        CREATE TABLE photos (id string , rawfilepath string, glancefilepath string, createtime string,
         gps string, eventid string, persons string, PRIMARY KEY('id'))
        :return:
        """
        if isdbexist:  #if db exist then check table and try one select.
            pass  #todo: need verify something when db exist.
        else:
            self.dbcursor.execute("CREATE TABLE photos (id string , rawfilepath string, glancefilepath string, "
                                  "createtime string,gps string, eventid string, persons string, PRIMARY KEY('id'))")

    def initeventable(self):
        pass

    def get_photoinfo(photoid="all"):
        """
        method used for getting photo infomation. all informations include (rawfilepath, glancefilepath, createtime,
        gps, eventid, persons) would be return. param photoid is all by default. means it will return all stored file.
        :param photoid:all=get all photos informatin. specific id means get one.
        :return:
        """
        #todo: think about if too many photos and get in separate pages?
        pass

    def put_photoinfo(self, photoid, rawfilepath, glancefilepath, createtime="", gpsinfo="", eventid="", persons=""):
        """
        :param photoid:
        :param rawfilepath:
        :param glancefilepath:
        :param createtime:
        :param gpsinfo:
        :param eventid:
        :param persons:
        :return:
        """
        sqlstring="insert into photos values ('%s','%s','%s','%s','%s','%s','%s')"%(photoid,rawfilepath,glancefilepath,createtime,gpsinfo,eventid,persons)
        self.dbcursor.execute(sqlstring)
        self.conn.commit()

    def update_photoinfo(self, photoid, rawfilepath="", glancefilepath="", createtime="", gpsinfo="", eventid="", persons=""):
        """
        update photos set gpsinfo = "aaa" where photoid ="ffff";
        :param photoid:
        :param rawfilepath:
        :param glancefilepath:
        :param createtime:
        :param gpsinfo:
        :param eventid:
        :param persons:
        :return:
        """
        #todo: update some of value should be supported.
        pass

    def isphotoexist(self,filehash):
        """
        Check if photo's SHA256 have already stored in db.
        :return:
        """
        sqlstr = "select count(*) from photos where id == '%s'"%filehash;
        self.dbcursor.execute(sqlstr)
        count = self.dbcursor.fetchone()[0]
        if count == 0:
            return False
        return True

    def __del__(self):
        self.conn.close()
        pass





