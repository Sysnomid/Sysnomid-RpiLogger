from db2 import *
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/temp')
def display_tables():
	cursor.execute("SELECT * FROM pitemp order by temp_id desc;")
	data = cursor.fetchall()
	return render_template("index.html", data=data)

@app.route('/temp/wiki')
def wiki():
    cursor.execute("SELECT temp_py FROM pitemp ORDER BY temp_id DESC LIMIT 1;")
    data0 = cursor.fetchall()
    return render_template("wiki.html", data0=data0)


if __name__ == "__main__": 
    app.run() 
