import pymysql
import os

password = os.environ.get("EC2_password")

conn = pymysql.connect(
    host='fivexfive.c0syxj4d0fpm.eu-central-1.rds.amazonaws.com',
    port=3306,
    user="admin",
    password="#####",
    db='fivexfive',

)

cursor = conn.cursor()


def insert_lift(date, lift, series, weight):
    with conn.cursor() as cur:
        cur.execute("INSERT INTO fivexfive.Workouts (date,lift_name,series,weight) VALUES (%s,%s,%s,%s)",
                    (date, lift, series, weight))
        conn.commit()


def update_series(date, lift):
    sql_query = f"""UPDATE fivexfive.Workouts
          SET series = series + 1
          WHERE date = '{date}' AND lift_name = '{lift}';"""
    with conn.cursor() as cur:
        cur.execute(sql_query)
        conn.commit()
    print(date, lift)
    print("updated!")


def get_lifts(workout_type):
    sql_query = f"""SELECT 
                    cl.lift_name,
                    ll.series as last_series,
                    ll.weight as last_weight,
                    cl.series as current_series,
                    cl.weight as current_weight
                    FROM fivexfive.current_lift cl
                    INNER JOIN fivexfive.workout_lifts w ON cl.lift_name = w.lift_type
                                    AND w.workout = '{workout_type}'

                    INNER JOIN fivexfive.last_lift ll ON cl.lift_name = ll.lift_name;
    """
    print(sql_query)
    with conn.cursor() as cur:
        cur.execute(sql_query)
        conn.commit()
    columns = [column[0] for column in cur.description]
    results = []
    for row in cur.fetchall():
        results.append((dict(zip(columns, row))))
    return results


def get_workout_lifts(workout_type):
    sql_query = f"""SELECT lift_type FROM fivexfive.workout_lifts WHERE workout = '{workout_type}'"""
    with conn.cursor() as cur:
        cur.execute(sql_query)
    workout_lifts = [lift[0] for lift in cur.fetchall()]
    return workout_lifts
