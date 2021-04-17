#import dependencies
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt
from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

engine = create_engine("sqlite:///hawaii2.sqlite")
base = automap_base()
base.prepare(engine,reflect=True)
measurement_class = base.classes.measurement
station_class = base.classes.station
session = Session(engine)

app = Flask(__name__)

#Use Flask to create your routes.
@app.route("/")
def route_1():
    return(
        f"Home Page<br/>"
        f"<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"-->Precipitation Data<br/>"
        f"<br/>"
        f"/api/v1.0/stations<br/>"
        f"-->Station Data<br/>"
        f"<br/>"
        f"/api/v1.0/tobs<br/>"
        f"-->Temperature Data<br/>"
        f"<br/>"
        f"/api/v1.0/<start><br/>"
        f"-->Temperature Data for dates greater than or equal to the given start date<br/>"
        f"<br/>"
        f"/api/v1.0/<start>/<end><br/>"
        f"-->Temperature data for dates between the start and end dates<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation_data():
    recent_date = session.query(func.max(measurement_class.date)).first()
    last_12months = dt.date(2017,8,23)-dt.timedelta(days=365)

