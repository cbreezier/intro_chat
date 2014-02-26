#!/usr/bin/python

import cgi
import sqlite3
import pickle
import datetime

class Message(object):
    def __init__(self, user, message, time):
        self.user = user
        self.message = message
        self.time = time

postvars = cgi.FieldStorage()
connection = sqlite3.connect("messages.db")
cursor = connection.cursor()

newMessage = Message(postvars["user"], postvars["message"], datetime.datetime.now())

cursor.execute("INSERT INTO messages '%s'" % (pickle.dumps(newMessage)))
connection.commit()
connection.close()

print("success")