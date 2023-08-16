from flask import Flask, request, jsonify
from dataclasses import dataclass

@dataclass
class Result:
    result: int

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello World!'

@app.route("/calculator/add", methods=['POST'])
def add():
    numbers = request.json
    response = Result(numbers['first'] + numbers['second'])
    # first = numbers['first']
    # second = numbers['second']
    return jsonify(response)
    # return jsonify(int(first + second))

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    numbers = request.json
    # response = Result(numbers['first'] - numbers['second'])
    first = numbers['first']
    second = numbers['second']
    return jsonify(Result(first - second))
    # return jsonify(int(first + second))

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')