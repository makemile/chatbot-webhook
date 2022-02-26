from flask import Flask, request, jsonify
import requests 
import os
import json
import datetime
import sys
import pprint
for place in sys.path:
    print(place)


app = Flask(__name__)
cf_port = os.getenv("PORT")

# Only get method by default
@app.route('/')
def hello():
    return '<h1>SAP Conversational AI</h1><body>The animal facts webhook for use in SAP Conversational AI chatbots.<br><img src="static/283370-pictogram-purple.svg" width=260px></body>'

if __name__ == '__main__':
	if cf_port is None:
		app.run(host='0.0.0.0', port=5000, debug=True)
	else:
		app.run(host='0.0.0.0', port=int(cf_port), debug=True)