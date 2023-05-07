import csv
import time

import psycopg2


while True:
    try:
        conn = psycopg2.connect(
            host="localhost",
            port="5432",
            database="db_sunny_web",
            user="postgres",
            password="postgres",
        )
        cursor = conn.cursor()
        break
    except Exception as error:
        print(f"Error: {error}")
        # If connection is not posible, waith 2 seconds and try it again
        time.sleep(2)

with open("data.csv", newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",", quotechar="|")
    next(reader, None)  # skip the headers

    for row in reader:
        cursor.execute(
            """INSERT INTO t_power (created_at, power, daily_yield,
            total_yield) VALUES (%s, %s, %s, %s)""",
            (str(row[0]), row[1], row[2], row[3]),
        )
        conn.commit()
