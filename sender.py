#!/usr/bin/python

import cgitb
cgitb.enable()

import cgi

postvars = cgi.FieldStorage()
connection = sqlite3.connect("messages.db")
cursor = connection.cursor()

newMessage = Message(postvars["user"], postvars["message"], datetime.datetime.now())

cursor.execute("INSERT INTO messages '{}'".format(pickle.dumps(newMessage)))
connection.commit()
connection.close()