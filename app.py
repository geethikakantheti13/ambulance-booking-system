from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/')
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check credentials
        if username == 'username' and password == 'ambulance@123':
            # Redirect to success page if credentials match
            return redirect(url_for('login'))
        else:
            # Redirect back to register page with error message
            return render_template('register.html', error='Invalid credentials. Please try again.')

    # Render the register.html template for GET request
    return render_template('register.html')






@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        connection = sqlite3.connect('ambulance.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM users WHERE username =? AND password = ?', (username, password))
        user = cursor.fetchone()
        connection.close()
        if user:
            return redirect(url_for('book'))
        else:
            return "Invalid credentials"
    return render_template('login.html')

@app.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        username = request.form.get('username', 'test_user')
        emergency_type = request.form.get('emergency_type', 'test_emergency')
        location = request.form.get('location', 'test_location')
        if username and emergency_type and location:
            connection = sqlite3.connect('ambulance.db')
            cursor = connection.cursor()
            cursor.execute('INSERT INTO bookings (username, emergency_type, location) VALUES (?, ?, ?)', (username, emergency_type, location))
            connection.commit()
            connection.close()
            return redirect(url_for('track', success=True))
        else:
            return "Missing form data", 400
    return render_template('book.html')

@app.route('/track')
def track():
    success = request.args.get('success')
    connection = sqlite3.connect('ambulance.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM bookings')
    bookings = cursor.fetchall()
    connection.close()
    return render_template('track.html', bookings=bookings, success=success)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

if __name__ == '__main__':
    app.run(debug=True)






















