#!/usr/bin/python

import time

import os

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
    return endpoint


@app.route('/env-list')
def path():
    env_list = ""
    for k, v in sorted(os.environ.items()):
        env_list += k + ":" + v + "<br/>"
    return env_list


@app.route('/hello/<name>')
def hello(name):
    return "Hello \"%s\" !" % name


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8082)
