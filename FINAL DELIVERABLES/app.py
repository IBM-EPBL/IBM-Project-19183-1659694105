import os
import numpy as np
from flask import Flask, request, render_template, send_from_directory, make_response
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image


app = Flask(__name__,template_folder='template') #initializing a flask app 
model=load_model('ECG.h5')

@app.route("/")
@app.route("/index.html")
def home():
    return render_template("index.html")


@app.route("/info.html")
def info():
    return render_template("info.html")

@app.route("/predict.html")
def infos():
    return render_template("predict.html")


@app.route("/premature_atrial_contraction.html")
def upload():
    return render_template("premature_atrial_contraction.html")

def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
    app.run(debug=True)