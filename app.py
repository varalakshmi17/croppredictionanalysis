from flask import Flask,render_template,url_for,request,redirect
import numpy as np
import pandas as pd
import joblib
import pickle

app = Flask(__name__)

model = joblib.load("regressor.pkl")

@app.route("/")
@app.route("/main")
def main():
      return render_template("main.html")

@app.route("/pridict",methods=["POST"])


def predict():
       int_features = [[features for features in request.form.values()]]
       c = ['Nitrogen', 'Phosphorus', 'Potassium', 'Temperature', 'Humidity', 'PH', 'Rainfall']
       df = pd.DataFrame(int_features, columns = c)
       final = df
       l1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
       l2 = ["apple","banana","blackgram","chickpea","coconut","coffee","cotton","grapes","jute","kidneybeans",
       "lentil","maize","mango","mothbeans","mungbean","muskmelon","orange","papaya","pigeonpeas","pomegranate",
       "rice","watermelon"]
       dic={i:j for i, j in zip(l1,l2)}
       result = model.predict(final)
       for i in result:
            res=dic[i]
            print("The suitable crop is: ",result)
       
       return render_template("main.html", prediction_text="The suitable crop is:{}".format(res))

if __name__=="__main__":
      app.debug=True 
      app.run()