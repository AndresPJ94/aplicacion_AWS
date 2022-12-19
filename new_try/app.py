from flask import Flask,Blueprint,render_template,request,session

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from werkzeug.utils import secure_filename


model = pd.read_pickle("model/model.model") 
# Define folder to save uploaded files to process further
UPLOAD_FOLDER = os.path.join('static')
 
# Define allowed files (for this example I want only csv file)
ALLOWED_EXTENSIONS = {'csv'}
 
app = Flask(__name__, template_folder='templates', static_folder='static')
# Configure upload file path flask
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
 
# Define secret key to enable session
app.secret_key = 'This is your secret key to utilize session in Flask'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict")
def show_pred():
    pred=model.predict(steps=30)
    pred=pd.DataFrame(pred)

    fig, ax = plt.subplots(figsize=(10, 3))
    graph=pred.plot(linewidth=2, label='predicción', ax=ax)
    ax.set_title('Predicción')
    ax.legend()
    fig.savefig("./static/my_plot.png");


    return render_template("predict.html",tables=[pred.to_html(classes="data")],titles=pred.columns.values)

@app.route("/update")
def update():
    return render_template("update.html")

@app.route('/upload',  methods=("POST", "GET"))
def uploadFile():
    if request.method == 'POST':
        # upload file flask
        uploaded_df = request.files['uploaded-file']
 
        # Extracting uploaded data file name
        data_filename = secure_filename(uploaded_df.filename)
 
        # flask upload file to database (defined uploaded folder in static path)
        uploaded_df.save(os.path.join(app.config['UPLOAD_FOLDER'], data_filename))
 
        # Storing uploaded file path in flask session
        session['uploaded_data_file_path'] = os.path.join(app.config['UPLOAD_FOLDER'], data_filename)
 
        return render_template('upload.html')
    

if __name__=='__main__':
    app.run(debug = True)