import sqlite3

DATABASE = 'ambulance_booking_system.db'

def initialize_db():
    with open('initialize_db.sql', 'r') as f:
        sql_script = f.read()

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.executescript(sql_script)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    initialize_db()
