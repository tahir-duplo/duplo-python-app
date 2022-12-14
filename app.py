#!/usr/bin/python

import time

import os
import datetime

from flask import Flask

app = Flask(__name__)


@app.route('/')
def root():
    return "Sample python app running on 8082.<br/><br/>" + endpoints()


@app.route('/endpoints')
def endpoints():
    endpoint = "<b>Endpoints</b> : <br/>"
    endpoint += "1. List of environment variables - [/env-list]<br/>"
    endpoint += "2. Hello - [/hello/(name)]<br/>"
    endpoint += "3. Get current time - [/current-time]<br/>"
    endpoint += "4. Get Duplo Details - [/duplo]<br/>"
    return endpoint


@app.route('/env-list')
def path():
    env_list = ""
    for k, v in sorted(os.environ.items()):
        env_list += k + ":" + v + "<br/>"
    return env_list


@app.route('/current-time')
def current_time():
    date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
    return date


@app.route('/hello/<name>')
def hello(name):
    return "Hello \"%s\" !" % name


@app.route('/duplo')
def duplo():
    return "All-in-One DevSecOps Automation Platform"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8082)
