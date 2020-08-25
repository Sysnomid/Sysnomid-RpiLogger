from flask import Flask, render_template
from logger import *

app = Flask(__name__,
            static_url_path='', 
            static_folder='assets/static',
            template_folder='assets/views')

@app.route("/")
def main():
    return render_template("index.html", ctemp=ctemp, ftemp=ftemp)

if __name__ == "__main__":
    app.run(host= '0.0.0.0')
