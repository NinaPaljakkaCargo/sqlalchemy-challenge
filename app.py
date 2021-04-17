#import dependencies
from flask import Flask
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


