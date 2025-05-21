# 📝 Student Registration Web App

A simple **Flask + MySQL** web application that allows students to register via a web form. The submitted data is stored in a MySQL database and displayed in a table.

---

## 🚀 Features

- 📋 Student registration form (HTML, CSS, JS)
- 🧠 Backend powered by Python Flask
- 🗃️ Data stored in MySQL database
- 📊 View all registered student entries
- 🔐 Form validation using JavaScript
- 🎨 Styled using Bootstrap

---

## 📷 Screenshot

![Student Registration Form](https://github.com/iamsatyamshukla/student-registration-flask/blob/main/form-screenshot.png.png?raw=true)


---

## 📁 Project Structure

student-registration/
│
├── static/
│ └── style.css
├── templates/
│ └── index.html
│ └── students.html
├── app.py
├── config.py (optional)
├── requirements.txt
└── README.md


---

## 🛠️ Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/student-registration-flask.git
   cd student-registration-flask

2. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate

3. Install dependencies:
   pip install flask flask-mysqldb
   
4. Update your MySQL database credentials in app.py
   
5. Run the Flask server:
   python app.py

6. Open your browser:
   http://127.0.0.1:5000/
---

🧾 Requirements
*Python 3.x
*Flask
*Flask-MySQLdb
*MySQL Server

Install with:
pip install -r requirements.txt

📦 Deployment Ideas
You can deploy this app on:
*Render
*PythonAnywhere
*Heroku (needs configuration)

📄 License
This project is open-source and free to use for learning purposes.
