from flask import Flask, request, jsonify
import json
from redis_connector_patient import Patient

#receive mock IOT data
app = Flask(__name__)
patient = Patient("Boris")


@app.route('/reception', methods=["GET", "POST"])
def reception():
    """Receive the data from the IOT device"""
    if request.method == "POST":
        content = request.get_json()
        print("Blood pressure: ", content["bp"])
        print("SP02: ", content["sp"])
        print("Pulse: ", content["pulse"])
        print("Temp: ", content["temp"])
        print("---------------------------------")
        patient.receive_vitals(content["bp"], content["sp"], content["pulse"], content["temp"])
        return content


if __name__ == '__main__':
    app.run()
