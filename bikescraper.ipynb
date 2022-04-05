{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "937fc345",
   "metadata": {},
   "source": [
    "# CODE"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1a7aab15",
   "metadata": {},
   "outputs": [],
   "source": [
    "import sqlalchemy as sqla\n",
    "from sqlalchemy import create_engine\n",
    "import traceback\n",
    "import glob\n",
    "import os\n",
    "from pprint import pprint\n",
    "import simplejson as json\n",
    "import requests\n",
    "import time\n",
    "from IPython.display import display\n",
    "import pymysql\n",
    "import sql_metadata\n",
    "from sqlalchemy import *\n",
    "import json"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fe906792",
   "metadata": {},
   "source": [
    "# CREATE TABLE"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "78a6dab6",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "URI=\"dbike.cvo8g1gt1fco.eu-west-1.rds.amazonaws.com\"\n",
    "PORT=\"3306\"\n",
    "DB = \"dbike\"\n",
    "USER = \"group15\"\n",
    "PASSWORD = \"declanmingbo\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d49615be",
   "metadata": {},
   "outputs": [],
   "source": [
    "engine = create_engine(\"mysql+pymysql://{}:{}@{}:{}/{}\".format(USER, PASSWORD, URI, PORT, DB), echo=True)\n",
    "sql = \"\"\"CREATE DATABASE IF NOT EXISTS dbike;\"\"\"\n",
    "engine.execute(sql)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d92a6b21",
   "metadata": {},
   "outputs": [],
   "source": [
    "for res in engine.execute(\"SHOW VARIABLES\"):\n",
    "    print(res)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8555e040",
   "metadata": {},
   "outputs": [],
   "source": [
    "sql = \"\"\"\n",
    "CREATE TABLE IF NOT EXISTS station (\n",
    "address VARCHAR(256) ,\n",
    "banking INTEGER,\n",
    "bike_stands INTEGER,\n",
    "bonus INTEGER,\n",
    "contract_name VARCHAR(256),\n",
    "name VARCHAR(256),\n",
    "number INTEGER,\n",
    "position_lat REAL,\n",
    "position_lng REAL,\n",
    "status VARCHAR(256)\n",
    ")\n",
    "\"\"\"\n",
    "\n",
    "try:\n",
    "    res = engine.execute (\"DROP TABLE IF EXISTS station\")\n",
    "    res = engine.execute(sql)\n",
    "    print(res)\n",
    "except Exception as e:\n",
    "    print(e)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "04493b12",
   "metadata": {},
   "outputs": [],
   "source": [
    "sql= \"\"\"\n",
    "CREATE TABLE IF NOT EXISTS availability (\n",
    "number INTEGER,\n",
    "available_bikes INTEGER,\n",
    "available_bike_stands INTEGER,\n",
    "last_update INTEGER\n",
    ")\n",
    "\"\"\"\n",
    "try:\n",
    "    res = engine.execute (\"DROP TABLE IF EXISTS availability\")\n",
    "    res = engine.execute(sql)\n",
    "    print(res)\n",
    "except Exception as e:\n",
    "    print (e"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ef1e3d13",
   "metadata": {},
   "source": [
    "# INSERT DATA"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ed25cdca",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests \n",
    "import traceback \n",
    "import datetime\n",
    "import time\n",
    "import mysql\n",
    "from datetime import datetime\n",
    "\n",
    "import mysql.connector\n",
    "import sys\n",
    "api_key = \"53c9b7d9148fef65635074fed863cc14f718219f\"\n",
    "URL = \"https://api.jcdecaux.com/vls/v1/stations?contract=dublin&apiKey=\" + api_key\n",
    "\n",
    "try:\n",
    "# Make the get request\n",
    "    r = requests.get(url=URL)\n",
    "    ## time.sleep(1*60)\n",
    "except requests.exceptions.RequestException as err:\n",
    "    print(\"SOMETHING WENT WRONG:\", err)\n",
    "    exit(1)\n",
    "stations = r.json()\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1f163afc",
   "metadata": {},
   "outputs": [],
   "source": [
    "def stations_to_db(text):  \n",
    "    stations = json.loads(text)\n",
    "    print(type(stations), len(stations))\n",
    "    for station in stations:\n",
    "        print(station)\n",
    "        vals = (station.get('address'), \n",
    "                int(station.get('banking')),\n",
    "                station.get('bike_stands'), \n",
    "                int(station.get('bonus')),\n",
    "                station.get('contract_name'),\n",
    "                station.get('name'),\n",
    "                station.get('number'),\n",
    "                station.get('position').get('lat'),\n",
    "                station.get('position').get('lng'),\n",
    "                station.get('status'))\n",
    "       \n",
    "        engine.execute(\"INSERT INTO station values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)\", vals)\n",
    "        \n",
    "\n",
    "    return\n",
    "stations_to_db(r.text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0ff69e27",
   "metadata": {},
   "outputs": [],
   "source": [
    "def availability_to_db(text):  \n",
    "    stations = json.loads(text)\n",
    "    print(type(stations), len(stations))\n",
    "    for availability in stations:\n",
    "        print(availability)\n",
    "        \n",
    "        vals = (availability.get('number'),\n",
    "               availability.get('available_bikes'),\n",
    "               availability.get('available_bike_stands'),\n",
    "               availability.get('last_update'))\n",
    "        \n",
    "        engine.execute(\"INSERT INTO availability values(%s,%s,%s,%s)\", vals)\n",
    "\n",
    "    return\n",
    "availability_to_db(r.text)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "be7a22e6",
   "metadata": {},
   "source": [
    "# TEST CONNECTION"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4497fd61",
   "metadata": {},
   "outputs": [],
   "source": [
    "metadata = sqla.MetaData(bind=engine)\n",
    "print(metadata)\n",
    "station = sqla.Table('station', metadata, autoload=True)\n",
    "print(station)\n",
    "availability = sqla.Table('availability', metadata, autoload=True)\n",
    "print(availability)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b10859a9",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "df = pd.read_sql_table(\"station\", engine)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "adcd596e",
   "metadata": {},
   "outputs": [],
   "source": [
    "display(df.head())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "67cde307",
   "metadata": {},
   "outputs": [],
   "source": [
    "sql = \"select count(*) from availability;\"\n",
    "print(engine.execute(sql).fetchall())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "50b21d05",
   "metadata": {},
   "outputs": [],
   "source": [
    "sql = \"select name from station limit 10;\"\n",
    "for row in engine.execute(sql):\n",
    "    print(row)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
