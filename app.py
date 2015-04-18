__author__ = 'Muin'
from flask import Flask, render_template, request, jsonify
#import extractdata

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


#get_results


#show_results


if __name__ == "__main__":
    #app.debug = True
    app.run()