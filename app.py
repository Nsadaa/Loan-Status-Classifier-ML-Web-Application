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


#get form data
@app.route('/classifier',methods=['GET','POST'])
def classifier():

    #checking request type
    str_req_type = request.method

    #convert string value into numeric value
    if request.method == str(str_req_type):

        x = request.args.get('loanamount')

        value_cl = "Accepted"
        return  render_template('result.html', value=value_cl)


if __name__ == '__main__':
    app.run(debug=True)
