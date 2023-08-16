from flask import Flask, request

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello World!'

@app.route("/calculator/add", methods=['POST'])
def add():
    numbers = request.json
    first = numbers['first']
    second = numbers['second']
    return {'result': first + second}

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    numbers = request.json
    first = numbers['first']
    second = numbers['second']
    return {'result': first - second}

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')