import os

from flask import Flask, render_template, request
import db

app = Flask(__name__, instance_relative_config=True)

app.config.from_mapping(
    SELECT_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
)

try:
    os.makedirs(app.instance_path)
except OSError:
    pass


db.init_app(app)

@app.route('/')
def root():
    return render_template('home/index.html')

@app.route('/users/map/')
def map():
    return render_template('map.html')

@app.route('/users/profile/')
def profile():
    return render_template('home/profile.html')

@app.route('/login/')
def login():
    return render_template('home/login.html')

@app.route('/register/')
def register():
    return render_template('home/register.html')


# def hello_world():  # put application's code here
#     return 'Hello World!'


if __name__ == '__main__':
    app.run()

