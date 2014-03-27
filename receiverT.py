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

botname = postvars["botname"]
message = json.loads(postvars["messages"])

time.sleep(0.5) # bot delay

botdir = "text_game"
botpath = os.path.join(botdir, botname)
program = subprocess.Popen(["python", botpath], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

results = []
for message in messages:
    program.stdin.write(message)
    stdout, stderr = program.communicate()
    results.append(stdout)

    connection.commit()
    connection.close()

print("Content-type:text/plain\n")
print(results[-1])
