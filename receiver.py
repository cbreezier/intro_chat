#!/usr/bin/python2.7

import cgitb
cgitb.enable()

import cgi
import sqlite3
import pickle
import datetime
import time
import os
import subprocess

postvars = cgi.FieldStorage()
# open("debug2.txt", "w").write(str(postvars))
# postvars = {}
connection = sqlite3.connect("messages.db")
cursor = connection.cursor()

# postvars["user"] = "test"
# postvars["message"] = "test"
newMessage = {"user": postvars["user"].value, "message": postvars["message"].value, "timestamp": datetime.datetime.now()}
cursor.execute("INSERT INTO messages VALUES(?);", (pickle.dumps(newMessage),))
connection.commit()
connection.close()

time.sleep(0.5) # bot delay

botdir = "group_chatbots"
for botname in os.listdir(botdir):
    botpath = os.path.join(botdir, botname)
    program = subprocess.Popen(["python", botpath], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    program.stdin.write("{}:{}".format(postvars["user"].value, postvars["message"].value))
    stdout, stderr = program.communicate()

    connection = sqlite3.connect("messages.db")
    cursor = connection.cursor()
    newMessage2 = {"user": botname, "message": stdout, "timestamp": datetime.datetime.now()}
    cursor.execute("INSERT INTO messages VALUES(?);", (pickle.dumps(newMessage2),))

    connection.commit()
    connection.close()

print("Content-type:text/plain\n")
print("success")
