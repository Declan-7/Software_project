from sqlalchemy import sqla
from sqlalchemy import create_engine
import traceback
import glob
import os
from pprint import pprint
import simplejson as json
import requests
import time
from IPython.display import display
import pymysql
import sql_metadata
from sqlalchemy import *
import json



URI="dbike.cvo8g1gt1fco.eu-west-1.rds.amazonaws.com"
PORT="3306"
DB = "dbike"
USER = "group15"
PASSWORD = "declanmingbo"

engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format(USER, PASSWORD, URI, PORT, DB), echo=True)
sql = """CREATE DATABASE IF NOT EXISTS dbike;"""
engine.execute(sql)

for res in engine.execute("SHOW VARIABLES"):
    print(res)
    
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
status VARCHAR(256)
)
"""

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
last_update INTEGER
)
"""
try:
    res = engine.execute ("DROP TABLE IF EXISTS availability")
    res = engine.execute(sql)
    print(res)
except Exception as e:
    print (e)
    
    
    
import requests 
import traceback 
import datetime
import time
from datetime import datetime
import mysql
import mysql.connector
import sys
api_key = "53c9b7d9148fef65635074fed863cc14f718219f"
URL = "https://api.jcdecaux.com/vls/v1/stations?contract=dublin&apiKey=" + api_key

try:
# Make the get request
    r = requests.get(url=URL)
    time.sleep(5*60)
except requests.exceptions.RequestException as err:
    print("SOMETHING WENT WRONG:", err)
    exit(1)
stations = r.json()


def stations_to_db(text):  
    stations = json.loads(text)
    print(type(stations), len(stations))
    for station in stations:
        print(station)
        vals = (station.get('address'), 
                int(station.get('banking')),
                station.get('bike_stands'), 
                int(station.get('bonus')),
                station.get('contract_name'),
                station.get('name'),
                station.get('number'),
                station.get('position').get('lat'),
                station.get('position').get('lng'),
                station.get('status'))
       
        engine.execute("INSERT INTO station values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", vals)
        

    return
stations_to_db(r.text)



def availability_to_db(text):  
    stations = json.loads(text)
    print(type(stations), len(stations))
    for availability in stations:
        print(availability)
        
        vals = (availability.get('number'),
               availability.get('available_bikes'),
               availability.get('available_bike_stands'),
               availability.get('last_update'))
        
        engine.execute("INSERT INTO availability values(%s,%s,%s,%s)", vals)

    return
availability_to_db(r.text)


metadata = sqla.MetaData(bind=engine)
print(metadata)
station = sqla.Table('station', metadata, autoload=True)
print(station)
availability = sqla.Table('availability', metadata, autoload=True)
print(availability)


import pandas as pd
df = pd.read_sql_table("station", engine)


display(df.head())

sql = "select count(*) from availability;"
print(engine.execute(sql).fetchall())


sql = "select name from station limit 10;"
for row in engine.execute(sql):
    print(row)
