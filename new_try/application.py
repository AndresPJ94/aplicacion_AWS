from flask import Flask, render_template, request, session
import pandas as pd
import os
from werkzeug.utils import secure_filename


 
app = Flask(__name__)

 
 
@app.route('/')
def index():
    return render_template('index.html')

 
