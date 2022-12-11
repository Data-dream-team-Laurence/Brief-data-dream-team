from flask import Flask, render_template
from app.dash_application import create_dash_application
# app.config.from_object('config')

app = Flask(__name__)
create_dash_application(app)

@app.route('/')
def index():
   
   return render_template('index.html')

@app.route('/about')
def about():
   return render_template('about.html')



