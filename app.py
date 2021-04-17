#import dependencies
from flask import Flask
app = Flask(__name__)

#Use Flask to create your routes.
@app.route("/")
def route_1():
    return(
        f"Home Page<br/>"
        f"<br/>"
        f"Precipitation Data<br/>"
        f"<br/>"
        f"Temperature Data<br/>"
        f"<br/>"

    )


