# ---------------------------------------------------------
# -- Databases => SQLite => Very Important Information's --
# ---------------------------------------------------------

# Import SQLite Module
import sqlite3

# Create Database And Connect
db = sqlite3.connect("App_Skill.db")

# Setting Up The Cursor
cr = db.cursor()

# my_tuple = ('Pascal', '65', 8)

# Inserting Data
# cr.execute("insert into skills values(?, ?, ?)", my_tuple)

# Fetch Data From Database
# cr.execute("select * from skills order by user_id desc")
# cr.execute("select * from skills order by user_id asc")
# cr.execute("select * from skills order by name desc")
# cr.execute("select * from skills order by name limit 2")
# cr.execute("select * from skills order by name limit 3 offset 2")
# cr.execute("select * from skills where user_id > 0")
# cr.execute("select * from skills where user_id not in(1, 2, 3)")
cr.execute("select * from skills where user_id  in(1, 2, 3)")

# Assign Data To Variable
results = cr.fetchall()

# Loop On Results
for row in results:
    print(f"Skill Name => {row[0]},", end=" ")
    print(f"Skill Progress => {row[1]},", end=" ")
    print(f"User ID => {row[2]}")

# Save (Commit) Changes
db.commit()

# Close Database
db.close()
