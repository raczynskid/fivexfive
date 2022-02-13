from db import db_connector as db


def increase_series(date, lift):
    db.update_series(date, lift)


def get_lift_data(workout_type):
    return db.get_lifts(workout_type)


def get_workout_lifts(workout_type):
    return db.get_workout_lifts(workout_type)


def get_workout(workout_type):
    lifts = get_workout_lifts("A")
    lift_data = get_lift_data(lifts)
