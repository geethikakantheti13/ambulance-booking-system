-- Initialize the users table
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT NOT NULL
);

-- Initialize the bookings table
CREATE TABLE IF NOT EXISTS bookings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    emergency_type TEXT NOT NULL,
    location TEXT NOT NULL,
    FOREIGN KEY (username) REFERENCES users (username)
);
