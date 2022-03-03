import sqlalchemy as sqla
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
CREATE TABLE IF NOT EXISTS weather (
temperature INTEGER,
sunset INTEGER,
sunrise INTEGER,
wind_speed INTEGER
)
"""

try:
    res = engine.execute ("DROP TABLE IF EXISTS weather")
    res = engine.execute(sql)
    print(res)
except Exception as e:
    print(e)
    
    
    
    
    
    
    
    
    
    
    
    URL = "http://api.openweathermap.org/data/2.5/weather?lat=53.349562&lon=-6.278198&appid=c51131085fb0be0598c73ebf0f4e70f5"

try:
# Make the get request
    r = requests.get(url=URL)
    #time.sleep(1)
except requests.exceptions.RequestException as err:
    print("SOMETHING WENT WRONG:", err)
    exit(1)
weather = r.json()


def weather_to_db(text):  
    weather = json.loads(text)
    print(type(weather), len(weather))
    print(weather)
    vals = (weather.get('main').get('temp'),
                weather.get('sys').get('sunrise'),
                weather.get('sys').get('sunset'),
                weather.get('wind').get('speed'))

                
       
    engine.execute("INSERT INTO weather values(%s,%s,%s,%s)", vals)
        

    return
weather_to_db(r.text)

import pandas as pd
df = pd.read_sql_table("weather", engine)


display(df.head())