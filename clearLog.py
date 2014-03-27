import sqlite3
connection = sqlite3.connect("messages.db")
cursor = connection.cursor()
cursor.execute("DELETE FROM messages;")
connection.commit()
connection.close()
