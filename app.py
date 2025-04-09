from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
import json
from datetime import datetime

app = Flask(__name__)

# Set up Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your-email-password'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

# Sample Data (You can replace this with a database)
projects = [
    {"name": "Project 1", "description": "A web app for project management", "link": "https://github.com/KLKushal/project1", "image": "project1.jpg"},
    {"name": "Project 2", "description": "An e-commerce platform", "link": "https://github.com/KLKushal/project2", "image": "project2.jpg"}
]

skills = ['HTML', 'CSS', 'JavaScript', 'Flask', 'Python']

@app.route('/')
def home():
    return render_template('index.html', name="KL Kushal", title="Web Developer", skills=skills)

@app.route('/projects')
def projects_page():
    return render_template('projects.html', projects=projects)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Send email using Flask-Mail
        msg = Message("New Contact Message", sender=email, recipients=["your-email@gmail.com"])
        msg.body = f"From: {name} <{email}>\n\n{message}"
        mail.send(msg)

        return redirect(url_for('home'))

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
