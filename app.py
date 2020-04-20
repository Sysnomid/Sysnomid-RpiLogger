#!/usr/bin/env python3
from db2 import *
from flask import Flask, render_template
from waitress import serve
import os
import re
import jinja2

app = Flask(__name__)

@app.route('/temp')
def display_tables():
	cursor.execute("SELECT * FROM pitemp order by ID desc;")
	data = cursor.fetchall()
	return render_template("index.html", data=data)

@app.route('/temp/wiki')
def wiki():
    cursor.execute("SELECT TEMP FROM pitemp ORDER BY ID DESC LIMIT 1;")
    data0 = cursor.fetchall()
    return render_template("wiki.html", data0=data0[0][0])

@app.after_request
def add_hostname_header(response):
    env_host = str(os.environ.get('HOSTNAME'))
    hostname = re.findall('[a-z]{3}-\d$', env_host)
    if hostname:
            response.headers["SP-LOCATION"] = hostname
    return response


if __name__ == "__main__": 
    serve(app, listen='*:8880') 
