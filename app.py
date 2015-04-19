__author__ = 'Muin'
from flask import Flask, render_template, request, jsonify
import extractdata

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/results", methods=["GET", "POST"])
def results():
    if request.method == "POST":
        course = request.form["course"].upper()
        c_avg, c_allprofs = extractdata.search_course(course)
        if "Course not found." in c_avg:
            return "Error."
        return render_template("results.html", course=course, c_avg=c_avg, c_allprofs=c_allprofs)
    else:
        return "Error."


if __name__ == "__main__":
    app.run()