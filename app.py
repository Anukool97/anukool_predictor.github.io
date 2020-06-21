from flask import Flask,request
import pandas as pd
import numpy as np
import pickle
import flasgger
from flasgger import Swagger

app= Flask(__name__)
Swagger(app)

pickle_in=open('model.pkl','rb')
model=pickle.load(pickle_in)

@app.route('/')

def HelloWorld ():
    return "Hello World"

@app.route('/predict')
def predict():

    """Here is the covid Predictor for you.
    Keep calm donot hurry to Hospital too early.
    ---
    parameters:
        - name: Leukocytes
          in: query
          type: number
          required: true
        - name: Monocytes
          in: query
          type: number
          required: true
        - name: Platelets
          in: query
          type: number
          required: true
        - name: Patient age quantile
          in: query
          type: number
          required: true
    responses:
        200:
            description: Passed the parameters
    """        
            
    

    Leukocytes=request.args.get('Leukocytes')
    Monocytes=request.args.get('Monocytes')
    Platelets=request.args.get('Platelets')
    Age=request.args.get('Patient age quantile')
    prediction=model.predict([[Leukocytes,Monocytes,Platelets,Age]])
    output=list(prediction)
    result=[]
    for i in output:
        if i==0:
            result.append(" Safe ")
        else:
            result.append(" Covid-Symptoms Found ")
    return "The Predicted Value IS "+str(result)

@app.route('/predict_file',methods=["POST"])
def predict_file():
    """Here is the covid Predictor for you.
        Keep calm donot hurry to Hospital too early.

    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true

    responses:
        200:
            description: Passed the parameters
    """


    
    df_test=pd.read_csv(request.files.get("file"))
    prediction=model.predict(df_test)
    output=list(prediction)
    result=[]
    for i in output:
        if i==0:
            result.append("Safe")
        else:
            result.append("Covid-Symptoms Found")
    ans='\n'.join(result)

            
    return "The Predicted values for csv file are \n" + str(ans)



if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=5000)
    
