from flask import Flask, redirect, request, render_template, url_for
import mysql.connector

app = Flask(__name__)

# MySQL connection setup
def get_db_connection():
    print("Connecting to database...")  # Debug message
    conn = mysql.connector.connect(
        host='localhost',  # Use localhost if you're running MySQL on your local machine
        user='root',
        password='password',
        database='test_db'
    )
    print("Connected to database.")  # Debug message
    return conn

@app.route('/')
def index():
    print("Rendering index page...")  # Debug message
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    fname = request.form['fname']
    lname = request.form['lname']
    print(f"Received form data: {fname}, {lname}")  # Debug message
    
    # Insert data into MySQL
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (first_name, last_name) VALUES (%s, %s)", (fname, lname))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('records'))
 
    

@app.route('/records')
def records():
    # Fetch all records from the 'users' table
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    records = cursor.fetchall()  # Fetch all records
    cursor.close()
    conn.close()

    # Render the records in the 'records.html' template
    return render_template('records.html', records=records)

if __name__ == '__main__':
    print("Starting the Flask app...")  # Debug message
    app.run(debug=True, host='0.0.0.0', port=5000)
