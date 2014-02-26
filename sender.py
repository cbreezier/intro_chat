#!/usr/bin/python

import cgitb
cgitb.enable()

import cgi

postvars = cgi.FieldStorage()
connection = sqlite3.connect("messages.db")
cursor = connection.cursor()



cursor.execute("SELECT object FROM messages {}".format()
connection.close()

