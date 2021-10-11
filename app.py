import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#Set Up the Database, access the SQLite database
#create_engine() function allows us to access and query our SQLite database file.
engine = create_engine("sqlite:///hawaii.sqlite")

#reflect the database into classes
Base = automap_base()

#reflect the database
Base.prepare(engine, reflect=True)

#save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

#create a session link from Python to our database
session = Session(engine)

#define Flask app, create a Flask application called "app."
app = Flask(__name__)

#define the welcome route using @app.route("/") code
@app.route("/")

#create a function welcome() with a return statement
def welcome():
    return(
#add the precipitation, stations, tobs, and temp routes that we'll need into return statement
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''') 



