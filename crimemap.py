from dbhelper import DBHelper
from flask import Flask
from flask import render_template, request
from json import dumps

app = Flask(__name__)
DB = DBHelper()


@app.route('/')
def home():
    try:
        crimes = DB.get_all_inputs()
        crimes = dumps(crimes, indent=4, sort_keys=True, default=str)
    except Exception as e:
        print(e)
    return render_template("home.html", crimes=crimes)


@app.route("/submit_crime", methods=["POST"])
def add():
    crime_details = get_crime_details()
    try:
        DB.add_input(crime_details)
    except Exception as e:
        print(e)
    return home()


@app.route("/clear")
def clear():
    try:
        DB.clear_all()
    except Exception as e:
        print(e)
    return home()


def get_crime_details():
    category = request.form.get("category")
    date = request.form.get("date")
    latitude = float(request.form.get("latitude"))
    longitude = float(request.form.get("longitude"))
    description = request.form.get("description")
    crime_details = {"category": category,
                     "date": date,
                     "latitude": latitude,
                     "longitude": longitude,
                     "description": description}
    return crime_details


if __name__ == "__main__":
    app.run(debug=True)
