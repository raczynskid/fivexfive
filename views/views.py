from flask import Flask, render_template, request, redirect, url_for
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
                           route="workout_a",
                           lifts=lifts)


@app.route("/b")
def workout_b():
    lifts = scripts.get_lift_data("B")
    return render_template("workout_template.html",
                           workout="B",
                           description="upper body pull",
                           date=datetime.now().strftime("%Y-%m-%d"),
                           route="workout_b",
                           lifts=lifts)


@app.route("/c")
def workout_c():
    lifts = scripts.get_lift_data("C")
    return render_template("workout_template.html",
                           workout="C",
                           description="full body workout",
                           date=datetime.now().strftime("%Y-%m-%d"),
                           route="workout_c",
                           lifts=lifts)


@app.route("/up_lift", methods=['GET', 'POST'])
def up_lift():
    data = request.form
    lift, url = data['lift'], data['url']

    scripts.increase_series(lift)
    return redirect(url_for(url))


@app.route("/finish", methods=['GET', 'POST'])
def finish():
    workout_type = request.form['workout_type']
    scripts.finish(workout_type)
    return redirect(url_for("index"))
