#import dependencies
from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import numpy as np
import datetime as dt

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
    session = Session(engine)
    recent_date = session.query(func.max(measurement_class.date)).first()
    last_12months = dt.date(2017,8,23)-dt.timedelta(days=365)
    last_12Precip = session.query(measurement_class.date,measurement_class.prcp).filter(measurement_class.date >= last_12months).all()
        
    precip_list = []
    for row in recent_date:
        dt_dict = {}
        dt_dict["date"]= row.date
        dt_dict["tobs"]= row.tobs
        precip_list.append(dt_dict)
        
    return jsonify(precip_dict)


@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    session_res = session.query(Station.name).all()
    station_info = list(np.ravel(results))
    
    return jsonify(station_info)


@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    dates = (session.query(measurement_class.date).order_by(measurement_class.date.desc()).first())
    dates_string = str(dates)
    
    station_list = (session.query(measurement_class.station, func.count(measurement_class.station)).group_by(measurement_class.station).desc()).all()
    
    tobs_list = []
    for result in results:
        tobs_dict = {}
        tobs_dict["date"]= result[1]
        tobs_dict["station"]= result[0]
        tobs_dict["Temperature"] = int(result[2])
        tobs_list.append(tobs_dict)

    return jsonify(tobs_list)


#When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
@app.route("/api/v1.0/<start>")
def start_only(start):
    session = Session(engine)
    start_results = (session.query(func.min(measurement_class.tobs),
                                   func.avg(measurement_class.tobs),
                               func.max(measurement_class.tobs)).filter(measurement_class.date >= start).all())
    
    tobs_min = start_results[0][0]
    tobs_avg = start_results[0][1]
    tobs_max = start_results[0][2]
    
    tobs_print = (['Start Date: ' + start,
                   'Min Temp Recorded: ' + str(tobs_min),
                   'Average Temp Recorded: ' + str(tobs_avg),
                   'Max Temp Recorded: ' + str(tobs_max)])
    
    return jsonify(tobs_print)

#When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
@app.route("/api/v1.0/<start>/<end>")
def startANDend(start, end):
    session = Session(engine)
    startEnd_results = (session.query(func.min(measurement_class.tobs),
                                   func.avg(measurement_class.tobs),
                               func.max(measurement_class.tobs)).filter(measurement_class.date >= start).filter(measurement_class.date <= end).all())
    
    tobs_min = start_results[0][0]
    tobs_avg = start_results[0][1]
    tobs_max = start_results[0][2]
    
    tobs_print = (['Start Date: ' + start,
                   'End Date: ' + end,
                   'Min Temp Recorded: ' + str(tobs_min),
                   'Average Temp Recorded: ' + str(tobs_avg),
                   'Max Temp Recorded: ' + str(tobs_max)])
    
    return jsonify(tobs_print)


if __name__ == '__main__':
    app.run(debug=True)
    
    



    
    

