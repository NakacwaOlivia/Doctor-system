# from msilib import init_database
from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import psycopg2.extras

app = Flask(__name__)
DB_HOST = 'localhost'
DB_NAME = 'Doctor-system'
DB_USER = 'postgres'
DB_PASS = '@Wdsk5313'

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

# ENV = 'dev'

# if ENV == 'dev':
#     app.debug = True
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgresql:@Wdsk5313/Doctor-system'
# else:
#     app.debug = False
#     app.config['SQLALCHEMY_DATABASE_URI'] = ''

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# class register(db.Model):
#     __tablename__ = 'Register'
#     userName = db.Column(db.String(200), primary_key=True)
#     firstName = db.Column(db.String(200))
#     lastName = db.Column(db.String(200))
#     password = db.column(db.String(100))
#     age = db.Column(db.Integer)
#     contact = db.Column(db.Integer, unique=True)
#     email = db.Column(db.String(200), unique=True)
#     country = db.Column(db.String(200))

#     def __init__(self, firstName, lastName, password, age, contact, email, country, remote_addr=None,):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.password = password
#         self.age = age
#         self.contact = contact
#         self.email = email
#         self.country = country

#         # if remote_addr is None and has_request_context():
#         #         remote_addr = request.remote_addr
#         # self.remote_addr = remote_addr


@app.route('/')
def home():
    return render_template('index.html')


# @app.route('/login', methods=['GET'])
# def login():
#     if request.method == 'GET':
#         userName = request.form['userName']
#         password = request.form['password']

#         if userName == '' or password == '':
#             return render_template('login.html', message='Please enter required fields')
#         return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        if firstName in request.form and lastName in request.form and password in request.form and age in request.form and contact in request.form and email in request.form and country in request.form:
            firstName = request.form['firstName']
            lastName = request.form['lastName']
            password = request.form['password']
            age = request.form['age']
            contact = request.form['contact']
            email = request.form['email']
            country = request.form['country']
            print(firstName)
            print(lastName)
            print(age)
    
    return render_template('signup.html')


if __name__ == '__main__':
    app.run()
