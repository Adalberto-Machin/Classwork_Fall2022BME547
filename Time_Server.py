from datetime import datetime
from datetime import time
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/time", methods=["GET"])
def server_time():
    # return the current time as a string
    time = datetime.now().time()
    time_string = str(time)
    return jsonify(time_string)


@app.route("/date", methods=["GET"])
def server_date():
    # current date as a string
    date = datetime.now().date()
    date_string = datetime.strftime(date, "%m-%d-%y %H:%M:%S")
    return jsonify(date_string)


def get_date():
    date = datetime.now().date()
    return date


@app.route("/age", methods=["POST"])
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
    return jsonify(round(age.days/365, 2))


@app.route("/until_next_meal/<meal>", methods=["GET"])
def server_meal_time(meal):
    time_now = datetime.now().time()
    date = get_date()
    origin_time_now = datetime.combine(date, time_now)
    if meal == "breakfast":
        # gets time till breakfast
        origin_breakfast = datetime.combine(date, time(9, 0, 0))
        breakfast_time_diff = origin_breakfast - origin_time_now
        answer = breakfast_time_diff.seconds/(60*60)
        return jsonify(round(answer, 2))
    elif meal == "lunch":
        # gets time till lunch
        origin_lunch = datetime.combine(date, time(12, 0, 0))
        lunch_time_diff = origin_lunch - origin_time_now
        answer = lunch_time_diff.seconds/(60*60)
        return jsonify(round(answer, 2))
    elif meal == "dinner":
        # gets time till dinner
        origin_dinner = datetime.combine(date, time(19, 0, 0))
        dinner_time_diff = origin_dinner - origin_time_now
        answer = dinner_time_diff.seconds/(60*60)
        return jsonify(round(answer, 2))
    else:
        answer = 'no good input'
        return jsonify(answer, 2)


if __name__ == "__main__":
    app.run()
