from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd
from views import views




app = Flask(__name__)

app.register_blueprint(views, url_prefix="/")

{}

if __name__=="__main__":
    app.run(debug=True,port=8000)