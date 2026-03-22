# ------------------------------------------------------
# -- Databases => SQLite => Insert Data Into Database --
# ------------------------------------------------------
# - cursor => All Operation in SQL Done By Cursor Not The Connection Itself
# - commit => Save All Changes
# ------------------------------------------------------

# Import SQLite Module
import sqlite3

# Create Database And Connect
db = sqlite3.connect("App.db")
# Setting Up The Cursor
cr = db.cursor()
# Create The Tables and Fields
cr.execute("create table if not exists users(user_id integer,name text)")
cr.execute(
    "create table if not exists skills (name text, progress integer, user_id integer)")
# Inserting Data
# cr.execute("insert into users values (1,'ahmad')")
# cr.execute("insert into users values (2,'ali')")
# cr.execute("insert into users values (3,'akram')")
# cr.execute("insert into users(user_id, name) values(3, 'Osama')")
my_list = ["Ahmed", "Sayed", "Mahmoud", "Ali", "Kamel", "Ibrahim", "Enas"]
for key, user in enumerate(my_list, 1):
    cr.execute(f"insert into users(user_id, name) values({key},'{user}')")
# Save(Commit) Changes
db.commit()
# Close Database
db.close()
