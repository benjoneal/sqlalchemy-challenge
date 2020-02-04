###########################################
# imports dependencies
###########################################

import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

###########################################
# initializes database
###########################################

engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

###########################################
# creates references to Measurement
# and Station tables
###########################################

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

####################################
# initializes Flask app
####################################
app = Flask(__name__)

################################
# initializes Flask Routes
################################