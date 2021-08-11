import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
from flask import Flask , render_template , request
import gunicorn

app = Flask(__name__)

@app.route('/')

@app.route('/Home',methods=["GET"])
def Home():

    #render template
    return render_template('index.html')


@app.route('/Form',methods=["GET"])
def Form():

    #render template
    return render_template('form.html')




if __name__ == '__main__':
    app.run(debug=True)
