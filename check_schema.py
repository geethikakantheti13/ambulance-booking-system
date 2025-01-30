import sqlite3

DATABASE = 'database.db'

def check_schema():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        
        # Check if 'users' table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users';")
        table_exists = cursor.fetchone()
        if table_exists:
            print("Table 'users' exists.")
        else:
            print("Table 'users' does not exist.")
            return
        
        # Check columns in 'users' table
        cursor.execute("PRAGMA table_info(users);")
        columns = cursor.fetchall()
        
        expected_columns = {'username', 'password'}
        actual_columns = {col[1] for col in columns}  # Column names are in the second index

        if expected_columns.issubset(actual_columns):
            print("Columns in 'users' table are correct.")
        else:
            missing_columns = expected_columns - actual_columns
            print("Missing columns in 'users' table:", missing_columns)

if __name__ == '__main__':
    check_schema()
