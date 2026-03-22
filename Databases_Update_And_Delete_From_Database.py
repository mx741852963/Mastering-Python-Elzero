# ----------------------------------------------
# -- Databases => SQLite => Update and Delete --
# ----------------------------------------------
import sqlite3

db = sqlite3.connect("App.db")
cr = db.cursor()
# Update
cr.execute("update users set name = 'Gamal' where user_id = 1")
cr.execute("update users set name = 'Karem' where user_id = 2")
cr.execute("update users set name = 'Malak' where user_id = 3")
# Delete
cr.execute("delete from users where user_id = 4")
cr.execute("select * from users")
print(cr.fetchone())
print(cr.fetchone())
print(cr.fetchone())
print(cr.fetchone())
db.commit()
db.close()
