import sqlite3 

conn = sqlite3.connect("database.db")
cur = conn.cursor() 

with open('schema.sql') as fp:
    cur.executescript(fp.read()) 
