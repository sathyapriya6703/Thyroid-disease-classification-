import flask
from flask import Flask, render_template, request
import pickle
import numpy as np
import sklearn
app = Flask(__name__)

model = pickle.load(open('rfd.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('thyroid.html')


@app.route('/getdata', methods=['POST'])
def pred():
    age = int(request.form['Age'])
    print(age)
    sex = request.form['Sex']
    print(sex)
    thyroxine= request.form['thyroxine']
    print(age)
    query = request.form['query']
    print(age)
    antithyro = request.form['antithyroid']
    print(age)
    sick = request.form['Sick']
    print(age)
    preg= request.form['Pregnant']
    print(age)
    thyros= request.form['ThyroSurgery']
    print(age)
    treat = request.form['I131treat']
    print(age)
    query1= request.form['qweryhypo']
    print(age)
    query2= request.form['qweryhyper']
    print(age)
    Li= request.form['Lithium']
    print(age)
    Go = request.form['Goitre']
    print(age)
    Tu = request.form['Tumour']
    print(age)
    hypo= request.form['Hypo']
    print(age)
    Psycho= request.form['Psycho']
    print(age)
    tsh= request.form['TSH']
    print(age)
    t3= request.form['T3']
    print(age)
    t4u= request.form['T4U']
    print(age)

    fti= request.form['FTI']
    print(age)
    rs= request.form['RS']
    print(age)
    pid = request.form['PI']
    inp_features= [[age,np.log(float(sex)),int(thyroxine),int(query),int(antithyro),int(sick),
                   int(preg),int(thyros),int(treat), int(query1),int(query2),int(Li),
                   int(Go), int(Tu),int(hypo),int(Psycho),np.log(float(tsh)), np.log(float(t3)),
                    np.log(float(t4u)),np.log(float(fti)), int(rs), int(pid)]]
    print(inp_features)
    prediction = model.predict(inp_features)
    print(type(prediction))
    t = prediction[0]
    print(t)
    if t > 0.5:
        prediction_text = 'You have thyroid, Thyroid will be predicted'
    else:
        prediction_text = 'Thyroid not predicted'
    print(prediction_text)
    return render_template('prediction.html', prediction_results=prediction_text)


if __name__ == "__main__":
    app.run()
