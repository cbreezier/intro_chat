#!/usr/bin/python

import cgitb
# cgitb.enable()

import cgi
import sqlite3
import datetime
import pickle
import json

postvars = cgi.FieldStorage()
connection = sqlite3.connect("messages.db")
cursor = connection.cursor()

posted = {"message_time": "04:20:18 24/03/12"}

returnedMessages = []
dateTimeFormat = "%I:%M:%S %d/%m/%y"
for object in cursor.execute("SELECT object FROM messages"):
    print("object is {}".format(object))
    message = pickle.loads(object[0])
    print("message is" + str(message))
    if message["timestamp"] > datetime.datetime.strptime(posted["message_time"], dateTimeFormat):
        message["message_time"] = message["timestamp"].strftime(dateTimeFormat)
        message.pop("timestamp")
        returnedMessages.append(message)

connection.close()

print("Content-type: text/plain\n")
print(json.dumps(returnedMessages))


