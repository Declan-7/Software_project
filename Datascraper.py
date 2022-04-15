#!/usr/bin/env python
# coding: utf-8

# # CODE

# In[ ]:


import sqlalchemy as sqla
from sqlalchemy import create_engine
import traceback
import simplejson as json
import requests
import time
import pymysql
from sqlalchemy import *
import json
import datetime as dt


# # CREATE TABLE

# In[ ]:


URL="dbike.cvo8g1gt1fco.eu-west-1.rds.amazonaws.com"
PORT="3306"
DB = "dbike"
USER = "group15"
PASSWORD = "declanmingbo"
api_key = "53c9b7d9148fef65635074fed863cc14f718219f"
r = requests.get("https://api.jcdecaux.com/vls/v1/stations?contract=dublin&apiKey=" + api_key)


# In[ ]:


engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format(USER, PASSWORD, URL, PORT, DB), echo=True)
sql = """CREATE DATABASE IF NOT EXISTS dbike;"""
engine.execute(sql)


# In[ ]:


for res in engine.execute("SHOW VARIABLES"):
    print(res)


# In[ ]:


def initaldatabase():
    sql1 = """
    CREATE TABLE IF NOT EXISTS station (
    address VARCHAR(256) ,
    banking INTEGER,
    bike_stands INTEGER,
    bonus INTEGER,
    contract_name VARCHAR(256),
    name VARCHAR(256),
    number INTEGER,
    position_lat REAL,
    position_lng REAL,
    status VARCHAR(256))"""
    
    try:
        res = engine.execute ("DROP TABLE IF EXISTS station")
        res = engine.execute(sql1)
        print(res)
    except Exception as e:
        print(e)
        
    sql2= """
    CREATE TABLE IF NOT EXISTS availability (
    number INTEGER,
    available_bikes INTEGER,
    available_bike_stands INTEGER,
    last_update VARCHAR(256))"""
    try:
        res = engine.execute ("DROP TABLE IF EXISTS availability")
        res = engine.execute(sql2)
        print(res)
    except Exception as e:
        print(e)
        
    sql3 = """
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
        res = cursor.execute(sql3)
        print('Created successfully!')
    except Exception as e:
        print(e)
    
    station_insert()


# # INSERT DATA

# In[ ]:


def stations_to_db():
    stationList=[]
    stations = json.loads(r.text)
    for station in stations:
        vals_s = (station.get('address'), 
                int(station.get('banking')),
                station.get('bike_stands'), 
                int(station.get('bonus')),
                station.get('contract_name'),
                station.get('name'),
                station.get('number'),
                station.get('position').get('lat'),
                station.get('position').get('lng'),
                station.get('status'))
        stationList.append(vals_s)
    return stationList


# In[ ]:


def station_insert():
    vals = stations_to_db()
    try:
        for val in vals:
            engine.execute("INSERT INTO station values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", val)
            db.commit()
            print("Insert correctly!")
    except Exception as e:
        db.rollback()
        print(e)


# In[ ]:


def availability_to_db():
    availabilityList=[]
    stations = json.loads(r.text)
    for availability in stations:
        vals_a = (availability.get('number'),
               availability.get('available_bikes'),
               availability.get('available_bike_stands'),
               dt.datetime.fromtimestamp(int(availability.get('last_update') / 1e3)))
        
        availabilityList.append(vals_a)
    return availabilityList


# In[ ]:


def availability_insert():
    vala = availability_to_db()
    try:
        for val in vala:
            sql = """INSERT INTO dbike.availability (number,available_bikes,available_bike_stands,last_update) VALUE (%s,%s,%s,'%s')""" % val
            engine.execute(sql)
            print("Insert correctly!")
    except Exception as e:
        print(e)


# In[ ]:


def weather_to_db(text):
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
        print("Insert wrong")
    
    db.close()


# In[ ]:





# In[ ]:


import requests 
import traceback 
import datetime
import time
import mysql
from datetime import datetime

import mysql.connector
import sys

URL="dbike.cvo8g1gt1fco.eu-west-1.rds.amazonaws.com"
PORT=3306
DB = "dbike"
USER = "group15"
PASSWORD = "declanmingbo"

db = pymysql.connect(
    host=URL,
    user=USER,
    password=PASSWORD,
    port=PORT,
    database=DB)
cursor = db.cursor()
initaldatabase()
db.close()
while True:
    
    bike_api_key = "53c9b7d9148fef65635074fed863cc14f718219f"
    r_bike = requests.get("https://api.jcdecaux.com/vls/v1/stations?contract=dublin&apiKey=" + bike_api_key)
    
    weatehr_api_key = "e857655954f34ae188982244bbb23b21"
    city_name = 'Dublin,ie'
    parameters = {"q" : city_name, "appid" : weatehr_api_key} 
    WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather" 
    r_weather = requests.get(WEATHER_URL, params = parameters)

    db = pymysql.connect(
        host=URL,
        user=USER,
        password=PASSWORD,
        port=PORT,
        database=DB)
    cursor = db.cursor()
    
    availability_insert()
    weather_to_db(r_weather.text)
    
    time.sleep(5*60)

# TEST CONNECTIONmetadata = sqla.MetaData(bind=engine)
print(metadata)
station = sqla.Table('station', metadata, autoload=True)
print(station)
availability = sqla.Table('availability', metadata, autoload=True)
print(availability)import pandas as pd
df = pd.read_sql_table("station", engine)display(df.head())sql = "select count(*) from availability;"
print(engine.execute(sql).fetchall())sql = "select name from station limit 10;"
for row in engine.execute(sql):
    print(row)