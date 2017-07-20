#! /usr/bin python
# -*- coding: utf-8 -*-

import sqlite3

class dbmanager(object):

    def __init__(self,db="./init.db"):
        self.conn = sqlite3.connect(db)


