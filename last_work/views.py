from flask import Blueprint,render_template,request
import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

with open("C:/Users/Joni/Desktop/last_work/model/model.model","rb") as model:
    model=pickle.load(model)
datos=pd.read_csv("C:/Users/Joni/Desktop/last_work/datos_train.csv")
datos["Date"]=pd.to_datetime(datos['Date'],format='%Y/%m/%d')
datos=datos.set_index("Date")



views = Blueprint(__name__,"views")

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/predict")
def show_pred():
    pred=model.predict(steps=30)
    pred=pd.DataFrame(pred)

    fig, ax = plt.subplots(figsize=(10, 3))
    graph=pred.plot(linewidth=2, label='predicción', ax=ax)
    ax.set_title('Predicción')
    ax.legend()
    fig.savefig("./static/my_plot.png");


    return render_template("predict.html",tables=[pred.to_html(classes="data")],titles=pred.columns.values)




@views.route("/update")
def update():
    return render_template("actualizar.html")

@views.route("/fit")
def fit():
    return render_template("fit.html")





