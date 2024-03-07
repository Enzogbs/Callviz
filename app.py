from flask import Flask, request
import json

app = Flask(__name__)

events = []

@app.route('/')
def index():
    return {"Teste": "Ok"}

@app.route('/post', methods=['POST'])
def result():
    request_data = request.get_json()
    events.append(request_data)
    return 'Received !'

@app.route('/get_info', methods=['GET'])
def get_info():
    json_event = json.dumps(events)
    return json_event

if __name__ == '__main__':
   app.run()

