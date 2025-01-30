import sqlite3

DATABASE = 'database.db'

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        with open('initialize_db.sql', 'r') as f:
            cursor.executescript(f.read())
        print("Database initialized with default user and tables created.")

if __name__ == '__main__':
    init_db()
