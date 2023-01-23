from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np
import os
import  sklearn
app = Flask(__name__)
model=pickle.load(open('C:/Users/SANTHOSH/Downloads/agrothon/signup.html/fertilizer/finalized_model.pkl','rb'))


picFolder = os.path.join('static', 'pics')
print(picFolder)
app.config['UPLOAD_FOLDER'] = picFolder


@app.route('/')
def hello_world():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], 'img1.jpg')
    return render_template("signup.html/fertilizer/templates/fertilizer_rec.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model.predict_proba(final)
    output='{0:.{1}f}'.format(prediction[0][1], 2)

    if output>str(0.5):
        return render_template('forest.html',pred='Your Forest is in Danger.\nProbability of fire occuring is {}'.format(output),bhai="kuch karna hain iska ab?")
    else:
        return render_template('forest.html',pred='Your Forest is safe.\n Probability of fire occuring is {}'.format(output),bhai="Your Forest is Safe for now")


if __name__ == '__main__':
    app.run(debug=True)
