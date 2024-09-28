import pickle

from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
from config import DevelopmentConfig, ProductionConfig

app=Flask(__name__)
app.config.from_object(ProductionConfig)

## Load the model
regmodel=pickle.load(open('regmodel.pkl','rb'))
scalar=pickle.load(open('scaling.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict',methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()]
    final_input=scalar.transform(np.array(data).reshape(1,-1))
    output=regmodel.predict(final_input)[0]
    
    return render_template("home.html", prediction_text=f"The House price prediction is {output:.2f}" )

if __name__=="__main__":
    app.run(debug=True, port=5000)
   
     