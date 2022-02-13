from flask import Flask, render_template, request, redirect
from datetime import datetime
from scripts import scripts

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/a")
def workout_a():
    lifts = scripts.get_lift_data("A")
    return render_template("workout_template.html",
                           workout="A",
                           description="upper body push",
                           date=datetime.now().strftime("%Y-%m-%d"),
                           lifts=lifts)


@app.route("/b")
def workout_b():
    lifts = scripts.get_lift_data("B")
    return render_template("workout_template.html",
                           workout="B",
                           description="upper body pull",
                           lifts=lifts)


@app.route("/c")
def workout_c():
    lifts = scripts.get_lift_data("C")
    return render_template("workout_template.html",
                           workout="C",
                           description="full body workout",
                           lifts=lifts)


@app.route("/up_lift", methods=['GET', 'POST'])
def up_lift():
    data = request.form
    date, lift = data['date'], data['lift']

    print(date, lift)

    scripts.increase_series(date, lift)
    return request.url
