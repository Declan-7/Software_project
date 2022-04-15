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
    sql = """
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
        res = engine.execute(sql)
        print(res)
    except Exception as e:
        print(e)
        
    sql= """
    CREATE TABLE IF NOT EXISTS availability (
    number INTEGER,
    available_bikes INTEGER,
    available_bike_stands INTEGER,
    last_update VARCHAR(256))"""
    try:
        res = engine.execute ("DROP TABLE IF EXISTS availability")
        res = engine.execute(sql)
        print(res)
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
        
    db.close()


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
    
    api_key = "53c9b7d9148fef65635074fed863cc14f718219f"
    r = requests.get("https://api.jcdecaux.com/vls/v1/stations?contract=dublin&apiKey=" + api_key)
    
    db = pymysql.connect(
    host=URL,
    user=USER,
    password=PASSWORD,
    port=PORT,
    database=DB)
    cursor = db.cursor()
    
    availability_insert()
    
    time.sleep(5*60)

# TEST CONNECTIONmetadata = sqla.MetaData(bind=engine)
# print(metadata)
# station = sqla.Table('station', metadata, autoload=True)
# print(station)
# availability = sqla.Table('availability', metadata, autoload=True)
# print(availability)

# import pandas as pd
# df = pd.read_sql_table("station", engine)display(df.head())sql = "select count(*) from availability;"
# print(engine.execute(sql).fetchall())sql = "select name from station limit 10;"
# for row in engine.execute(sql):
   #  print(row)
