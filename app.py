import joblib
import pandas as pd
from flask import Flask,request,jsonify

app=Flask(__name__)
with open('xgboost_dynamic_pricing_model.pkl','rb') as f:
    model=joblib.load(f)
with open('model_features.pkl','rb') as f:
    model_features=joblib.load(f)  

def preprocessing_input(data):
    data['Customer_Loyalty_Status']=data['Customer_Loyalty_Status'].map({'Regular':0,'Silver':1,'Gold':2})
    data['Time_of_Booking']=data['Time_of_Booking'].map({'Morning':0,'Afternoon':1,'Evening':2,'Night':3})
    data['Vehicle_Type']=data['Vehicle_Type'].map({'Economy':0,'Premium':1})
    data=pd.get_dummies(data,columns=['Location_Category'],drop_first=True)
    data=data.reindex(columns=model_features,fill_value=0)
    return data

def make_prediction(data):
    prediction=model.predict(data)
    return prediction

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method=='GET':
        return jsonify({'response':'Please Use POST Method To Make Prediction'})
    data=request.get_json()
    features=data['features']
    data=pd.DataFrame([features])
    data=preprocessing_input(data)
    pred=make_prediction(data)

    out={}
    cnt=1
    for p in pred:
        out[f'prediction_{cnt}']=float(p)
        cnt+=1
    return jsonify(out)    



@app.route('/Dynamic Pricing',methods=['GET','POST'])
def home():
    return jsonify({'response':'Welcome to the Dynamic Pricing Prediction API'})

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)    