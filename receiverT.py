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
import json

postvars = cgi.FieldStorage()

botname = postvars["botname"].value

print ("Content-type:text/plain\n")
print botname
print postvars["messages"].value
x = json.loads(postvars["messages"].value)
print x


messages = json.loads(postvars["messages"].value)



botdir = "text_game"
botpath = os.path.join(botdir, botname)
program = subprocess.Popen(["python", botpath], stdin=subprocess.PIPE, stdout=subprocess.PIPE)


results = []
stdout = program.stdout.readline()
results.append(stdout)
print stdout
exit()

for message in messages:
    program.stdin.write(message)
    stdout, stderr = program.communicate()
    results.append(stdout)




print("Content-type:text/plain\n")
print(results[-1])
