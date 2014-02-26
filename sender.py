#!/usr/bin/python

import cgitb
cgitb.enable()

import cgi
import sqlite3
import datetime
import pickle
import json

postvars = cgi.FieldStorage()
connection = sqlite3.connect("messages.db")
cursor = connection.cursor()

returnedMessages = []
dateTimeFormat = "%I:%M:%S %d/%m/%y"
for object in cursor.execute("SELECT object FROM messages"):
    message = pickle.loads(object[0])
    if not postvars["message_time"] or message["timestamp"] > datetime.datetime.strptime(postvars["message_time"].value, dateTimeFormat):
        message["message_time"] = message["timestamp"].strftime(dateTimeFormat)
        message.pop("timestamp")
        returnedMessages.append(message)

connection.close()

print("Content-type:text/plain\n")
print(json.dumps(returnedMessages))


