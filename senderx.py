#!/usr/bin/python2.7

import cgitb
cgitb.enable()

import cgi
import sqlite3
import datetime
import pickle
import json
import time

postvars = cgi.FieldStorage()
# postvars = {}
# open("debug.txt", "w").write(str(postvars))
connection = sqlite3.connect("messages.db")
cursor = connection.cursor()

slept = 0

returnedMessages = []

while not returnedMessages and slept < 50:
    dateTimeFormat = "%H:%M:%S.%f %d/%m/%y"
    for object in cursor.execute("SELECT object FROM messages"):
        message = pickle.loads(str(object[0]))
        if not "last_message" in postvars or message["timestamp"] > datetime.datetime.strptime(postvars["last_message"].value, dateTimeFormat):
            message["message_time"] = message["timestamp"].strftime(dateTimeFormat)
            message.pop("timestamp")
            returnedMessages.append(message)
    time.sleep(0.1)
    slept += 1

connection.close()

print("Content-type:text/plain\n")
print(json.dumps(returnedMessages))


