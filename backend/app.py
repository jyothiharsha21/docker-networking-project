from flask import Flask, jsonify
import pymysql
import os

app = Flask(__name__)

db = pymysql.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

@app.route("/")
def home():
    return "Backend Running Successfully"

@app.route("/employees")
def employees():

    cursor = db.cursor()

    cursor.execute("SELECT * FROM employees")

    result = []

    for row in cursor.fetchall():

        result.append({
            "id": row[0],
            "name": row[1],
            "department": row[2]
        })

    return jsonify(result)

app.run(host="0.0.0.0", port=5000)
