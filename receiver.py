#!/usr/bin/python

import cgitb
cgitb.enable()

import cgi
import sqlite3
import pickle
import datetime
import time

postvars = cgi.FieldStorage()
# open("debug2.txt", "w").write(str(postvars))
# postvars = {}
connection = sqlite3.connect("messages.db")
cursor = connection.cursor()

# postvars["user"] = "test"
# postvars["message"] = "test"
newMessage = {"user": postvars["user"].value, "message": postvars["message"].value, "timestamp": datetime.datetime.now()}
cursor.execute("INSERT INTO messages VALUES(?);", (pickle.dumps(newMessage),))

time.sleep(0.1) # to get greater timestamp
newMessage2 = {"user": "pythonbot", "message": "%s is a retard" % postvars["user"].value, "timestamp": datetime.datetime.now()}
cursor.execute("INSERT INTO messages VALUES(?);", (pickle.dumps(newMessage2),))

connection.commit()
connection.close()

print("Content-type:text/plain\n")
print("success")
