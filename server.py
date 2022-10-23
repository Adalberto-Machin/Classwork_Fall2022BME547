from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods =["GET"])
def server_status():
    return "Server is on. "


@app.route("/info", methods =["GET"])
def information(): 
    x = "Machin is the beast, absolute unit"
    return x


@app.route("/hdl_check", methods =["POST"])
def hdl_check_from_internet():
    """
        incoming_json = {"name": <name_str>,
                        "hdl_value": <hdl_value_int>}
    """
    from blood_calculator import check
    in_data = request.get_json()
    hdl_value = in_data["hdl_value"]
    print(f"HDL value was {hdl_value}")
    answer = check(hdl_value)
    return jsonify(answer)


@app.route("/add_numbers", methods =["POST"])
def sum_code():
    """
        incoming_json = {"a": <number>,
                        "b": <number>}
    """
    in_data = request.get_json()
    numbers = list(in_data.values())
    sum_result = sum(numbers)
    print(f"Sum value was {sum_result}")
    #print(numbers)
    # answer = sum_result
    answer = sum_result
    return jsonify(answer)

if __name__ == "__main__":
    app.run()