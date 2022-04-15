#!/usr/bin/env python
# coding: utf-8

# # CODE

# In[ ]:


import pymysql 
import traceback
import requests
import time
from datetime import datetime
import json


# # CREATE TABLE

# In[ ]:


api_key = "e857655954f34ae188982244bbb23b21"
city_name = 'Dublin,ie'
parameters = {"q" : city_name, "appid" : api_key} 
WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather" 

def create_table():
    sql = """
    CREATE TABLE IF NOT EXISTS weather(
        Clouds INTEGER,
        feels_like DOUBLE,
        humidity INTEGER,
        pressure INTEGER,
        temp DOUBLE,
        temp_max DOUBLE,
        temp_min DOUBLE,
        sunrise VARCHAR(255),
        sunset VARCHAR(255),
        visibility INTEGER,
        weather_description VARCHAR(255),
        weather_main VARCHAR(255),
        wind_deg INTEGER,
        wind_speed DOUBLE,
        dt VARCHAR(255)
    );
    """
        
    try:
        res = cursor.execute(sql)
        print('Created successfully!')
    except Exception as e:
        print(e)
        


# # INSERT DATA

# In[ ]:


def write_to_db(text):
    weather_data = json.loads(text)
    
    weather_vals = (
        str(weather_data['clouds']['all']),
        str(weather_data['main']['feels_like']),
        str(weather_data['main']['humidity']),
        str(weather_data['main']['pressure']),
        str(weather_data['main']['temp']),
        str(weather_data['main']['temp_max']),
        str(weather_data['main']['temp_min']),
        str(datetime.fromtimestamp(weather_data['sys']['sunrise'])),
        str(datetime.fromtimestamp(weather_data['sys']['sunset'])),
        str(weather_data['visibility']),
        str(weather_data['weather'][0]['description']),
        str(weather_data['weather'][0]['main']),
        str(weather_data['wind']['deg']),
        str(weather_data['wind']['speed']),
        str(datetime.fromtimestamp(weather_data['dt']))
    )
    
    sql = """INSERT INTO dbike.weather (Clouds,feels_like,humidity,pressure,
    temp,temp_max,temp_min,sunrise,sunset,visibility,weather_description,
    weather_main,wind_deg,wind_speed,dt) 
    VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',
    '%s','%s','%s','%s','%s')""" % weather_vals
    
    try:
        cursor.execute(sql)
        db.commit()
        print("Insert successfully")
    except:
        db.rollback()
        print("Insert wrong")
    
    db.close()

