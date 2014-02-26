#!/usr/bin/python2.7

import cgitb
cgitb.enable()

import cgi
import sqlite3
import datetime
import pickle
import json

postvars = cgi.FieldStorage()
# open("debug.txt", "w").write(str(postvars))
connection = sqlite3.connect("messages.db")
cursor = connection.cursor()

returnedMessages = []
dateTimeFormat = "%I:%M:%S %d/%m/%y"
for object in cursor.execute("SELECT object FROM messages"):
    message = pickle.loads(str(object[0]))
    if not "last_message" in postvars or message["timestamp"] > datetime.datetime.strptime(postvars["last_message"], dateTimeFormat):
        message["message_time"] = message["timestamp"].strftime(dateTimeFormat)
        message.pop("timestamp")
        returnedMessages.append(message)

connection.close()

print("Content-type:text/plain\n")
print(returnedMessages)
print(json.dumps(returnedMessages))


