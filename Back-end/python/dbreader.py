import sqlite3
item = 'conjugat/db.sqlite3'
con = sqlite3.connect(item)
cur = con.cursor()
cur.execute("SELECT * FROM verbs_RomanceTense")
print(cur.fetchall())

names = list(map(lambda x: x[0], cur.description))
print(names)

#applicationName_ModelName
