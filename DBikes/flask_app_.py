import json
import pymysql
from sqlalchemy import create_engine
import pandas as pd
from flask import Flask,request, render_template,jsonify
import dbike_info 
import pickle 
import numpy as np
from sklearn.linear_model import LinearRegression

app = Flask(__name__,template_folder='templates')

@app.route("/")
def hello():
    return render_template("app.html")


@app.route("/stations")
def station_sql():
         engine = create_engine(
         f"mysql+mysqlconnector://{dbike_info.USER}:{dbike_info.PASSWORD}@{dbike_info.URI}"
          f":3306/{dbike_info.DB}", echo=True)
        
         query ="SELECT s.number, s.name, s.address, s.position_lat, s.position_lng, a.available_bike_stands, a.available_bikes, a.last_update," \
          "s.status, MAX(a.last_update) AS `current_availability` " \
          "FROM dbike.availability as a " \
          "INNER JOIN dbike.station as s ON s.number = a.number " \
          "GROUP BY s.number " \
          "ORDER BY s.number;"
        
        

         df = pd.read_sql(query, engine)

         return df.to_json(orient="records")
         json.dump(df)
#      <link rel="stylesheet"  type="text/css" href="/static/cssbike.css">
@app.route("/weather")
def wthr():
    engine2 = create_engine(
    f"mysql+mysqlconnector://{dbike_info.USER}:{dbike_info.PASSWORD}@{dbike_info.URI}" f":3306/{dbike_info.DB}", echo=True)
    
    query2= "SELECT * FROM dbike.weather order by dt"
    df2 = pd.read_sql(query2,engine2)   
    return df2.to_json(orient="records")
    json.dump(df2)



#!pip3 install pickle5
import pickle5 as pickle


import datetime
import gzip
@app.route('/prediction_/<station>/<predict_date>/<predict_time>')
def predict_available_bikes(station,predict_date,predict_time):
     with open('./models/models/models/' +str(station) + '_station_model.pkl', 'rb') as handle: 
            model = pickle.load(handle)
            print('model',model)
            year,month,day = (int(x) for x in predict_date.split('-'))
            hour_ = int(predict_time[0:2])
            day = int(datetime.date(year,month,day).weekday())
            scattered_clouds = 0
            #hour = int(time[0:2])
            test = [[day,hour_,scattered_clouds]]
            ml = model.predict(test)
            result = round(ml[0])
            print(result)
            return jsonify(result)
     
    
if __name__ == "__main__":
    app.run(debug=True)
    #app.run(debug=True, host='0.0.0.0' ,port=3306)

    
    

