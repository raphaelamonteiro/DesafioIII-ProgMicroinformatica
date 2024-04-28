from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/projects')
def projects():
     return render_template('projects.html')

@app.route('/resume')
def resume():
     return render_template('resume.html')
     
@app.route('/contacts')
def contacts():
     return render_template('resume.html')


