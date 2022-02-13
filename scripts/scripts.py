from db import db_connector as db


def increase_series(lift):
    db.update_series(lift)


def get_lift_data(workout_type):
    return db.get_lifts(workout_type)


def get_workout_lifts(workout_type):
    return db.get_workout_lifts(workout_type)


def finish(workout_type):
    db.archive_current_lifts(workout_type)
    db.reset_current_lifts(workout_type)
