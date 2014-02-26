#!/usr/bin/python

import cgitb
cgitb.enable()

import cgi
import sqlite3
import pickle
import datetime

postvars = cgi.FieldStorage()
connection = sqlite3.connect("messages.db")
cursor = connection.cursor()

newMessage = {"user": postvars["user"], "message": postvars["message"], "timestamp": datetime.datetime.now()}

cursor.execute("INSERT INTO messages '?';", (pickle.dumps(newMessage)))
connection.commit()
connection.close()

print("success")