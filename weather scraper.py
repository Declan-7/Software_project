from datetime import datetime
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
import pandas as pd 


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
    




#
sql = """
CREATE TABLE IF NOT EXISTS current(
Time INTEGER,
temperature INTEGER,
sunrise INTEGER,
sunset INTEGER,
Wind_Speed INTEGER,
Wind_Temp INTEGER,
Description VARCHAR(45)
)

"""


try:
    res = engine.execute ("DROP TABLE IF EXISTS current")
    res = engine.execute(sql)
    print(res)
except Exception as e:
    print(e)
    URL = "http://api.openweathermap.org/data/2.5/onecall?id=524901&appid=07daa9f106813518ee71c9fd2dc84557&lat=53.344&lon=-6.2672&exclude=minutely,alerts"

    


try:
# Make the get request
    r = requests.get(url=URL)
    time.sleep(60*15)
except requests.exceptions.RequestException as err:
    print("SOMETHING WENT WRONG:", err)
    exit(1)
weather = r.json()


def weather_to_db(text):  
    weather = json.loads(text)
   # print(type(weather), len(weather))
   # print(weather)
    x= datetime.fromtimestamp(weather.get('current').get('sunrise'))
    y= datetime.fromtimestamp(weather.get('current').get('sunset'))
    print(x)
    print(y)
    #dt_obj_sunrise = datetime.fromtimestamp(x).strftime('%d-%m-%y-%t')
    #dt_obj_sunset = datetime.fromtimestamp(y).strftime('%d-%m-%-%t')
    for i in range(0,len(weather.get('current').get('weather'))):
        
        vals = (weather.get('current').get('dt'),
               weather.get('current').get('time'),
               x,
               y,
               weather.get('current').get('wind_speed'),
               weather.get('current').get('wind_deg'),
               weather.get('current').get('weather')[0]['description'])
            
                    
                


                
       
    engine.execute("INSERT INTO current values(%s,%s,%s,%s,%s,%s,%s)", vals)
        

    return 
weather_to_db(r.text)
df = pd.read_sql_table("current", engine)

display(df.head())







sql1= """
CREATE TABLE IF NOT EXISTS hourly_weather (
Time INTEGER,
temperature INTEGER,
WindSpeed INTEGER,
WindTemp INTEGER,
Description VARCHAR(256),
Icon VARCHAR(256)
)
"""

try:
    res = engine.execute ("DROP TABLE IF EXISTS hourly_weather")
    res = engine.execute(sql1)
    print(res)
except Exception as e:
    print(e)
    URL = "http://api.openweathermap.org/data/2.5/onecall?id=524901&appid=07daa9f106813518ee71c9fd2dc84557&lat=53.344&lon=-6.2672&exclude=minutely,alerts"

    
    

try:
# Make the get request
    r1= requests.get(url=URL)
    time.sleep(60*60)
except requests.exceptions.RequestException as err:
    print("SOMETHING WENT WRONG:", err)
    exit(1)
weather1 = r1.json()
print(weather1)
def weather_to_db1(text):
    sleep(60*60)
    weather1 = json.loads(text)
    #using index[0] gets the current hour as the api is updated everyhour
    vals = ((weather1).get('hourly')[0].get('dt'),
            (weather1).get('hourly')[0].get('temp'),
            (weather1).get('hourly')[0].get('wind_speed'),
            (weather1).get('hourly')[0].get('wind_deg'),
            (weather1).get("hourly")[0].get('weather')[0]['description'],
            (weather1).get("hourly")[0].get('weather')[0]['icon'])
                
                 
    engine.execute("INSERT INTO hourly_weather values(%s,%s,%s,%s,%s,%s)", vals)
        

    return 
weather_to_db1(r.text)

df = pd.read_sql_table("hourly_weather", engine)


display(df.head())



sql2= """
CREATE TABLE IF NOT EXISTS dailyweather (
temperature_day FLOAT,
temperature_night FLOAT,
temperature_min FLOAT,
temperature_max FLOAT,
temperature_evening FLOAT,
temperature_morning FLOAT,
sunrise INTEGER,
sunset INTEGER,
moonset INTEGER,
moonrise INTEGER,
Wind_Speed FLOAT,
Wind_Temp INTEGER,
Description VARCHAR(256),
Icon VARCHAR(256)
)
"""

try:
# Make the get request
    r2= requests.get(url=URL)
    time.sleep(60*60*24)
except requests.exceptions.RequestException as err:
    print("SOMETHING WENT WRONG:", err)
    exit(1)
weather2 = r2.json()
print(weather2)


    
try:
    res = engine.execute ("DROP TABLE IF EXISTS dailyweather")
    res = engine.execute(sql2)
    print(res)
except Exception as e:
    print(e)
    URL = "http://api.openweathermap.org/data/2.5/onecall?id=524901&appid=07daa9f106813518ee71c9fd2dc84557&lat=53.344&lon=-6.2672&exclude=minutely,alerts"

    
def weather_to_db2(text):
    weather2 = json.loads(text)
    #using index[0] gets the current day as the api is updated everyhour. Can get tomorrow by using [1] and day after tomorrow by [2] etc

    time.sleep(60*60*24)
    vals =  ((weather2).get('daily')[0].get('temp').get('day'),
            (weather2).get('daily')[0].get('temp').get('night'),
            (weather2).get('daily')[0].get('temp').get('min'),
            (weather2).get('daily')[0].get('temp').get('max'),
            (weather2).get('daily')[0].get('temp').get('eve'),
            (weather2).get('daily')[0].get('temp').get('morn'),
            (weather2).get('daily')[0].get('sunrise'),
            (weather2).get('daily')[0].get('sunset'),
            (weather2).get('daily')[0].get('moonset'),
            (weather2).get('daily')[0].get('moonrise'),
            (weather2).get('daily')[0].get('wind_speed'),
            (weather2).get('daily')[0].get('wind_deg'),
            (weather2).get("daily")[0].get('weather')[0]['description'],
            (weather2).get("daily")[0].get('weather')[0]['icon'])
                
                 
    engine.execute("INSERT INTO dailyweather values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", vals)
        

    return 
weather_to_db2(r2.text)

df = pd.read_sql_table("dailyweather", engine)


display(df.head())

