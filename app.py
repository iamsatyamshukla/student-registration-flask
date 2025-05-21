from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Satyam@555'   # Your MySQL password
app.config['MYSQL_DB'] = 'student_portal'  # Use your actual DB name

mysql = MySQL(app)

# 🔹 Route 1: Home Page (form)
@app.route('/')
def index():
    return render_template('index.html')

# 🔹 Route 2: Handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        roll = request.form['roll_no']
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO students (name, email, password, roll_no) VALUES (%s, %s, %s, %s)", 
                    (name, email, password, roll))
        mysql.connection.commit()
        cur.close()

        # ✅ Redirect to student list after submission
        return redirect('/students')

# 🔹 ✅ Route 3: Display all students in a table
@app.route('/students')
def students():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()
    cursor.close()
    return render_template('students.html', students=data)

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=8000)
