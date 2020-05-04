from flask import Flask, request, jsonify
import json

#receive mock IOT data
app = Flask(__name__)


@app.route('/reception', methods=["GET", "POST"])
def reception():
    """Receive the data from the IOT device"""
    if request.method == "POST":
        content = request.get_json()
        print("Blood pressure: ", content["bp"])
        print("SP02: ", content["sp"])
        print("Temperature: ", content["temp"])
        print("---------------------------------")
        return content


if __name__ == '__main__':
    app.run()
