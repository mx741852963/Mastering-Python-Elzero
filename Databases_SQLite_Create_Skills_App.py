# Databases – SQLite Create Skills App

import sqlite3

database = sqlite3.connect("App_Skill.db")
cursor = database.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Users (name text, user_id integer)")
cursor.execute(
    "CREATE TABLE IF NOT EXISTS skills (name text, progress integer,user_id integer)"
)

# My User I_d
u_id = 1

# Input Main Message
input_message = """ What Do You Want To Do ?
"s" => Show All Skills
"a" => Add New Skill
"d" => Delete Skill
"u" => Update Skill Progress
"q" => Quit The Application
Choose Option:
"""
user_input = input(input_message).strip().lower()


# Define The Methods
def save_and_commit():
    database.commit()
    database.close()
    print("Database Saved And Closed")


def show_skills():
    cursor.execute("select * from skills where user_id = ?", (u_id,))
    results = cursor.fetchall()
    print(f"You have {len(results)} Skills")
    if len(results) > 0:
        for row in results:
            print(f"Skill Name: {row[0]}, Progress: {row[1]}%")
    save_and_commit()


def add_skill():
    skill_name = input("Enter Skill Name : ").strip().capitalize()
    cursor.execute(
        "select name from skills where name =? and user_id = ? ", (skill_name, u_id)
    )
    results = cursor.fetchone()
    if results is None:
        skill_progress = input("Enter  Skill Progress : ").strip().capitalize()
        cursor.execute(
            "insert into skills(name, progress, user_id) values(?, ?, ?)",
            (skill_name, skill_progress, u_id),
        )
    else:
        print("Skill Already Exists")
    save_and_commit()


def delete_skill():
    skill_name = input("Enter Skill Name : ").strip().capitalize()
    cursor.execute(
        "DELETE FROM skills WHERE name = ? AND user_id = ?", (skill_name, u_id)
    )
    save_and_commit()


def update_skill():
    skill_name = input("Enter Skill Name : ").strip().capitalize()
    skill_progress = input("Enter  New Skill Progress : ").strip().capitalize()
    cursor.execute(
        "update skills set progress = ? where name = ? and user_id = ?",
        (skill_progress, skill_name, u_id),
    )
    save_and_commit()


def quit_skill():
    print("Quit")
    save_and_commit()


# Command List
match user_input:
    case "s":
        show_skills()
    case "a":
        add_skill()
    case "d":
        delete_skill()
    case "u":
        update_skill()
    case "q":
        quit_skill()
    case _:
        print("Invalid Input")
        save_and_commit()
