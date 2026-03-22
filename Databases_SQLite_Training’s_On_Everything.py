# Databases – SQLite Training’s On Everything
import sqlite3


def get_all_data():
    db = None
    try:
        db = sqlite3.connect("App.db")
        print("Connected to database\n     Successfully ")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users")
        result = cursor.fetchall()
        print(f"Data Row in  Database: {len(result)}")
        print("Showing all data")
        for row in result:
            print(f"Name is {row[1]} and User ID is {row[0]}")
    except sqlite3.Error as error:
        print(f"Error {error}")
    finally:
        if db:
            db.close()
            print("Database closed")


get_all_data()
