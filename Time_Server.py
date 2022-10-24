from datetime import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/time", methods =["GET"])
def server_time():
    # return the current time as a string 
    time = datetime.now().time()
    time_string = str(time)
    return jsonify(time_string)


@app.route("/date", methods =["GET"])
def server_date():
    # current date as a string
    date = datetime.now().date()
    date_string = datetime.strftime(date, "%m-%d-%y %H:%M:%S")
    return jsonify(date_string)

def get_date():
    date = datetime.now().date()
    return date


@app.route("/age", methods =["POST"])
def age_substract():
    """
        incoming_json = {"date": <10/10/1999>,
                        "units": <years>}
    """
    # gets the age
    date = get_date()
    age_origin = request.get_json()
    date_object_age_origin = datetime.strptime(age_origin['date'], "%m/%d/%Y")
    my_time = datetime.min.time()
    age = datetime.combine(date, my_time) - date_object_age_origin
    return jsonify(round(age.days/365,2))

if __name__ == "__main__":
    app.run()