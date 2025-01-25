from flask import Flask, render_template, request, session, Response, redirect, url_for, make_response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# app.secret_key = 'rushi'

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///DATA.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class WebMedConsultMaster(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(50), nullable=False)
    height = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    bloodgroup = db.Column(db.String(50), nullable=False)

    def __repr__(self) -> str:
        return f"{self.sno} {self.name} {self.phone} {self.email} {self.age} {self.gender} {self.height} {self.weight} {self.bloodgroup}"

class Appointment(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    appointment_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    doctor = db.Column(db.String(80), nullable=False)
    message = db.Column(db.String(250), nullable=False)

    def __repr__(self) -> str:
        return f"{self.sno} {self.appointment_name} {self.email} {self.doctor} {self.message}"

class Contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    message = db.Column(db.String(250), nullable=False)

    def __repr__(self) -> str:
        return f"{self.sno} {self.name} {self.email} {self.message}"

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        new_contact = Contact(name=name, email=email, message=message)
        db.session.add(new_contact)
        db.session.commit()
    return render_template('return3.html')

@app.route('/form', methods=["GET", "POST"])
def form():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        age = request.form['age']
        gender = request.form['gender']
        height = request.form['height']
        weight = request.form['weight']
        bloodgroup = request.form['bloodgroup']

        new_webmedconsult = WebMedConsultMaster(
            name=name, phone=phone, email=email, age=age, gender=gender, height=height, weight=weight, bloodgroup=bloodgroup
        )
        db.session.add(new_webmedconsult)
        db.session.commit()
        return render_template('return.html')

    return render_template('form.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/videocall')
def videocall():
    return render_template('videocall.html')

@app.route('/doctinfo1')
def doctinfo1():
    return render_template('doctinfo1.html')

@app.route('/doctinfo2')
def doctinfo2():
    return render_template('doctinfo2.html')

@app.route('/doctinfo3')
def doctinfo3():
    return render_template('doctinfo3.html')

@app.route('/docs')
def docs():
    return render_template('docs.html')

@app.route('/gmeet')
def gmeet():
    return render_template('gmeet.html')

@app.route('/appointment', methods=["GET", "POST"])
def appointment():
    if request.method == 'POST':
        appointment_name = request.form['appointment_name']
        email = request.form['email']
        doctor = request.form['doctor']
        message = request.form['message']

        new_appointment = Appointment(appointment_name=appointment_name, email=email, doctor=doctor, message=message)
        db.session.add(new_appointment)
        db.session.commit()
        return render_template('return2.html')

    return render_template('appointment.html')

if __name__ == "__main__":
    app.run(debug=True)
